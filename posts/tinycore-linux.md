<html><body><a href="http://upload.wikimedia.org/wikipedia/sl/0/02/Tcl_logo.png"><img title="Tinycore Linux" src="http://upload.wikimedia.org/wikipedia/sl/0/02/Tcl_logo.png" alt=""></a>

<strong>TinyCore Linux</strong> belkide dünyanın en küçük "grafik arabirimi" olan 10 mb'lık Linux dağıtımıdır.6 mb büyüklüğünde Linux 2.6 kerneli birlikte gelen bu dağıtım içeriğinde BusyBox,Tiny X,Fltk birlikte gelmektedir.TinyCore'un açılış süresi 4 sn gibi kısa bir sürede gerçekleşmedir.

Bilgisayar donanımı yetersiz ve düşük olanlar için ilaç gibi GUI ile birlikte gelen linux dağıtımı.Tam donanım desteği olmamasına rağmen bir çok donanımda hiç bir sorun olan olmadan kullanılabilir.TinyCore sadece bu kadar da değil,debian'dan bildiğimiz synaptic gibi ihtiyacınız olan yazılımı bir tıkla gerekli bağımlılıkları ile birlikte otomatik yükleyebilir ve sisteminizi güncelleştirebilirsiniz.Son sürümü 2.8.1 ve canlı cd ya da usb belleğinize yüklenebileceği gibi harddiskinize de normal bir linux dağıtımı gibi yüklenebilir.

TinyCore Linux hakkında daha fazla bilgi almak için <a href="http://tinycorelinux.com/">buradan</a> .

2.8.1 Son sürümünü indirmek için <a href="http://distro.ibiblio.org/pub/linux/distributions/tinycorelinux/2.x/release/tinycore_2.8.1.iso">buradan</a> .
<h4>TinyCore Linux'un hardiske yüklenmesi :</h4>
TinyCore Linux'u boot ettikten sonra "AppBrowser" ile gerekli iki paketi kurmamız gerekli:

1. <strong>cfdisk.tcz</strong>

2.<strong>grub-0.97-splash.tcz</strong>

bu kurulumlar tamamlandıktan sonra "root shell"i açıp aşağıdaki sıra ile komutları izliyoruz.
<ul>
	<li>fdisk -l  #harddisk bölümlerini görelim.</li>
	<li>cfdisk /dev/hda  #harddiskimizde yükleyeceğimiz disk bölümlerini oluşturalım.</li>
	<li>Yukardaki komutu verdikten açılan ekranda gösterilen bölümü "Enter"layıp sırayla  şu seçenekleri seçiyoruz."NEW&gt;Primary&gt;bölümün büyüklüğünü 100mb yapmanız yeterli&gt;Begining&gt;Bootable&gt;Write&gt;Quit .</li>
	<li>Buraya kadar tamamsa yeni harddisk bölümümüz hazırdır ve bu bölümü ext2 ile biçimlendirelim.Not:Tiny ext3'ü desteklemiyor.Şekillendirmek için " $ mkfs.ext3 /dev/hda1" ve ardından "$rebuildfstab"</li>
	<li>Bu adımda yeni bölümümüzü bağlayıp sistem dosyalarımızı koplayalım:" $mount /mnt/hda1" , "$mkdir -p /mnt/hda1/boot/grub","$mount /mnt/hdc" ,"$cp -p /mnt/hdc/boot/* /mnt/hda1/boot/","$mkdir -p /mnt/hda1/tce","$touch /mnt/hda1/tce/mydata.tgz"</li>
	<li>Buraya kadar hiç sorun olmamışsa artık Grub ayarlarını da tamamlayıp kurulumu tamamlayabiliriz.Grub ayarları içinde sırayla "$cp -p /usr/lib/grub/i386-pc/* /mnt/hda1/boot/grub/", "$vi /mnt/hda1/boot/grub/menu.lst" bu komutla grub menüsüne aşağıdaki gibi ekliyoruz;</li>
</ul>
<strong>default 0
timeout 10
title tinycore
kernel /boot/bzImage quiet
initrd /boot/tinycore.gz</strong>
<ul>
	<li>Ve son olarak  da "$grub " komutu verip grup konsolun giriyoruz ve yine sırayla:</li>
	<li><strong>root (hd0,0)
setup (hd0)
quit
</strong>yazarak kurulumu tamamlıyoruz.</li>
</ul>
Çok iyi anlatamadığımın farkındayım fakat sorularınız için yorum bırakmayı unutmayın!</body></html>