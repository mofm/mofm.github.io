<html><body><p><img title="Sane Logo" src="http://img683.imageshack.us/img683/6276/sanelogo.jpg" alt="" width="192" height="225"></p>
<p>Bu yazıda Arch Linux üzerinde scannerı nasıl tanıtacağımızı ve sane yükleyeceğiz ona kısa bir biçimde anlatacaz.Yapmanız gereken sadece yönergeleri sırasıyla izlemek:</p>
<p>1. Eğer scannerınız "sane" tarafından desteklenip desteklenmediğini öğrenmek için <a href="http://www.sane-project.org/sane-supported-devices.html">burayı tıklayın</a> .Eğer destekleniyorsa diğer adımlara devam edebilirsiniz.</p>
<p>2."Extra" depolarından "sane" i pacman ile yüklüyoruz;</p>
<p>$ <strong>pacman -S sane</strong></p>
<p>3."Sane" bilgisayarımıza kurulduktan sonra scanner grubuna kullanıcı adımızı ekleyelim;</p>
<p>$ <strong>gpasswd -a kullanıcı_adınız scanner</strong></p>
<p>4. Şimdi resmimizi taramayı deneyelim;</p>
<p>$ <strong>scanimage -L</strong></p>
<p>Eğer <strong>HP marka</strong> bir multiyazıcı ya da scanner kullanıyorsanız aşağıdaki adımlarla devam edin:</p>
<p>5.Pacman ile "HPLIP" i kuruyoruz;</p>
<p>$ <strong>pacman -S hplip</strong></p>
<p>6. "hplip" kurulduktan sonra aşağıdaki komutu veriyoruz;</p>
<p>$ <strong>echo "hpaio" &gt;&gt; /etc/sane.d/dll.conf</strong></p>
<p>7.  " <strong>$ hp-setup -i</strong>" komutu ile  aygıtımızı otomatik tanıtıp ekleyelim.</p>
<p>8. "$ <strong>hp-plugin</strong> " komutu ile eklentileri yükleyelim.</p>
<p>9. Son olarak tarayıcımız üzerimize bir şey koyup sağlam çalışıp çalışmadığını test edelim;</p>
<p>$ <strong>hp-scan</strong></p>
<p>İsterseniz Xsane de kurulabilirsiniz;</p>
<p>$<strong> <a href="http://www.nvidia.com/content/DriverDownload-March2009/confirmation.php?url=/XFree86/Linux-x86_64/173.14.25/NVIDIA-Linux-x86_64-173.14.25-pkg2.run&amp;lang=us&amp;type=Other">pacman -S xsane</a><br>
</strong></p>
</body></html>