<html><body><img class="alignright" title="CUPS" src="http://www.cups.org/doc-1.1/images/cups-large.gif" alt="" width="179" height="212">Yazıcınız "SAMBA" ile değilde,"CUPS" ile ağınızda paylaşmak istiyorsanız adımları takip edin:

<strong>1-</strong> "<em>/etc/cups/cups.conf</em>" dosyasını metin düzenleyici ile açın yada diğer bir yol ise ; tarayıcınıza " <em>http://localhost:631</em> " yazın ve CUPS web arayüzüne ulaşın.CUPS web arayüzünden "<em>Administrator</em>" sekmesini tıklayın ve oradan "<em>Edit Configuration File</em>" butonuna tıklayıp düzenleme yapacağımız sayfayı açın.

<strong>2-</strong>Ağınızdaki ip grublarına izin verin.
<blockquote><tt>
# Restrict access to the server...</tt>

<tt>Order allow,deny
<strong> Allow localhost
Allow from 192.168.1.*</strong>
</tt></blockquote>
<strong>3-</strong> Tarayıcı ile ulaşmalarına izin verin.
<blockquote><tt>
# Show shared printers on the local network.
Browsing On
BrowseOrder allow,deny
BrowseAllow all
<strong>BrowseAddress 192.168.1.*:631</strong></tt></blockquote>
<strong>4- </strong>Eğer uzaktaki bir bilgisayarın yazıcıyı yönetilmesine izin vermek istiyorsanız.(Örnek olarak "192.168.1.3" ip'li bilgisayara izin verdik):
<blockquote><tt>
# Restrict access to the admin pages...</tt>

<tt>Encryption Required
Order allow,deny
<strong>Allow localhost
Allow 192.168.1.3</strong></tt>

<tt></tt></blockquote>
<strong>5- </strong>Bu ayarları yaptıktan sonra "CUPS"u yeniden başlatalım.
<blockquote><tt># /etc/init.d/cupsd restart</tt></blockquote>
<strong>6-</strong>Uzaktaki bilgisayara yazıcıyı ayarlamak için "<em>/etc/cups/client.conf</em>" dosyasına "<em>Servername</em>" ile printer server adını yazın ya da Gnome masaüstü kullanıyorsanız ""<strong>Sistem&gt;&gt;Yönetim&gt;&gt;Yazdırma&gt;&gt;Ekle&gt;&gt;Ağ yazıcısı bul</strong>"" yolunu izleyerek çıkan ekranda printer server ip adresini yazarak ağdaki printerı otomatik olarak makinenize tanımlayabilirsiniz.</body></html>