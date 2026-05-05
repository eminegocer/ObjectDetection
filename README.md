# Arduino and Raspberry Pi4 Object Detection Project

## Description
This project focuses on object detection using Arduino, Raspberry Pi 4, and the YOLOv4 model. A USB camera connected to the Raspberry Pi 4 captures the images, and objects are detected using the YOLOv4 model. When a specific object is identified, the corresponding LED on the Arduino is triggered to light up. The project aims to evaluate the performance and efficiency of Arduino and Raspberry Pi 4 hardware in real-time object detection.

## Features
- Object detection using YOLOv4.
- Real-time object identification via a USB camera connected to Raspberry Pi 4.
- Arduino triggers LEDs to indicate recognized objects.
- Performance and efficiency measurement of Arduino and Raspberry Pi 4 hardware.

## Technologies Used
- **Hardware**:
  - Arduino
  - Raspberry Pi 4
  - USB Camera
  - LEDs
- **Software**:
  - YOLOv4 Object Detection Model
  - Python for Raspberry Pi programming
  - Arduino IDE for microcontroller programming
  - OpenCV for image processing

## Setup
1. Connect the USB camera to the Raspberry Pi 4.
2. Upload the Arduino code to the microcontroller using the Arduino IDE.
3. Install necessary Python libraries for YOLOv4 on the Raspberry Pi:
## Model Files
The YOLO model files are stored externally due to size constraints. Download them from the following link:
[Download YOLO Models](https://drive.google.com/file/d/1YHB8XA6gKgN_wgjmSJKbKTTeveajuWFH/view)

 
## Banka için “varlık” nedir?
Sistem içinde değeri olan, çalışmayı sağlayan veya veri barındıran her bileşen bir varlıktır.
Altyapı (Infrastructure) varlıkları
En temel ve en görünür olanlardır:
-	Web sunucuları (internet bankacılığı) 
-	Uygulama sunucuları 
-	Veritabanı sunucuları 
-	Network cihazları (firewall, router, switch) 
-	Load balancer sistemleri 
Örnek:
-	10.0.0.5 → Web server 
-	10.0.0.10 → Database server 
________________________________________
# Uygulama varlıkları
Kullanıcıların doğrudan etkileşimde olduğu sistemlerdir:
-	İnternet bankacılığı web uygulaması 
-	Mobil bankacılık backend sistemleri 
-	API servisleri 
Örnek:
-	/login endpoint 
-	/api/transfer servisi 
________________________________________
# Modern (cloud / container) varlıklar
-	Docker container’lar 
-	Kubernetes pod’ları 
-	Cloud servisleri (VM, storage vs.) 
________________________________________
# Kimlik ve erişim varlıkları
-	Active Directory kullanıcıları 
-	Admin hesapları 
-	Servis hesapları 
________________________________________
 # Veri (dolaylı varlıklar)
Doğrudan Bizzy’de “asset” olarak görünmeyebilir ama çok kritiktir:
-	Müşteri verileri 
-	Finansal kayıtlar 
-	Kredi bilgileri 
________________________________________
# Kritik fark 
IP adresi bir varlık değildir, varlığın kimliğidir
Yani:
- 10.0.0.5 → bir web sunucusunu temsil eder 
- Asıl varlık → o sunucunun kendisidir 
________________________________________
# Varlıklar neden gruplandırılır?
Varlıkları tek tek yönetmek imkansızdır.
 Bu yüzden gruplama yapılır:
-	Yönetimi kolaylaştırmak 
- Önceliklendirme yapmak 
-	Doğru kişiye atama yapmak 
- Raporlama oluşturmak 
________________________________________
# Varlıklar neye göre gruplandırılır?

Genelde birden fazla kriter birlikte kullanılır.
________________________________________
# Ortama göre (Environment-based)
En yaygın gruplama türüdür:
-	Production (canlı sistemler) 
- Test 
- Development 
 Önemi:
- Aynı zafiyet → prod’da kritik, testte önemsiz olabilir 
________________________________________
# İş fonksiyonuna göre (Business-based)
Bankalar için en önemli gruplamadır:
-	İnternet bankacılığı 
-	Ödeme sistemleri 
-	ATM altyapısı 
-	Kredi sistemleri 
Bu sayede:
“En kritik iş süreçlerinde hangi açıklar var?” sorusu cevaplanır
________________________________________
# Teknolojiye göre (Technology-based)
Teknik ekipler için faydalıdır:
- Web sunucuları 
-	Database sunucuları 
- Linux sistemler 
-	Windows sistemler 
________________________________________
# Network konumuna göre
Güvenlik açısından çok önemlidir:
	DMZ (internete açık sistemler) 
-	Internal network 
- VPN erişimli sistemler 
________________________________________
# Sahiplik (Owner-based)
-	Kişi bazlı (Ahmet, Ayşe) 
-	Ekip bazlı (DevOps Team, Security Team) 
________________________________________
# Kritiklik / risk bazlı
Bazı sistemlerde:
-	High critical assets 
-	Medium 
-	Low 
eklinde gruplama yapılır.
________________________________________
# Bizzy’de bu yapı nasıl kullanılır?
Bu gruplar sadece “etiket” değildir, aktif olarak kullanılır:
-  Filtreleme: “Sadece prod sistemlerdeki açıkları göster” 
- Atama:	Belirli grup → belirli ekibe gider 
- Risk hesaplam:	Kritik gruplardaki açıklar daha yüksek risk alır 
- Raporlama: 	“İnternet bankacılığında kaç açık var?” 
________________________________________
Gerçek banka senaryosu
Diyelim ki bir sunucu var:
•	IP: 10.0.0.5 
•	Sistem: Internet Banking Server 
Bu varlık şu gruplarda olabilir:
•	Production 
•	DMZ 
•	Web Servers 
•	Internet Banking 
•	Web Team (owner) 
👉 Bu ne sağlar?
Bir zafiyet geldiğinde sistem şunu anlar:
•	Prod → kritik 
•	DMZ → dışa açık 
•	Internet Banking → iş kritik 
➡️ Risk skoru otomatik yükselir
