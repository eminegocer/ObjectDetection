import cv2
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import Tk, Label, Canvas, Frame, BOTH
from PIL import Image, ImageTk
import numpy as np

net = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

response_times_raspberry = []
objects_detected = []

root = Tk()
root.title("Raspberry Pi Nesne Tanıma ve Tepki Süresi")
root.geometry("1200x700")

camera_frame = Frame(root)
camera_frame.pack(side="left", fill=BOTH, expand=True)
camera_label = Label(camera_frame)
camera_label.pack()

fig, ax = plt.subplots(figsize=(5, 4))
objects = ["person", "bottle", "book", "chair", "laptop"]
bars_raspberry = ax.bar(objects, [0] * len(objects), color='blue', label='Raspberry')
ax.set_xlabel("Nesne Türü")
ax.set_ylabel("Tepki Süresi (Saniye)")
ax.set_title("Raspberry Pi Tepki Süresi")
ax.legend()
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(side="right", fill=BOTH, expand=True)

def update_graph():
    global response_times_raspberry, objects_detected
    bar_heights_raspberry = []
    for obj in objects:
        raspberry_times = [
            response_times_raspberry[i] for i in range(len(objects_detected))
            if objects_detected[i] == obj
        ]
        if raspberry_times:
            bar_heights_raspberry.append(np.mean(raspberry_times))
        else:
            bar_heights_raspberry.append(0)

    for bar, height in zip(bars_raspberry, bar_heights_raspberry):
        bar.set_height(height)
    ax.set_ylim(0, max(bar_heights_raspberry) * 1.2 if bar_heights_raspberry else 1)
    canvas.draw()

def process_frame():
    global response_times_raspberry, objects_detected

    ret, frame = cap.read()
    if not ret:
        return

    height, width, channels = frame.shape
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (320, 320), (0, 0, 0), True, crop=False)
    net.setInput(blob)

    start_time_raspberry = time.time()
    outputs = net.forward(net.getUnconnectedOutLayersNames())
    response_times_raspberry.append(time.time() - start_time_raspberry)

    class_ids = []
    confidences = []
    boxes = []
    for output in outputs:
        for detection in output:
            scores = detection[5:]
            class_id = int(np.argmax(scores))
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
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f"{label}: {confidence:.2f}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            if label in objects:
                objects_detected.append(label)

        update_graph()

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img))
    camera_label.imgtk = img
    camera_label.configure(image=img)

    root.after(10, process_frame)

process_frame()
root.mainloop()

cap.release()
cv2.destroyAllWindows()