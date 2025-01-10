import cv2
import serial
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Label, Canvas, Frame, BOTH
from PIL import Image, ImageTk
import numpy as np
import atexit  # Program sonlandığında işlemleri temizlemek için

# Arduino ile seri bağlantıyı başlat
arduino = serial.Serial('COM3', 9600)  # Arduino'nuzun bağlı olduğu COM portunu kontrol edin
time.sleep(2)  # Arduino'nun hazır hale gelmesini bekleyin

# Program kapandığında LED'leri kapatmak için bir fonksiyon
def cleanup():
    print("Program sonlanıyor, LED'ler kapatılıyor...")
    arduino.write(b'x')  # Tüm LED'leri kapat
    arduino.close()  # Arduino bağlantısını kapat

atexit.register(cleanup)  # Program sonlandığında cleanup fonksiyonu çağrılacak

# YOLO modelini yükleme
net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers().flatten()]

classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Kamerayı başlat ve çözünürlüğü optimize et
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# Dinamik grafik için veriler
response_times = []
objects_detected = []

# Tkinter GUI Ayarları
root = Tk()
root.title("Nesne Tanıma ve Dinamik Grafik")
root.geometry("1200x700")

# Kamera Görüntüsü için Canvas
camera_frame = Frame(root)
camera_frame.pack(side="left", fill=BOTH, expand=True)
camera_label = Label(camera_frame)
camera_label.pack()

# Grafik için Matplotlib
fig, ax = plt.subplots(figsize=(5, 4))
objects = ["person", "bottle", "book", "chair", "laptop"]
bars = ax.bar(objects, [0] * len(objects), color='blue')
ax.set_xlabel("Nesne Türü")
ax.set_ylabel("Arduino Tepki Süresi (saniye)")
ax.set_title("Nesneye Göre Arduino Tepki Süresi")
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side="right", fill=BOTH, expand=True)

def update_graph():
    """
    Tepki sürelerini dinamik olarak grafikte günceller.
    """
    global response_times, objects_detected
    bar_heights = []
    for obj in objects:
        obj_times = [response_times[i] for i in range(len(objects_detected)) if objects_detected[i] == obj]
        if obj_times:
            bar_heights.append(np.mean(obj_times))
        else:
            bar_heights.append(0)

    for bar, height in zip(bars, bar_heights):
        bar.set_height(height)
    ax.set_ylim(0, max(bar_heights) * 1.2 if bar_heights else 1)  # Y-ekseni dinamik ayar
    canvas.draw()

def process_frame():
    """
    Kameradan görüntüyü alır, YOLO ile nesne tanır ve Arduino tepki süresini ölçer.
    """
    ret, frame = cap.read()
    if not ret:
        print("Kamera görüntüsü alınamıyor!")
        return

    height, width, channels = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (320, 320), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outputs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = int(scores.argmax())
            confidence = scores[class_id]
            if confidence > 0.3:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    led_signal = None
    label = None
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]

            # Çerçeve çiz
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"{label}: {confidence:.2f}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Algılanan nesneye göre LED kontrolü
            if label == "person":
                led_signal = '0'
            elif label == "bottle":
                led_signal = '1'
            elif label == "book":
                led_signal = '2'
            elif label == "chair":
                led_signal = '3'
            elif label == "laptop":
                led_signal = '4'

    if led_signal:
        arduino.write(led_signal.encode())
        start_time = time.time()
        while arduino.in_waiting == 0:
            pass
        response = arduino.readline().decode().strip()
        response_time = time.time() - start_time
        response_times.append(response_time)
        objects_detected.append(label.lower())

        # Konsola istenilen formatta çıktı yazdırma
        print(f"Tanınan Nesne: {label}, Arduino Tepki Süresi: {response_time:.4f} saniye, Mesaj: {response}")

        # Grafiği güncelle
        update_graph()
    else:
        # Hiçbir nesne algılanmazsa LED'leri kapat
        arduino.write(b'x')
        print("Nesne algılanmadı, tüm LED'ler kapatıldı.")

    # Kamera görüntüsünü güncelle
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img))
    camera_label.imgtk = img
    camera_label.configure(image=img)

    # Tekrar çağır
    root.after(10, process_frame)

# Kameradan işlem başlat
process_frame()
root.mainloop()

cap.release()
cv2.destroyAllWindows()
