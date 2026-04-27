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





Local Area Network (LAN) Topolojileri – Notlar
Ağ dünyasında “topoloji” kavramı, bir ağın fiziksel veya mantıksal olarak nasıl tasarlandığını, yani cihazların birbirine nasıl bağlandığını ifade eder. Zaman içinde farklı ihtiyaçlara göre çeşitli topolojiler geliştirilmiş ve kullanılmıştır. Her topolojinin kendine özgü avantajları ve dezavantajları vardır; bu yüzden seçim yapılırken maliyet, ölçeklenebilirlik ve güvenilirlik gibi faktörler dikkate alınır.
Star (Yıldız) Topolojisi
Yıldız topolojisi günümüzde en yaygın kullanılan ağ yapılarından biridir. Bu yapıda tüm cihazlar (bilgisayarlar, yazıcılar vb.) merkezi bir cihaza bağlanır. Bu merkezi cihaz genellikle bir switch veya hub’dır. Ağdaki veri iletişimi doğrudan cihazlar arasında değil, bu merkezi cihaz üzerinden gerçekleşir. Yani bir cihazdan diğerine veri gönderildiğinde, veri önce merkezi cihaza gider, ardından hedef cihaza iletilir.
Bu topolojinin en önemli avantajlarından biri güvenilirliktir. Çünkü ağdaki bir cihazın veya kablonun arızalanması genellikle sadece o cihazı etkiler, tüm ağı çökertmez. Ayrıca oldukça ölçeklenebilir bir yapıya sahiptir; yani ağa yeni cihazlar eklemek oldukça kolaydır. Bu da özellikle büyüyen işletmeler için büyük bir avantaj sağlar.
Ancak yıldız topolojisinin bazı dezavantajları da vardır. Öncelikle, her cihazın merkezi cihaza ayrı ayrı bağlanması gerektiği için daha fazla kablo kullanılır ve bu da maliyeti artırır. Ayrıca switch veya hub gibi ek donanımların satın alınması gerekir. Ağ büyüdükçe bakım ihtiyacı da artar ve bu durum yönetimi zorlaştırabilir. Sorun giderme (troubleshooting) süreçleri de daha karmaşık hale gelebilir.
En kritik noktalardan biri ise merkezi cihaza olan bağımlılıktır. Eğer switch veya hub arızalanırsa, ağa bağlı tüm cihazlar iletişimini kaybeder. Yani ağın tamamı çalışamaz hale gelir. Her ne kadar bu cihazlar genellikle dayanıklı olsa da, bu durum yıldız topolojisinin tek noktadan hata (single point of failure) riski taşıdığını gösterir.

Bus (Veriyolu) Topolojisi 
Bus topolojisi, tüm cihazların tek bir ana kabloya (backbone) bağlandığı bir ağ yapısıdır. Bu yapı, bir ağacın dalına bağlı yapraklar gibi düşünülebilir; yani tüm cihazlar tek bir hat üzerinden iletişim kurar. Ağdaki veri, bu ortak kablo boyunca ilerler ve hedef cihaza ulaşır.
Bu topolojinin en önemli avantajlarından biri kurulumunun basit ve maliyetinin düşük olmasıdır. Ekstra ağ cihazlarına (örneğin switch gibi) ihtiyaç duyulmaması ve daha az kablolama gerektirmesi, özellikle küçük ve basit ağlar için ekonomik bir çözüm sunar.
Ancak bu yapının bazı önemli dezavantajları vardır. Tüm veri trafiğinin tek bir kablo üzerinden gitmesi, ağda yoğunluk oluşmasına neden olabilir. Özellikle birden fazla cihaz aynı anda veri göndermek istediğinde performans düşer ve darboğaz (bottleneck) oluşur. Ayrıca tüm veri aynı hat üzerinden geçtiği için bir sorun oluştuğunda hangi cihazdan kaynaklandığını tespit etmek oldukça zorlaşır.
Bus topolojisinin bir diğer kritik zayıflığı ise yedekliliğin (redundancy) olmamasıdır. Ana kablo (backbone) ağın tek iletişim yolu olduğu için bu kabloda meydana gelecek herhangi bir arıza tüm ağı etkiler. Kablo koparsa veya zarar görürse, ağa bağlı hiçbir cihaz veri gönderemez veya alamaz. Bu da bus topolojisini güvenilirlik açısından zayıf hale getirir.

