import matplotlib.pyplot as plt
import numpy as np

# Veriler (ms'den s'ye çevrildi)
objects = ['Person', 'Bottle','Book', 'Chair', 'Laptop']
arduino_times = [0.0068 / 1000, 0.0068 / 1000, 0.0067 / 1000, 0.0067 / 1000, 0.0069/1000]  # ms -> s
raspberry_times = [1.76 / 1000, 1.57 / 1000, 1.64 / 1000, 1.75 / 1000, 1.58 / 1000]  # ms -> s

# Grafik oluşturma
x = np.arange(len(objects))
width = 0.35

fig, ax = plt.subplots()
bars_arduino = ax.bar(x - width/2, arduino_times, width, label='Arduino', color='blue')
bars_raspberry = ax.bar(x + width/2, raspberry_times, width, label='Raspberry Pi', color='green')

# Grafik detayları
ax.set_xlabel('Nesneler')
ax.set_ylabel('Tepki Süresi (s)')  # Birimi değiştirdik
ax.set_title('Arduino ve Raspberry Pi Tepki Süreleri Karşılaştırması')
ax.set_xticks(x)
ax.set_xticklabels(objects)
ax.legend()

# Grafiği göster
plt.tight_layout()
plt.show()
