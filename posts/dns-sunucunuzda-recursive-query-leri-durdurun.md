<html><body><img class="alignright" title="Bind Dns server" src="http://www.readynas.com/wp-content/uploads/2009/07/binddns-logo.jpg" alt="" width="110" height="110">DNS sunucunuz üzerinde "<strong>recursion</strong>"(<em>recursive query</em>) istekleri aktif ise dışardan sorgulamalara açık demektir.Bu da dns sunucunuzun dışarıdan boş yere meşgul olması demektir.DNS sunucunuzun bu istekleri açık olup olmadığını sorgulatın."<a href="http://intodns.com" target="_blank">intodns</a>" adlı site dns sunucunuz hakkında detaylı bir rapor veren güzel bir site.Bu siteye girip dns sunucunuzu sorgulatarak sağlığı hakkında bilgi alın.(Kısaca tarayıcınıza "http://intodns.com/domain-adiniz.com" şeklinde de sorgulatabilirsiniz.)

Sorgu raporu içindeki "<strong>Recursive Query</strong>" sekmesinde hata alıyorsanız sunucunuz dışardan sorgulara açık demektir.BIND DNS serverda "recursion"u kapatmak için named.conf adlı ayar dosyamıza "recursion on" satırını ekleyelim:

<code>#vi /var/named/chroot/etc/named.conf</code>

"<strong>Options</strong>" bölümü içine "<em>recursion no;</em>" satırını ekleyin ve ya kendiniz dışında herkese kapatmak için ise " allow-recursion { 127.0.0.1 ; } ; " satırını ekleyebilirsiniz ve yeniden başlatın.

<code># service named restart</code></body></html>