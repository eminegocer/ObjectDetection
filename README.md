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

Nessus ile Doğrulama ve Politika Yapılandırması
Bu bölümde, tespit edilen zafiyetlerin (CVE-2026-39808 ve CVE-2026-39813) Nessus güvenlik tarayıcısı kullanılarak nasıl doğrulanacağı ve tarama sırasında izlenmesi gereken metodoloji açıklanmaktadır.

6.1. Doğrulama Yaklaşımı
Söz konusu zafiyetlerin doğrulanmasında Nessus, aktif istismar (exploit) yöntemleri yerine sürüm ve servis tespiti (version-based detection) metodolojisini kullanmaktadır. Bu süreçte tarayıcı; cihaz tipini tanımlar, çalışan yazılım sürümünü belirler ve elde edilen veriyi bilinen CVE veritabanı ile eşleştirerek risk durumunu raporlar.

6.2. Tarama Politikası (Scan Policy) Konfigürasyonu
Doğru bir tespit için Nessus üzerinde "Basic Network Scan" şablonu temel alınarak aşağıdaki kritik yapılandırmalar uygulanmalıdır:

Port ve Servis Tespiti: Cihazın yönetim arayüzlerine erişim sağlayan 443 (HTTPS) ve 80 (HTTP) portları öncelikli olmak üzere standart TCP port taraması aktif edilmelidir. "Service Detection" modülü, FortiSandbox servisinin doğru tanımlanması için açık tutulmalıdır.

Plugin Yapılandırması: Tarama sırasında; Web Servers, CGI Abuses, Service Detection ve Fortinet Appliance Detection kategorisindeki plugin'lerin aktif olduğundan emin olunmalıdır. Bu plugin'ler, cihazın imzasını ve CVE eşleşmelerini analiz eder.

Kimlik Bilgisi (Credentials): İlgili zafiyetlerin tespiti için kimlik bilgisi kullanımı zorunlu değildir. "Unauthenticated Scan" (Kimlik bilgisiz tarama) yöntemi, dışarıdan sürüme bağlı risk tespiti yapmak için yeterlidir.

Güvenli Tarama (Safe Checks): Üretim ortamındaki cihazın sürekliliğini korumak adına "Safe Checks" ayarı mutlaka aktif edilmelidir.

6.3. Uygulama ve Analiz Süreci
Tarama işlemi tamamlandıktan sonra elde edilen sonuçlar aşağıdaki kriterlere göre analiz edilir:

Beklenen Bulgular: Nessus raporunda cihazın "FortiSandbox" olarak tanımlanması ve etkilenen sürüm aralıklarından birinin (4.4.0–4.4.8 veya 5.0.0–5.0.5) raporlanması beklenmektedir.

CVE Referansları: Rapor çıktısında CVE-2026-39808 ve CVE-2026-39813 kodlarının doğrudan referans gösterilmesi, zafiyetin varlığını kanıtlar.

Doğrulama Durumu: Sistem sürümü zafiyetli aralıkta yer alıyor ve Nessus çıktısı bu sürümü "Kritik" olarak işaretliyorsa, bulgu teknik olarak doğrulanmış kabul edilir.

6.4. Sonuç ve Önemli Notlar
Nessus tarafından gerçekleştirilen bu işlem, zafiyetin varlığını sürüm bazlı (evidence-based) olarak kanıtlar; ancak gerçek bir exploit testi gerçekleştirmez. Bu nedenle Nessus çıktıları, sızma testi raporlarında ön doğrulama kanıtı olarak sunulmalı ve gerek görüldüğü takdirde kontrollü ortamlarda gerçekleştirilen manuel testlerle desteklenmelidir.

Rapor Özeti: Zafiyet doğrulama sürecinde Nessus tarayıcısı kullanılmıştır. Yapılan analiz sonucunda hedef sistemin FortiSandbox ürününe ait etkilenen sürümleri çalıştırdığı tespit edilmiş ve ilgili bulgular CVE referansları ile eşleştirilmiştir. Bu tespit, zafiyetlerin sistem üzerinde potansiyel olarak istismar edilebilir olduğunu teknik verilerle ortaya koymaktadır.


