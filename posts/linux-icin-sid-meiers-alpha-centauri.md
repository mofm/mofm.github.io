<html><body><p style="text-align: center;"><img class="aligncenter" src="http://www.brainygamer.com/.a/6a00e3982444028833011570a308ba970b-800wi" alt="Sid Meier's Alpha Centauri" width="245" height="300"></p>
<p style="text-align: left;">1999 yılında piyasaya çıkan güzel bir strateji oyunu(Ayrıntılı bilgi için <a href="http://tr.wikipedia.org/wiki/Sid_Meier%27s_Alpha_Centauri">buradan</a>).Oynayanlar,bilenler hastalık derecesinde bir oyun olduğunu çok iyi bilirler.Eğer sizde Linux kurulu masaüstünüzde bu oyunu oynamak istiyorsanız;
<strong>1.</strong> İlk olarak <a href="http://thepiratebay.org/torrent/4221412/Sid_Meier__s_Alpha_Centauri_for_Linux" target="_blank">bu adresten </a>torrent dosyasını indirin.(Dosya büyüklüğü=630 MB)
<strong>2.</strong>Bir "Torrent programı" ile (önerim Transmission) bilgisayarınıza 'iso' dosyasını indirin.
<strong>3.</strong>İndirdiğiniz "iso" dosyasını sistemimize bağlayalım.Bunun içinde şu adımları uygulayın;</p>
<p style="text-align: left;">*$ <em>cd /mnt</em></p>
<p style="text-align: left;">*$ <em>sudo mkdir iso</em></p>
<p style="text-align: left;">*$ <em>sudo mount -o loop -t iso9660 Alpha_Centauri.iso /mnt/iso/</em></p>
<p style="text-align: left;"><em> </em>
<strong>4.</strong>Böylece indirdiğimiz iso dosyasını "/mnt/iso" dizinine bağlamış olduk.Artık oyunu kurabiliriz.Yapmanız gereken tek şey ise;</p>
<p style="text-align: left;">*$cd /mnt/iso</p>
<p style="text-align: left;">*$<em>sudo sh setup.sh</em>
komutunu verip oyunu sisteminize yüklemek.Kurulum bitince;</p>
<p style="text-align: left;">*$ <em>smack</em> komutu vererek oyuna başlayabilirsiniz.</p>
<p style="text-align: left;">NOT: Eğer sisteminiz "x86_64" ise yapmanız gereken :</p>
<p style="text-align: left;">"setup.sh" dosyasındaki aşağıdaki kısımı değiştirmektir.</p>
<p style="text-align: left;"><strong>Önceki:</strong></p>
<p style="text-align: left;">DetectARCH()
{
status=1
case `uname -m` in
i?86) echo "x86"
status=0;;
*) echo "`uname -m`"
status=0;;
esac
return $status
}</p>
<p style="text-align: left;"></p>
<p style="text-align: left;"><strong>Yeni:</strong></p>
<p style="text-align: left;">DetectARCH()
{
status=1
case `uname -m` in
i?86) echo "x86"
status=0;;
*) echo "x86"
status=0;;
esac
return $status
}</p></body></html>