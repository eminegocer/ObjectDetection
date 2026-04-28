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






BlueHammer Zafiyeti

Cloud Files API ve dosya kilitleme (opportunistic locking) mekanizmalarının etkileşiminden kaynaklanan bir yerel ayrıcalık yükseltme (Local Privilege Escalation - LPE) zafiyetidir. Bu zafiyet, normal bir kullanıcı yetkisine sahip bir saldırganın, sistem bileşenlerinin belirli bir zamanlama hatasından yararlanarak NT AUTHORITY\SYSTEM seviyesine yükselmesine olanak tanımaktadır. Temel problem, Defender’ın güncelleme veya tarama süreçleri sırasında VSS tarafından oluşturulan sistem anlık görüntüsünün (snapshot) erişim penceresinin, Cloud Files callback ve dosya kilitleme mekanizmalarıyla birlikte manipüle edilebilmesidir. Bu durum, kritik sistem dosyalarının (SAM, SYSTEM, SECURITY hive’ları) snapshot üzerinden erişilebilir hale gelmesine ve saldırganın yerel kimlik doğrulama verilerini elde ederek sistem üzerinde tam kontrol sağlamasına yol açmaktadır. Zafiyet birden fazla meşru Windows bileşeninin öngörülmeyen şekilde bir araya gelmesinden kaynaklanan bir tasarım ve zamanlama (race condition) problemidir.

Etki Noktaları:
•	Kurumsal endpoint cihazları (Domain’e bağlı kullanıcı bilgisayarları)
Standart kullanıcı yetkisine sahip domain-joined workstation’lar üzerinden saldırı başlatılabildiği için kurumsal istemci ortamları yüksek risk altındadır.
•	Defender Antivirus aktif Windows sunucuları
Defender ve VSS bileşenleri aktif olan Windows Server sistemleri (özellikle dosya sunucuları ve uygulama sunucuları) etkilenebilir.
•	Yedekleme / snapshot kullanılan sistemler (VSS bağımlı altyapılar)
Volume Shadow Copy kullanan backup agent’ları veya sistem geri yükleme aktif olan sunucular, snapshot manipülasyonu nedeniyle risk altındadır.
•	Cloud Files API kullanan senkronizasyon altyapısına sahip sistemler
OneDrive / benzeri sync altyapıları bulunan ve Cloud Files callback mekanizmasını destekleyen Windows ortamları saldırı zincirinin bir parçası olabilir
•	Least privilege kullanıcıların erişim sağlayabildiği çok kullanıcılı sistemler
Birden fazla düşük yetkili kullanıcının erişebildiği paylaşımlı sistemlerde saldırı yüzeyi artar (örneğin eğitim, lab, terminal server ortamları).

Olası Saldırı Sonuçları:
•	Sistem üzerinde tam kontrol elde edilmesi (SYSTEM yetkisi kazanımı)
Saldırgan, yerel kullanıcıdan NT AUTHORITY\SYSTEM seviyesine yükselerek işletim sistemi üzerinde en yüksek yetkiyi elde edebilir. 
•	Kimlik bilgisi hırsızlığı (Credential Dumping)
SAM ve SYSTEM hive’ları üzerinden NTLM hash’leri ve yerel kullanıcı parolaları elde edilerek kimlik doğrulama verileri çalınabilir. 
•	Yetkili hesapların ele geçirilmesi
Yerel Administrator hesapları dahil olmak üzere tüm yerel hesaplar üzerinde kontrol sağlanabilir ve kimlik taklidi yapılabilir. 
•	Yan hareket (Lateral Movement) imkânı
Ele geçirilen kimlik bilgileri ile domain ortamında diğer sistemlere geçiş yapılabilir. 
•	Hassas veri sızıntısı (Data exfiltration)
Sistem içindeki dosyalar, kullanıcı verileri ve uygulama konfigürasyonları saldırgan tarafından erişilip dışarı aktarılabilir. 
•	Sistem bütünlüğünün bozulması
Kritik sistem dosyalarının değiştirilmesi, servislerin manipüle edilmesi veya güvenlik yapılandırmalarının devre dışı bırakılması mümkündür. 

