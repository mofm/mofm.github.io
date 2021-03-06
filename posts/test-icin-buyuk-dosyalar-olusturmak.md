<html><body><p>Sisteminiz üzerinde ya da networkte test yapmak için büyük dosyalar oluşturmak isteyebilirsiniz.İhtiyacımız olan bu dosyaları yeterli disk alanımız olup olmadığını kontrol ettikten sonra "dd" komutu ile oluşturabiliriz.Dosyaları oluşturmaya geçmeden önce "<em>dd</em>" komutunun man sayfasına ya da <a href="http://linux.die.net/man/1/dd" target="_blank">online man sayfalarına</a> göz atabilirsiniz.

Küçükten büyüğe doğru dosyalar oluşturmaya başlayabiliriz:

<strong>1 MB ' lık test dosyası :</strong>
</p><pre>$ <code>dd if=/dev/zero of=1MB.img bs=1024 count=0 seek=1024</code></pre>
 

<strong>10 MB'lık test dosyası :</strong>
<pre>$ <code>dd if=/dev/zero of=10MB.img bs=1024 count=0 seek=$[1024*10]</code></pre>
 

<strong>100 MB'lık test dosyası :</strong>
<pre>$ <code>dd if=/dev/zero of=100MB.img bs=1024 count=0 seek=$[1024*100]</code></pre>
 

<strong>1 GB'lık test dosyası :</strong>

<strong>
</strong>
<pre>$ <code>dd if=/dev/zero of=1GB.img bs=1024 count=0 seek=$[1024*100*10]</code></pre>
Şimdi oluşturduğumuz dosyaları ve boyutlarını kontrol edelim:

 
<pre>$ ls -lh</pre>
<pre>-rw-r--r--  1 piesso   piesso    100M Kas 17 10:18 100MB.img
-rw-r--r--  1 piesso   piesso     10M Kas 17 10:17 10MB.img
-rw-r--r--  1 piesso   piesso   1000M Kas 17 10:19 1GB.img
-rw-r--r--  1 piesso   piesso    1,0M Kas 17 10:17 1MB.img</pre>
 

<strong>10 GB'lık test dosyası :</strong>
<pre>$ <code>dd if=/dev/zero of=10GB.img bs=1024 count=0 seek=$[1024*1000*10]</code></pre>
 

Son olarak 10 GB boyutunda test dosyası da oluşturduktan sonra bir noktaya değinelim.Aşağıdaki iki komutun çıktısını dikkatlice inceleyelim.

Örnek olarak en son oluşturduğumuz 10GB'lık "<em>10GB.img</em>" dosyasının büyüklüğüne "<em>ls -lh</em>" komutu ile bakalım.

 
<pre>$ ls -lh</pre>
<pre>-rw-r--r--  1 piesso   piesso    9,8G Kas 17 10:28 10GB.img</pre>
 

Yukarıda görüldüğü gibi "<em>10GB.img</em>" adlı dosyasının boyutu <em>9.8 GB</em> büyüklüğünde.Bu dosyanın büyüklüğüne birde "<em>du -h</em>" komutu ile bakalım:

 
<pre>$ du -h 10GB.img</pre>
<pre>0    10GB.img</pre>
 

Yukardaki çıktıda bu dosyayının hiçbir büyüklüğünün olmadığını görüyorsunuz.Buradaki ince nokta "<em>ls -lh</em>" komutu dosyanın boyutunu ekrana yazdırırken , "du -h" komutu bu dosyanın diskimizde ne kadar yer kapladığını göstermektedir.Oluşturduğumuz "<em>image dosyaları</em>"na hiçbir data yazmadığımız için diskimizde yer kaplamaktadır.Bunu daha iyi anlamak için aşağıdaki komutla diskimizde ne kadar block kapladığına bakalım.
<pre>$ stat 10GB.img</pre>
<pre>
</pre>
<pre>File: `10GB.img'
 Size: 10485760000    Blocks: 0          IO Block: 4096   normal dosya
Device: 801h/2049d    Inode: 9281712     Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/piesso)   Gid: ( 1000/piesso)
Access: 2011-11-17 10:28:09.000000000 +0200
Modify: 2011-11-17 10:28:09.000000000 +0200
Change: 2011-11-17 10:28:09.000000000 +0200</pre>
 

Yukardaki çıktıdan da anlaşılacağı gibi bu dosya diskimizde "0" bloğa sahip.Birde diskimiz yer kaplayan test dosyası oluşturalım ve bunu daha iyi anlayalım.

<strong>500 MB'lık test dosyası :</strong>
<pre>$ dd if=/dev/zero of=test.img bs=1MB count=500</pre>
<pre>500+0 records in
500+0 records out
500000000 bytes (500 MB) copied, 2,20355 s, 227 MB/s</pre>
Şimdi oluşturduğumuz "test.img" adlı dosyanın boyutunu ve diskte kapladığı yeri inceleyelim.

 
<pre>$ ls -lh</pre>
<pre>-rw-r--r--  1 piesso   piesso    477M Kas 17 10:40 test.img</pre>
<pre>
</pre>
<pre>$ du -h test.img</pre>
<pre>478M    test.img</pre>
<pre>
</pre>
Yukardaki çıktıdan anlaşılacağı gibi bu dosya diskimizde "478 MB" lık yer kaplamaktadır.Daha detaylı bir çıktı alalım.

 
<pre>$ stat test.img</pre>
<pre>File: `test.img'
 Size: 500000000     Blocks: 977536     IO Block: 4096   normal dosya
Device: 801h/2049d    Inode: 9281713     Links: 1
Access: (0644/-rw-r--r--)  Uid: ( 1000/piesso)   Gid: ( 1000/piesso)
Access: 2011-11-17 10:40:17.000000000 +0200
Modify: 2011-11-17 10:40:19.000000000 +0200
Change: 2011-11-17 10:40:19.000000000 +0200</pre>
Oluşturduğumuz bu dosya diskte "977536" block kaplıyor.Bu şekilde aradaki farkı görebiliriz.</body></html>