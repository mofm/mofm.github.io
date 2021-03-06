<html><body><p>Linux'de sizi hiçbiryere muhtaç bırakmayacak her türlü araç mevcuttur.Birim çevirme gibi genel geçer bir ihtiyaç olan çevirme işlemlerini konsoldan yapabilirsiniz.Çeviri işlemlerini "<strong>units</strong>" komutuyla yapıyoruz.Ama ilk önce sisteminizde "units" kurulu olması lazım.Eğer sisteminizde "<strong>units</strong>" kurulu değilse hemen bu aracı kuruyoruz.Her dağıtım kendi paketleme sistemi üzerinde bunu indirip hemen kurabilirler.Debian ve Ubuntu kullanıcıları "<strong>aptitude install units</strong>" demeleri yeterlidir.Paket kurulduktan sonra artık çeviri işlemlerine başlayabiliriz.<strong>Units</strong> komutuyla istediğiniz her birimi birbirine çevirebilir,hatta tanımını alabilirsiniz.

<strong>Örnekler:</strong>

Kilometre'den Mil'e
</p><pre>$ units -t '1km' 'mile'</pre>
<pre>0.62137119</pre>
Ayak'dan Kilometre'ye
<pre>$ units -t '1foot' 'km'</pre>
<pre>0.0003048</pre>
İstediğiniz her birimi yukardaki gibi birbirine çevirebiliriz.Şimdi de Google'ın isim kökeni olan "<strong>googol</strong>"un ne olduğunu soralım.
<pre>$ units -t '1 googol'</pre>
<pre>1e+100</pre>
Görüldüğü gibi "<strong>Googol</strong>"un  1'in yanına 100 sıfır gelmesiyle oluştuğunu söyledi.Units komutuyla ilgili ayrıntılı bilgiliyi man sayfasından ulaşabilirsiniz.Bunun içinden "<strong>$ man units</strong>" yazmanız yeterli.Kolay gelsin.

Googol hakkında ayrıntılı bilgi için <a href="http://tr.wikipedia.org/wiki/Googol">buradan</a> .</body></html>