Zafiyetin Doğrulanması
BlueHammer zafiyeti, imza tabanlı bir yazılım hatasından ziyade Windows bileşenleri arasındaki etkileşimden kaynaklanan bir tasarım kusuru olduğu için, klasik vulnerability scanner araçları (örneğin Nessus) tarafından doğrudan “exploit tespiti” şeklinde işaretlenmeyebilir. Bu nedenle doğrulama süreci, hem otomatik tarama hem de davranışsal analiz kombinasyonu ile gerçekleştirilmelidir.
Nessus Tabanlı Ön Değerlendirme
Nessus credentialed scan kullanılarak hedef sistem analiz edilmelidir. Bu aşamada amaç zafiyeti doğrudan tespit etmek değil, saldırı yüzeyinin uygunluğunu belirlemektir.
•	Windows sisteminde Microsoft Defender servisinin aktif olup olmadığı kontrol edilir 
•	Volume Shadow Copy Service (VSS) yapılandırması ve erişilebilirliği analiz edilir 
•	Cloud Files API ve sync root mekanizmalarının mevcut olup olmadığı incelenir 
•	Kullanıcı yetki seviyeleri ve local privilege escalation’a uygun yapı kontrol edilir 
Nessus tarafında özellikle Windows enumeration ve misconfiguration plugin sonuçları değerlendirilerek sistemin BlueHammer saldırı zincirine uygun bir ortam olup olmadığı analiz edilir.

Davranışsal ve Manuel Doğrulama
Sistem üzerinde manuel doğrulama gerçekleştirilir. Bu aşamada amaç exploit çalıştırmak değil, zafiyet için gerekli bileşenlerin davranışlarını gözlemlemektir.
•	Defender servisinin aktif olduğu ve sistemde tarama/güncelleme süreçlerinin çalıştığı doğrulanır 
•	VSS servisinin çalışır durumda olduğu ve shadow copy oluşturabilme kapasitesi kontrol edilir 
•	Cloud Files API çağrılarının sistemde mevcut olduğu tespit edilir 
•	Standart kullanıcı hesabının bu bileşenlere erişim seviyeleri analiz edilir 
Bu kontroller sırasında özellikle sistemin snapshot oluşturma davranışı ve kullanıcı süreçlerinin bu süreçlerle etkileşimi gözlemlenir.


Davranışsal Log Analizi (EDR / Event Logs)
Doğrulama sürecinin kritik bir parçası da log tabanlı analizdir:
•	Windows Defender Operational logları incelenir 
•	VSS snapshot oluşturma olayları takip edilir 
•	Cloud Files API ile ilgili erişim ve callback aktiviteleri kontrol edilir 
•	Event ID 4723 / 4724 gibi yerel kullanıcı parola değişiklik olayları izlenir 
•	Standart kullanıcı süreçlerinden gelen servis oluşturma (CreateService) girişimleri analiz edilir 

Etkilenen Sürümler
BlueHammer zafiyeti, belirli bir yazılım hatasından ziyade Windows’un modern mimarisinde yer alan bileşenlerin etkileşiminden kaynaklandığı için aşağıdaki işletim sistemi sürümlerini potansiyel olarak etkiler:
•	Windows 10 (1909 ve sonrası tüm desteklenen sürümler) 
•	Windows 11 (tüm güncel ve desteklenen sürümler) 
•	Microsoft Defender Antivirus’in aktif olduğu Windows kurulumları 
•	Volume Shadow Copy Service (VSS) aktif olan sistemler 
•	Cloud Files API (CfAPI) desteği bulunan Windows build’leri 
•	Kurumsal ve bireysel tüm Windows client workstation ortamları


Çözüm Önerileri:
BlueHammer zafiyeti klasik bir yazılım hatasından ziyade Windows bileşenlerinin etkileşiminden kaynaklanan bir tasarım problemi olduğu için tek bir “patch” yaklaşımı yeterli değildir. Bu nedenle çözüm, hem Microsoft seviyesinde güncellemeleri hem de sistem yöneticisi seviyesinde güvenlik sertleştirme (hardening) önlemlerini içermelidir.
•	Güncellemeler: Windows ve Microsoft Defender en güncel sürüme yükseltilmeli, özellikle VSS, Defender ve Cloud Files bileşenlerine yönelik güvenlik yamaları düzenli olarak uygulanmalıdır. 
•	Yetki kısıtlaması (Least Privilege): Kullanıcılara gereksiz admin yetkisi verilmemeli, Cloud Files API ve VSS gibi kritik bileşenlere standart kullanıcı erişimi sınırlandırılmalıdır. 
•	Davranışsal izleme: Standart kullanıcı süreçlerinden gelen VSS erişimleri, Cloud Files API çağrıları ve servis oluşturma (CreateService) girişimleri SIEM/EDR üzerinde anomali olarak izlenmelidir. Özellikle ardışık yerel admin parola değişiklikleri (Event ID 4723/4724) kontrol edilmelidir. 
•	Sistem sertleştirme: VSS ve Cloud Files erişimi yalnızca sistem servisleriyle sınırlandırılmalı, gereksiz Windows bileşenleri kapatılmalı ve kritik sistemlerde sıkı uygulama kontrolü (WDAC/AppLocker) uygulanmalıdır.



