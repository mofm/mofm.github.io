<html><body><p>Sunucu kaynaklarınız az ve mail sunucunuz mevcut değilse,herhangi bir external mail sunucusunu kullanmak zorunda kalabilirsiniz.Birçok küçük ve orta ölçekli kurumların ya da sitelerin <a href="http://www.google.com/a/?hl=tr" target="_blank">Google Apps</a> hizmetlerinden faydalandığını düşünürsek ,sunucunuzdan sadece mail göndermek için Google'ın ücretsiz sunduğu mail hizmetinden faydalanabiliriz.

Sunucunuz ya da bilgisayarınız üzerinden mailleri dışardaki mail sunucusuna yönlendirmek için "ssmtp"i kullanabiliriz.CentOS üzerine "ssmtp" i kurmak için olmazsa olmaz ek depolardan "<a href="http://fedoraproject.org/wiki/EPEL" target="_blank">EPEL</a>"in eklenmiş olması lazım."EPEL"i eklemek için <a href="http://linux.piesso.com/epel-ve-rpmforge-depolarini-ekleyin" target="_blank">bu yazıyı</a> takip edebilirsiniz.

İlk olarak "<em>ssmtp</em>"i kuralım :
</p><pre><strong># yum install ssmtp </strong></pre>
"ssmtp" i kurduktan sonra "<em>ssmtp.conf</em>" dosyasına <strong>Google Apps Email</strong> hesap bilgilerimizi ve <strong>smtp</strong> ayarlarımızı ekleyelim :
<pre><strong># vi /etc/ssmtp/ssmtp.conf</strong>
</pre>
<pre>root=kullanici_adi@domain_adi.com</pre>
<pre>mailhub=smtp.gmail.com:587</pre>
<pre>AuthUser=kullanici_adi@domain_adi.com
AuthPass=parola
UseSTARTTLS=YES
</pre>
Bilgileri ekledikten sonra test maili gönderelim.
<pre><strong>$ echo test | mail -s "test" kullanici_adi@domain_adi.com</strong></pre>
<strong>Diğer Başka Kaynaklar :</strong>

<a href="https://wiki.archlinux.org/index.php/SSMTP" target="_blank">Arch Linux için Ssmtp</a>

<a href="http://wiki.debian.org/sSMTP" target="_blank">Debian için Ssmtp</a>

<a href="http://www.freebsd.org/doc/handbook/outgoing-only.html" target="_blank">FreeBSD için Ssmtp</a>

<a href="http://forums.gentoo.org/viewtopic-t-420358-start-0.html" target="_blank">Gentoo için Ssmtp</a></body></html>