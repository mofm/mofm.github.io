<html><body><img class="alignright" title="Gentoo" src="http://www.uz-freiburg.com/gentoo-logo.png" alt="" width="89" height="91">Birden fazla bilgisayarınızın olduğu evinizde,küçük işletmenizde dosyalarınızı,dizinlerinizi ya da disklerinizi paylaşmak isteyebilirsiniz.Herhangi bir linux dağıtımı ile bunu birkaç adımda ve  kısa sürede gerçekleştirebilirsiniz.Bu yazıda NFS server olarak Gentoo Linux dağıtımını,NFS Client olarak Ubuntu Linux dağıtımı olarak anlatacağım.

1- İlk olarak "NFS Server"ı Gentoo kurulu sistemimize kuralım.
<blockquote><tt># emerge -av nfs-utils</tt></blockquote>
2- "NFS Server" kuruldu.Şimdi paylaşacağımız dizinleri <em>/etc/exports</em> dosyasına yazalım.Siz kendiniz farklı dizinleri paylaşabilirsiniz.
<blockquote><tt>/home/kullanici/paylasilan_dizin 192.168.1.3(async,rw,no_subtree_check)</tt></blockquote>
Yukardaki örnekte "/home/kullanici/paylasilan_dizin" yolundaki "paylasilan_dizin" adlı klasörü "192.168.1.3" ip adresindeki bilgisayar ile paylaşıma açtık.Sizin paylaşacağınız dizin farklı yolda ve bu klasörü paylaşacağınız adres farklı olabilir.Mesela paylaşacağınız dizini ağdaki tüm bilgisayarlara açabilirsiniz.Bunun içinse örnek olarak "192.168.*.*" şeklinde ya da ip adresi yerine " * " kullanabilirsiniz.
Dikkat edilecek bir nokta ise yukardaki paylaştığımız dizine ağdaki diğer bilgisayar için yazma ve okuma yetkisi verdik.Eğer sadece okuma yetkisi vermek isterseniz aşağıdaki gibi yapabilirsiniz.
<blockquote><tt>/home/kullanici/paylasilan_dizin 192.168.1.3(ro,async)</tt></blockquote>
<em>/etc/exports</em> dosyasına yukardaki istediğiniz ayarlardan birini yazarak,kaydedip çıkabilirsiniz.

3- NFS Serverı başlatın ve sistem başlangıçına ekleyin.Aşağıdaki adımlarda dağıtıma göre değişebilir.
<blockquote><tt># /etc/init.d/nfs start </tt></blockquote>
<blockquote><tt>#rc-update add nfs default </tt></blockquote>
4- Şimdi Ubuntu sistemimize NFS Client kuralım ve paylaşılan dizini sistemimize ekleyelim.
<blockquote><tt># apt-get install portmap nfs-common</tt></blockquote>
NFS Client kurulumu bittikten sonra <em>/etc/fstab</em> dosyasına ağdaki paylaşılan dizini ekleyelim.Aşağıdaki örnek sizin paylaşacağınız dizine ve NFS Server'ın ip adresine göre değişiklik gösterebilir.
<blockquote><tt>192.168.1.2:/home/kullanici/paylasilan_dizin      /home/ubuntu_kullanicisi/paylasilan_dizin       nfs     defaults 0 0</tt></blockquote>
Bu adımlardan sonra 192.168.1.2 adresinde bulunan NFS Server "/home/kullanici/paylasilan_dizin" yolundaki dizini 192.168.1.3 adresinde bulunan NFS Client istemcisi tarafından "/home/ubuntu_kullanici/paylasilan_dizin" yoluna her açılışta otomatik bağlayacaktır.</body></html>