Ring (Halka / Token) Topolojisi 
Ring topolojisinde cihazlar birbirine doğrudan bağlanarak kapalı bir döngü (loop) oluşturur. Yani her cihaz iki komşu cihaza bağlıdır ve ağ bir halka şeklinde çalışır. Bu yapı, yıldız topolojisine kıyasla daha az kablolama gerektirir ve merkezi bir cihaza olan bağımlılığı azaltır.
Bu topolojide veri, halka boyunca sırayla ilerleyerek hedef cihaza ulaşır. Verinin iletilmesi sırasında her cihaz, kendisine gelen veriyi bir sonraki cihaza aktarır. İlginç bir çalışma mantığı vardır: Eğer bir cihazın kendi göndereceği verisi yoksa, gelen veriyi iletir; ancak kendi verisi varsa önce onu gönderir, ardından diğer verileri iletmeye devam eder. Bu mekanizma genellikle “token” mantığı ile ilişkilendirilir.
Ring topolojisinin avantajlarından biri, veri akış yönünün tek olması sayesinde hata tespitinin nispeten kolay olmasıdır. Veri belirli bir yol izlediği için, bir sorun oluştuğunda hangi noktada problem olduğu daha rahat anlaşılabilir. Ayrıca aynı anda tüm cihazlar veri göndermediği için bus topolojisindeki gibi ciddi darboğaz problemleri daha az görülür.
Bununla birlikte bazı dezavantajları da vardır. Verinin hedefe ulaşabilmesi için bazen birçok cihazdan geçmesi gerekir, bu da verimliliği düşürebilir ve gecikmelere neden olabilir. En önemli sorunlardan biri ise ağın kırılgan yapısıdır: Eğer halkadaki bir kablo koparsa veya bir cihaz arızalanırsa, tüm ağ iletişimi durabilir. Yani tek bir arıza tüm sistemi etkileyebilir.

