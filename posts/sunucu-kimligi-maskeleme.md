<html><body><p>Sunucu ve uygulamalar hakkında saldırganlara bilgi vermek güvenlik zaafiyeti yaratabilir.Saldırganlara bu kolaylığı vermemek için bilgileri saklamamız gerekir.Özellikle web sunucusu hakkında dışarıya bilgi vermek hem sunucu tarafında hemde uygulama tarafında zaafiyet yaratır.Dünyanın popüler ve özgür web sunucusu "<a href="http://www.apache.org/" target="_blank"><strong>Apache</strong></a>" de sunucu imzasını(<em>ServerSignature</em>) ve web server bilgilerini (<em>ServerTokens</em>) konfigurasyon dosyasında değerlerini değiştirerek gizleyebiliriz.

Apache'nin sunucumuzun işletim sistemini,kendisini ve kurulu olan modülleri göstermemesi için "<strong>/etc/httpd/conf/httpd.conf</strong>" dosyası içinde;

<strong>ServerSignature Off
ServerTokens Prod</strong>

değerlerini atayarak ayarlayabiliyoruz.Fakat sadece bunları yaparak sunucumuzun ne olduğunu saklayamıyoruz.Örnek olarak "<a href="http://news.netcraft.com/" target="_blank"><strong>netcraft</strong></a>" kolaylıkla web sunucumuzun "<em>Apache</em>" olduğunu   söylecektir.Eğer test etmek istiyorsanız <a href="http://news.netcraft.com/" target="_blank">netcraft.com</a> adresine girerek ya da kısaca " <em>http://toolbar.netcraft.com/site_report?url=site_adiniz.com</em> " şeklinde sorgulatarak öğrenebiliriz.

<strong>Netcraft'tan  :</strong>

<a href="http://i56.tinypic.com/8yc4s3.jpg"><img class="alignnone" title="Netcraft" src="http://i56.tinypic.com/8yc4s3.jpg" alt="" width="480" height="71"></a>

Yukarda görüldüğü gibi sunucu kimliğimizin "<em>Apache</em>" olduğu ortada.Başka bir şekilde " <a href="http://nmap.org/" target="_blank"><strong>nmap</strong></a> " ile tarayarak da test edelim.("<em>Nmap nedir?</em>" diyorsanız <a href="http://tr.wikipedia.org/wiki/Nmap" target="_blank">buradan</a> )Sisteminizde "<strong>nmap</strong>" mevcut değilse paket yöneticisi yardımı ile kurun.
</p><pre># yum install nmap</pre>
Eğer grafik arabirimi ile kullanmak istiyorsanız "<a href="http://nmap.org/zenmap/" target="_blank">zenmap</a>" i kurabilirsiniz."<strong>zenmap</strong>"i de kurmak için;
<pre># yum install zenmap</pre>
Sistemimize "nmap" kuruldu ise sunucunuzun ip  adresini ya da adını yazarak taratın.Eğer sunucuyu maskelememişsek nmap Apache'nin parmak izini(<em>fingerprint</em>) tanıyacaktır ve size 80. portta Apache sunucusunun çalıştığını söylecektir.

<strong>Zenmap'ten :</strong>

<a href="http://i51.tinypic.com/2d18cqh.png"><img class="alignnone" title="Zenmap" src="http://i51.tinypic.com/2d18cqh.png" alt="" width="396" height="67"></a>

Demek ki Apache'deki "<em>ServerSignature Off</em> " ve "<em>ServerTokens Prod</em>" değerleri sunucu bilgisini gizleyemiyor sadece kısıtlama yapabiliyor.Şimdi sunucu bilgilerimizi tamamen saklayalım.Bu maskeleme işlemini Apache'nin "<a href="http://www.modsecurity.org/" target="_blank">mod_security</a>" ile yapacağız.Eğer "<strong>mod_security</strong>" modülü yüklü değilse yükleyelim.CentOS üzerine bu modülü yüklemek için "<em>EPEL</em>" deposunu eklemiş olmanız gerekiyor.(" Epel deposu eklemek için <a href="http://linux.piesso.com/epel-ve-rpmforge-depolarini-ekleyin" target="_blank">yardım</a> ")Paket yöneticisi ile hemen yükleyelim;
<pre># yum install mod_security</pre>
Modülü kurduktan sonra ilk önce "mod_security" kuralları aktif edelim."<strong>modsecurity_crs_10_config.conf</strong>" dosyasına "SecRuleEngine On" satırını ekleyelim.
<pre># vi /etc/httpd/modsecurity.d/modsecurity_crs_10_config.conf</pre>
<pre>+  SecRuleEngine On
</pre>
Şu an "mod_security" modülümüz hazır.Artık Apache'nin kimliğini maskeleyelim.Bunun için biraz önce " <em>SecRuleEngine On</em> " satırını eklediğimiz "<strong>modsecurity_crs_10_config.conf</strong>" dosyasına "<strong>SecServerSignature</strong> " satırını eklemeliyiz."<strong>SecServerSignature </strong>" değeri için istediğiniz ismi girebilirsiniz,hatta farklı aldatmaca sunucu kimlikleri de kullanabilirsiniz.Örnek olarak :
<pre>+ SecServerSignature  " Ulak Web Server"</pre>
Yukardaki satırı ekledikten sonra Apache'deki "<strong>ServerTokens</strong>" değerini "<em>Major</em>" olarak değiştirin.
<pre># vi /etc/httpd/conf/httpd.conf</pre>
<pre>" ServerTokens Major "</pre>
Bu değişikliği de yaptıysanız "<strong>Apache</strong>"yi yeniden başlatalım.
<pre># service httpd restart</pre>
Web sunucumuzun kimliği dışarıya karşı maskelendi.Artık testler yaparak kontrol edebiliriz.</body></html>