Nessus üzerinde “Windows Local Privilege Escalation”, “Microsoft Defender Security Bypass” veya “Shadow Copy / VSS exposure” kategorilerine ait plugin’ler (Windows Local Privilege Escalation Checks, Microsoft Windows Defender Detection Plugins vs.) çalıştırılarak sistemde bilinen zayıf yapılandırmalar, eksik yamalar veya riskli servis davranışları kontrol edilir. Ayrıca sistemde Defender güncelleme mekanizması, shadow copy servis durumu ve kullanıcı yetki seviyeleri ile ilgili güvenlik kontrollerinin yanlış yapılandırılıp yapılandırılmadığı raporlanır.
Manuel doğrulama kapsamında hedef sistemde standart kullanıcı yetkisine sahip bir hesap ile oturum açılır ve Defender güncelleme/tarama süreçleri sırasında VSS snapshot oluşumu gözlemlenir. Bu süreçte Event Viewer (Windows Event Logs), özellikle Defender (Microsoft-Windows-Windows Defender/Operational) ve VSS logları incelenerek snapshot oluşturma ve dosya erişim aktiviteleri doğrulanır.
Ek olarak, Cloud Files API ile ilişkili aktiviteler ve oplock mekanizmalarının tetiklenip tetiklenmediği Process Monitor (Sysinternals) veya benzeri izleme araçları ile analiz edilir. Şüpheli durumlar arasında kullanıcı süreçlerinin shadow copy cihaz yollarına erişim denemeleri, sistem hive dosyalarına (SAM, SYSTEM, SECURITY) yönelik erişim girişimleri ve Defender süreçlerinin bekleme/delay durumuna girmesi yer alır.





Adobe Acrobat Zafiyeti
Bu zafiyet, Adobe Acrobat Reader uygulamasında bulunan ve henüz yamalanmamış (zero-day) bir güvenlik açığının, kötü amaçlı hazırlanmış PDF dosyaları aracılığıyla istismar edilmesiyle ortaya çıkan bir uzaktan kod çalıştırma (RCE) ve sandbox bypass riski oluşturmaktadır.
Saldırı, kullanıcı etkileşimi minimum seviyede olacak şekilde tasarlanabilmektedir; hedef kullanıcı yalnızca zararlı PDF dosyasını açtığında exploit tetiklenmektedir. PDF içerisine gömülü JavaScript kodları ve Acrobat’ın yerleşik API fonksiyonlarının kötüye kullanılması sayesinde saldırgan, yerel dosya sistemine erişim sağlayabilmekte ve sistem hakkında bilgi toplayabilmektedir.
Bu zafiyetin temel risk noktası, Adobe Acrobat Reader’ın PDF işleme motoru içerisinde bulunan meşru fakat geniş yetkilere sahip API’lerin (örneğin dosya okuma ve ağ iletişimi sağlayan fonksiyonlar) yeterince kısıtlanmadan çalıştırılabilmesidir. Saldırgan bu API’leri kullanarak:
•	Yerel dosyaları okuyabilmekte 
•	Sistem ve kullanıcı ortamını keşfedebilmekte 
•	Toplanan verileri dış bir sunucuya iletebilmektedir 
Daha ileri saldırı senaryolarında ise bu zafiyet, sandbox izolasyonunun aşılması ile birleştiğinde uzaktan komut çalıştırma (RCE) seviyesine kadar ilerleyebilmekte ve hedef sistemin tamamen ele geçirilmesine yol açabilmektedir.
Zafiyet özellikle phishing kampanyaları ile dağıtılan PDF dosyaları üzerinden aktif olarak istismar edilmekte olup, tespit edilmesi zor bir yapıya sahiptir çünkü saldırı akışı, Adobe Acrobat’ın normal çalışma davranışları ile büyük ölçüde örtüşmektedir.


Etki Noktaları:
•	Son Kullanıcı Sistemleri (Endpoint’ler)
•	Yerel Dosya Sistemi (Local File System)
•	Acrobat Reader Sandbox Ortamı
•	Kullanıcı Hesapları ve Kimlik Bilgileri


Olası Saldırı Sonuçları
•	Hassas Veri Sızıntısı (Information Disclosure)
Kullanıcıya ait tüm yerel ve tarayıcı tabanlı hassas veriler ifşa olabilir.

•	Kimlik Bilgisi Hırsızlığı (Credential Theft)
•	Sistem Bilgisi Toplanması (System Reconnaissance)
•	Sandbox Bypass
•	Veri Sızdırma
•	Yatay Yayılım (Lateral Movement)