Switch Nedir?
Switch (anahtar), bir ağ içerisinde birden fazla cihazı birbirine bağlamak için kullanılan temel ağ cihazlarından biridir. Bilgisayarlar, yazıcılar ve diğer ağ destekli cihazlar ethernet kabloları aracılığıyla switch üzerindeki portlara bağlanır. Switch’ler genellikle 4, 8, 16, 24, 32 veya 64 port gibi farklı kapasitelere sahip olabilir ve bu sayede çok sayıda cihazın tek bir ağda toplanmasını sağlar.
Switch’lerin en önemli özelliklerinden biri, ağ trafiğini akıllı bir şekilde yönetmesidir. Bir switch, hangi cihazın hangi porta bağlı olduğunu bilir. Bu sayede bir veri paketi aldığında, bu paketi tüm portlara göndermek yerine sadece hedef cihaza iletir. Bu durum, ağı gereksiz veri trafiğinden kurtarır ve performansı önemli ölçüde artırır. Bu yönüyle switch’ler, daha basit çalışan hub veya repeater gibi cihazlara göre çok daha verimlidir.
Ayrıca switch’ler ve router’lar birbirine bağlanarak daha büyük ve dayanıklı ağ yapıları oluşturulabilir. Bu bağlantılar sayesinde ağda birden fazla veri yolu (path) oluşur. Eğer bu yollardan biri kesilirse, veri alternatif bir yol üzerinden iletilmeye devam eder. Bu durum ağın güvenilirliğini (redundancy) artırır. Her ne kadar veri bazen daha uzun bir yol izlemek zorunda kalabileceği için performansta küçük düşüşler yaşanabilse de, ağın tamamen kesilmemesi büyük bir avantaj sağlar.
Router Nedir?
outer (yönlendirici), farklı ağları birbirine bağlayan ve bu ağlar arasında veri iletimini sağlayan temel bir ağ cihazıdır. En basit haliyle, bir yerel ağı (örneğin ev veya ofis ağı) internet gibi başka bir ağa bağlar. Router’ın görevi, gelen veriyi doğru hedefe ulaştırmak için en uygun yolu belirlemek ve bu veri paketlerini ilgili ağa iletmektir.
Bu işlem “routing” (yönlendirme) olarak adlandırılır. Routing, verinin bir kaynaktan çıkıp hedefe ulaşana kadar geçtiği yolun belirlenmesi sürecidir. Router, ağlar arasında birden fazla yol (path) varsa, bu yollar arasından en uygun olanı seçerek verinin doğru ve verimli şekilde iletilmesini sağlar. Bu seçim; hız, mesafe veya ağ yoğunluğu gibi faktörlere bağlı olabilir.
Router’lar özellikle birden fazla ağın bulunduğu yapılarda büyük önem taşır. Örneğin bir ofis ağı ile internet arasında veri alışverişi router sayesinde gerçekleşir. Aynı şekilde büyük ağlarda birden fazla router kullanılarak alternatif yollar oluşturulabilir. Bu da ağın daha dayanıklı olmasını sağlar; çünkü bir yol kesildiğinde veri başka bir yol üzerinden iletilmeye devam eder.
Kısaca özetlemek gerekirse, switch’ler aynı ağ içindeki cihazları birbirine bağlarken, router’lar farklı ağları birbirine bağlar ve verinin bu ağlar arasında doğru şekilde ilerlemesini sağlar.
Subnetting (Alt Ağlara Bölme)
Subnetting, bir ağı daha küçük ve yönetilebilir parçalara (alt ağlara) bölme işlemidir. Temel amaç, büyük bir ağ yapısını daha düzenli hale getirmek ve farklı ihtiyaçlara göre bölümlendirmektir
Gerçek hayatta özellikle işletmelerde farklı departmanlar bulunur (örneğin muhasebe, finans, insan kaynakları). Ağlarda da benzer bir mantık vardır. Network yöneticileri subnetting kullanarak her departman için ayrı ağ bölümleri oluşturur ve böylece verinin doğru yere gitmesini sağlar.
Subnetting işlemi, IP adreslerinin ve subnet mask denilen bir yapının birlikte kullanılmasıyla gerçekleştirilir. IP adresi ve subnet mask, 32 bitlik (4 oktetli) bir yapıdadır ve her oktet 0 ile 255 arasında bir değer alır. Subnet mask, ağın hangi kısmının “network”, hangi kısmının “host” olduğunu belirlemeye yarar. Yani bir IP adresinin hangi ağa ait olduğunu ve o ağ içindeki hangi cihaza ait olduğunu ayırır.
Bir subnet içinde IP adresleri üç temel rol için kullanılır:
İlk olarak network address (ağ adresi), ağın başlangıcını temsil eder ve o ağın kimliğini belirler. Örneğin 192.168.1.100 IP adresine sahip bir cihaz, 192.168.1.0 ağı içinde yer alır. Buradaki 192.168.1.0 ifadesi tüm ağı temsil eden başlangıç adresidir.
İkinci olarak host address (host adresi), ağ içindeki bireysel cihazları tanımlamak için kullanılır. Aynı ağda bulunan her cihazın kendine özgü bir host adresi vardır. Örneğin 192.168.1.100 bu ağdaki belirli bir bilgisayarı ifade eder.
Üçüncü olarak default gateway (varsayılan ağ geçidi), farklı ağlara çıkış yapmak için kullanılan özel bir IP adresidir. Eğer bir cihaz aynı ağ dışında bir hedefe veri göndermek isterse, bu veri önce default gateway’e gönderilir. Genellikle router bu görevi üstlenir ve çoğunlukla .1 veya .254 gibi ilk ya da son kullanılabilir IP adreslerinden biri bu amaçla seçilir (örneğin 192.168.1.254).
Ev ağları gibi küçük yapılarda genellikle tek bir subnet bulunur çünkü aynı anda çok fazla cihaza ihtiyaç duyulmaz. Ancak işletmelerde yüzlerce hatta binlerce cihaz bulunduğu için subnetting zorunlu hale gelir. Bilgisayarlar, yazıcılar, kameralar ve sensörler farklı subnetlere ayrılarak hem yönetim kolaylaştırılır hem de ağ daha verimli çalışır.
Subnetting’in en önemli faydalarından biri güvenliktir. Subnetting sayesinde ağlar birbirinden tamamen ayrılır. Böylece farklı departmanlar birbirinin sistemine erişemez, ancak her ikisi de internet bağlantısını kullanabilir.
Özetle subnetting; ağları daha düzenli, daha güvenli ve daha verimli hale getirmek için kullanılan, IP adresleme mantığına dayalı bir bölümlendirme yöntemidir.
Basit senaryo
1.	PC → paketi default gateway’e gönderir 
2.	Router (gateway) paketi alır 
3.	Router NAT yapar (192.168.1.10 → public IP) 
4.	Paket internete çıkar

