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











Nessus Plugin Türleri
Local (Authenticated) Plugins
-	Sisteme kullanıcı adı/şifre ile giriş yaparak çalışır 
-	Yüklü yazılımları kontrol eder 
-	Eksik patch (güncelleme) tespiti 
-	Registry / config dosyası analizi
-	Credentialed Scanda kullanılır (Windows domain taraması (AD ortamı), Sunucu güvenlik denetimi)
Remote (Unauthenticated) Plugins
-	Sisteme giriş yapmadan dışarıdan tarar
-	Açık portlar ,  Servis versiyonları,  Bilinen zafiyetleri (banner grabbing ile) tarar
-	Basic Network Scanda kullanılır
Network Service Plugins
-	Ağ servislerini hedef alır 
-	HTTP, FTP, SSH, SMB gibi servislerde zafiyet arar
-	Web + network taramalarında kullanılır


Windows / Unix Plugins
-	İşletim sistemine özel controller
-	Patch eksikleri, SMB açıkları, Paket zafiyetleri, SSH config hataları
-	Credentialed Scanda kullanılır
Compliance Plugins
-	Güvenlik standartlarına uygunluk kontrolü
-	Compliance Scanda kullanılır

Web Application Plugins
-	Web uygulamalarını test eder
-	XSS, SQL Injection, Directory traversal 
-	Web Application Scanda kullanılır

Denial of Service (DoS) Plugins
-	Sistemi zorlayarak DoS açığı test eder
-	Genelde kapalıdır, test ortamlarında kullanılır.

Policy Compliance / Audit Plugins
-	Sistem yapılandırmasını analiz eder 
-	Şifre politikaları, Firewall kuralları, Güvenlik ayarları 
-	 Audit + Hardening testleri
Malware Detection Plugins
-	Zararlı yazılım izleri arar 
-	Backdoor, Botnet bağlantıları
-	Incident response / forensic analiz
General / Information Plugins
-	Bilgi toplama
-	OS tespiti, Açık port listesi, Servis bilgisi 
-	 Tüm taramaların temelidir



 
https://drive.google.com/file/d/1cA5jtzvYWB0QagmoKBei5ViOhuN7RfC6/view?usp=drive_link 






Remote (Unauthenticated) Taramada Aktif Olması Gereken Pluginler
-	“Dış saldırgan ne görür?” mantığı
-	Açık portlar, Servisler,  Versiyon bazlı zafiyetler,  Yanlış konfigürasyonlar
Network / Service Discovery
-	Port scanning 
-	Service detection 
-	Banner grabbing

General
-	OS detection 
-	Host discovery
Web Servers
-	HTTP/HTTPS zafiyetleri 
-	SSL/TLS hataları 
SSL / TLS
-	Sertifika hataları 
-	Eski protokoller (TLS 1.0 vs)
Databases
-	MySQL, MSSQL, Oracle servisleri
DNS
-	Zone transfer 
-	DNS misconfiguration

Credentialed (Authenticated) Taramada Aktif Pluginler
-	“İç denetim / gerçek güvenlik durumu”
Local Security Checks 
-	Patch kontrolü 
-	CVE bazlı analiz
Windows Plugins  
-	SMB üzerinden detaylı analiz 
-	Registry kontrolü 
Unix / Linux Plugins
-	Paket zafiyetleri 
-	SSH config analizi
Configuration Audit
-	Güvenlik ayarları 
-	Hardening kontrolü
Patch Management
-	Eksik güncellemeler 
-	Kritik security patch’ler
Authentication
-	Weak password policy 
-	Account config hataları


Performance Options
taramanın ne kadar hızlı, ne kadar agresif ve hedef sistemi ne kadar zorlayarak yapılacağını belirler.
Yanlış ayarlanırsa zfiyetler kaçırılabilir, system yavaşlaayabilir ve kesintiye sebep olabilir.
aynı anda kaç host’un taranacağı, bir host’a kaç paralel bağlantı açılacağı, istekler arasındaki gecikme (delay), timeout süreleri ve ağa gönderilen trafik yoğunluğunu control eder
Kurumsal bir ortamda kritik varlıklar dediğimizde, örneğin ödeme altyapısı ya da canlı müşteri verisi işleyen sunucuları gibi sistemleri düşün. Bu tür sistemlerde öncelik her zaman erişilebilirlik (availability) olduğu için taramanın agresif olması istenmez. Bu yüzden performans ayarları daha kontrollü yapılır. Aynı anda taranan host sayısı düşük tutulur, paralel bağlantı sayısı azaltılır ve istekler arasına küçük gecikmeler eklenir. Timeout değerleri biraz daha yüksek tutulur ki sistem geç cevap verse bile yanlış negatif oluşmasın. Ayrıca ağ yoğunluğu sınırlanır, yani Nessus’un bir anda çok fazla trafik üretmesi engellenir.
Bu yaklaşımın amacı şudur: “Zafiyet bulayım ama sistemi riske atmayayım yanlış yapılandırılmış agresif bir tarama, gerçek bir DoS etkisi yaratabilir. Bu yüzden çoğu kurum kritik sistemleri ya mesai dışı saatlerde tarar ya da düşük yoğunluklu (throttled) tarama profili kullanır.
________________________________________
Buna karşılık genel kurumsal taramalar (örneğin ofis bilgisayarları, test ortamları, staging sunucuları) daha esnek ortamlardır. Burada performans ayarları daha agresif olabilir çünkü sistemlerin çökmesi kritik bir iş kesintisi yaratmaz. Bu yüzden aynı anda daha fazla host taranabilir, her host’a daha fazla paralel bağlantı açılabilir ve gecikmeler minimumda tutulur. Tarama süresi kısalır ve daha hızlı sonuç alınır.
Bu senaryoda amaç şudur: “Mümkün olduğunca hızlı ve kapsamlı tarama yap.” Özellikle büyük ağlarda binlerce cihaz varsa, düşük performans ayarlarıyla tarama günler sürebilir. Bu yüzden burada hız önceliklidir.
________________________________________
İki yaklaşımı zihninde şöyle ayırabilirsin: kritik sistemlerde Nessus “nazik” davranır, genel sistemlerde ise “agresif”. Yani aynı araç ama davranış şekli hedefe göre değişir.


