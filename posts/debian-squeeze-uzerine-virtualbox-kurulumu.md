<html><body><a href="http://img251.imageshack.us/img251/6217/virtualboxlogo.jpg"><img title="VirtualBox Kurulumu" src="http://img251.imageshack.us/img251/6217/virtualboxlogo.jpg" alt="" width="302" height="312"></a>

<strong>Debian Lenny</strong> kullanıcıları <strong>VirtualBox</strong> kurarken normal kurulum sırasında bir hata almazlarken,Unstable(sid) ve Squeeze(testing) kullanıcıları "kernel modul" hatası almaktadır.Aşağıda basit adımlarla Debian testing ve unstable sürümleri üzerine VirtualBox kurulumunu çok basit adımlarla anlatmaktadır.

1. İlk önce konsolumuzu açıp root oluyoruz ve ;
<pre>$ aptitude install virtualbox-ose
</pre>
2. Yukardaki komutu verdikten sonra ,virtualbox modullerimizi yukleyelim;
<pre>$ aptitude install virtualbox-ose-modules-$(uname -r)
</pre>
Eğer yukardaki komutta bulunamadı uyarısını alırsanız 3.adımdaki gibi yapıyoruz;

3.Modülleri yükleme;
<pre>$ aptitude install module-assistant
$ m-a a-i virtualbox-ose-source
</pre>
4.Son olarak;
<pre>$modprobe vboxdrv</pre>
Artık "VirtualBox" sistemimize kuruldu.VirtualBox'a <strong>Gnome Menu Paneli</strong>'nden <em>Uygulamalar&gt;&gt;Sistem Araçları&gt;&gt;VirtualBox OSE</em> sırasını izleyerek açabilirsiniz ya da uçbirimden
<pre>$virtualbox</pre>
yazarakda açabilirsiniz.Sorularınız için yorum bırakabilirsiniz.</body></html>