DHCP (Dynamic Host Configuration Protocol) 
IP adresleri bir cihaza iki şekilde atanabilir: manuel olarak (statik IP) ya da otomatik olarak DHCP sunucusu üzerinden. Manuel atamada ağ yöneticisi IP adresini elle girer. Ancak büyük ağlarda bu yöntem pratik olmadığı için genellikle DHCP kullanılır.
DHCP, ağa yeni bağlanan cihazlara otomatik olarak IP adresi ve gerekli ağ bilgilerini (subnet mask, default gateway gibi) dağıtan bir sistemdir. Böylece her cihazın ayrı ayrı manuel ayarlanmasına gerek kalmaz.
Bir cihaz ağa bağlandığında ve IP adresi yoksa, DHCP süreci otomatik olarak başlar. Bu süreç dört aşamadan oluşur ve genellikle “DORA” olarak hatırlanır:
İlk adım DHCP Discover aşamasıdır. Cihaz, ağda bir DHCP sunucusu olup olmadığını bulmak için bir yayın (broadcast) mesajı gönderir. Bu mesaj “Bana IP verebilecek bir DHCP var mı?” şeklinde düşünülebilir.
İkinci adım DHCP Offer aşamasıdır. Ağda bir DHCP sunucusu varsa, cihaza kullanılabilir bir IP adresi teklif eder. Bu teklif, aynı zamanda bazı ek ağ bilgilerini de içerebilir.
Üçüncü adım DHCP Request aşamasıdır. Cihaz, sunucunun teklif ettiği IP adresini kabul ettiğini belirtmek için bir yanıt gönderir. Bu aşamada cihaz artık o IP’yi kullanmak istediğini doğrular.
Son adım DHCP ACK (Acknowledgement) aşamasıdır. DHCP sunucusu bu talebi onaylar ve IP adresini resmi olarak cihaza tahsis eder. Bu andan itibaren cihaz artık ağda bu IP ile aktif olarak iletişim kurabilir.
Özetle DHCP, IP adresi yönetimini otomatikleştirerek ağ kurulumunu kolaylaştırır ve özellikle büyük ağlarda hataları ve yönetim yükünü ciddi şekilde azaltır.


Zafiyetin doğrulanması, sistem üzerinde doğrudan istismar gerçekleştirilmeden, güvenli yöntemler kullanılarak yapılmalıdır. Öncelikle Microsoft Active Directory rolüne sahip Domain Controller sistemler hedef olarak belirlenir.

Ardından Nessus kullanılarak credentialed scan gerçekleştirilir ve sistem üzerindeki güvenlik güncellemeleri analiz edilir. Tarama sonucunda, CVE-2026-33826 ile ilişkili güvenlik yamalarının eksik olup olmadığı kontrol edilir.

Elde edilen bulguların doğrulanması amacıyla sistem üzerinde yüklü güncellemeler manuel olarak incelenir ve ilgili KB paketlerinin varlığı kontrol edilir.

Ek olarak, zafiyetin Remote Procedure Call üzerinden çalıştığı göz önünde bulundurularak hedef sistemlerde RPC servislerinin erişilebilir olduğu doğrulanır.

Remediation (Çözüm Önerileri)

Bu zafiyetin giderilmesi için öncelikle Microsoft Active Directory sistemlerine Microsoft tarafından yayınlanan Nisan 2026 güvenlik güncellemeleri uygulanmalıdır. İlgili KB paketlerinin (örneğin Server 2022 ve Server 2025 için yayınlanan yamalar) tüm Domain Controller sistemlere eksiksiz şekilde yüklenmesi gerekmektedir.

Güncelleme sonrasında sistemlerin yeniden başlatılması ve yamaların başarıyla uygulandığının doğrulanması önerilir.

Ek olarak, Remote Procedure Call erişimi mümkün olduğunca sınırlandırılmalı ve yalnızca gerekli sistemler arasında izin verilmelidir. Gereksiz RPC erişimleri firewall kuralları ile engellenmelidir.

Ağ içerisinde Domain Controller sistemlere erişim sıkı şekilde kontrol edilmeli, yalnızca yetkili kullanıcıların ve sistemlerin erişimine izin verilmelidir. En az yetki prensibi uygulanarak kullanıcıların gereksiz haklara sahip olması engellenmelidir.

Son olarak, anormal RPC trafiği ve şüpheli aktivitelerin tespit edilebilmesi için loglama ve izleme mekanizmaları aktif hale getirilmeli ve düzenli olarak incelenmelidir.