Zafiyetin Doğrulanması
Nessus ile Doğrulama
Nessus üzerinde credentialed scan kullanılarak hedef sistemler analiz edilmelidir. Bu aşamada temel amaç, Adobe Acrobat Reader uygulamasının etkilenen sürümde olup olmadığını ve sistemin genel saldırı yüzeyinin exploit zincirine uygunluğunu belirlemektir.
Bu kapsamda Nessus tarafından aşağıdaki kontroller değerlendirilir:
•	Hedef sistemde kurulu Adobe Acrobat Reader sürümü tespit edilir ve vulnerability feed ile karşılaştırılır 
•	Windows Installed Software Enumeration üzerinden Acrobat kurulum bilgileri analiz edilir 
•	Patch seviyesinin güncel olup olmadığı kontrol edilir 
•	JavaScript execution desteğinin aktif olduğu Acrobat yapılandırmaları tespit edilir 
•	Protected Mode (sandbox) özelliğinin aktif veya devre dışı durumu değerlendirilir 
•	Kullanıcı yetki seviyesi (local admin / standard user) analiz edilerek saldırının etki potansiyeli belirlenir 
Nessus çıktıları bu aşamada doğrudan exploit doğrulaması sağlamaz; bunun yerine sistemin “vulnerable configuration” içerip içermediğini ve Adobe tarafından yayınlanan güvenlik yamalarına karşı güncel olup olmadığını ortaya koyar. Eğer kurulu sürüm etkilenen versiyon aralığında yer alıyorsa sistem “potansiyel olarak vulnerable” olarak sınıflandırılır.

Davranışsal Doğrulama
Nessus sonuçlarının doğrulanması için kontrollü test ortamlarında davranışsal analiz yapılması önerilir. Bu aşamada amaç exploit’in aktif olarak tetiklenip tetiklenmediğini gözlemlemektir.
Bu kapsamda:
•	Kontrollü bir PDF dosyasının Acrobat Reader üzerinde açılması sırasında process davranışı izlenir 
•	Sysmon veya Procmon kullanılarak Acrobat process’inin dosya sistemi erişimleri analiz edilir 
•	Şüpheli Acrobat API çağrıları ve beklenmeyen local file access girişimleri gözlemlenir 
•	PDF açıldıktan sonra oluşan HTTP/DNS trafiği Wireshark gibi araçlarla incelenir 
•	Sandbox bypass şüphesi oluşturacak sistem seviyesi process spawn davranışları kontrol edilir
Etkilenen Sistemler 
•	Adobe Acrobat Reader DC (Continuous Track) üzerinde güncel güvenlik yamaları uygulanmamış sürümler 
•	2025 yılı ve öncesinde yayımlanmış, Adobe security update almamış Acrobat Reader DC build’leri 
•	Windows, macOS ve Linux üzerinde çalışan Acrobat Reader kurulumları 
•	E-posta, web indirmesi veya dosya paylaşım platformları üzerinden PDF açan tüm uç kullanıcı sistemleri 
•	Kurumsal ortamda merkezi güncelleme yapılmamış endpoint cihazları 
•	Protected Mode (Sandbox) devre dışı bırakılmış veya kısıtlı yapılandırılmış sistemler 

Çözüm Önerileri
•	Adobe Acrobat Reader uygulaması en güncel güvenlik yamaları uygulanmış sürüme yükseltilmelidir 
•	Eski ve güvenlik açığı içeren Acrobat Reader sürümleri sistemlerden tamamen kaldırılmalıdır 
•	Kurumsal ortamlarda merkezi yazılım yönetimi (Intune, SCCM vb.) ile standart ve güncel sürüm dağıtımı yapılmalıdır 
•	Adobe Acrobat Reader için otomatik güncelleme mekanizması aktif hale getirilmelidir

Güvenlik Sertleştirme (Hardening) Önerileri
•	Adobe Acrobat Reader içerisinde JavaScript çalıştırma özelliği devre dışı bırakılmalıdır 
•	Protected Mode (Sandbox) özelliği etkin hale getirilmelidir 
•	Protected View ayarı “tüm PDF dosyaları için” aktif edilmelidir 
•	PDF dosyalarının varsayılan olarak kısıtlı modda açılması sağlanmalıdır 
•	Acrobat Reader uygulamasının outbound (dışa giden) ağ trafiği sınırlandırılmalıdır 
•	Kurumsal firewall üzerinden Acrobat süreçleri için gereksiz internet erişimi kısıtlanmalıdır 
•	Endpoint seviyesinde EDR çözümleri ile Acrobat davranışları izlenmelidir

