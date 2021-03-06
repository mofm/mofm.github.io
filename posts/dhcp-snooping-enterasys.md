<html><body><strong>DHCP</strong> ( <em><strong>D</strong>ynamic <strong>H</strong>ost <strong>C</strong>onfiguration <strong>P</strong>rotocol</em>) : basit olarak sistemdeki bilgisayarlara IP adreslerini ve buna ek olarak değişik parametreleri atamak için kullanılan servistir.DHCP’nin temel özelliği sistemi kuran kişilerin tek tek tüm makineleri gezip aynı veya benzer parametreleri defalarca eliyle girmesini engellemek,böylece zaman kazanmak ve sistem yöneticisinin işini kolaylaştırmaktır.<em>(*)</em>

<strong>DHCP Snooping</strong> : Ağda sahte  DHCP sunucusu kuran ve çalıştıran bir kişi, aynı ağda DHCP isteğinde bulunan istemci cihazlara varsayılan ağ geçidi adresi kendisine ait olan bir DHCP cevabı dönebilir. İstemci bu cevabı aldığı andan itibaren ağ geçidi adresi olarak bu sahte adresi kullanmaya başlar ve yerel ağın dışında bir adresi hedefleyen paketleri ilk olarak atak yapan kişinin makinesine yönlenir. Atakçı bu paketleri gitmeleri gereken doğru adreslere kendi üzerinden gönderirken tüm paketleri izleme olanağına sahip olur. Bu, istemci güvenliğini ve gizliliğini açıkça tehdit eden bir durumdur.  Man-in the-middle ataklarının bir türü olan DHCP Snooping atakları tam olarak bu şekilde gerçekleşir.<em>(**)</em>

 

Enterasys kenar switchler ve router'lar üzerinde "<strong>DHCP Snooping</strong>" ataklarını engellemek için aşağıdaki gibi adım adım konfigurasyon yapabiliriz.

1- İlk olarak kenar switch ve router üzerindeki <em>uplink</em> ve gerçek <em>DHCP sunucusu</em>nun portlarını <strong>"trust"</strong> olarak işaretlememiz lazım.Örnek olarak 48 portlu bir switch(Enterasys C2/B2) üzerinde 48.port uplink,47.port gerçek DHCP sunucumuzun bağlı olduğunu farzedelim.
<pre># set dhcpsnooping trust port fe.1.47-48 enable</pre>
Yukardaki komutta 47 ve 48.portları trust olarak işaretledik.(Gigabit portlar için fe.1.47-48 yerine ge.1.47-48 yazmalısınız.)

2-Trust portları işaretledikten sonra dhcpsnooping'i global olarak devreye alalım.
<pre># set dhcpsnooping enable</pre>
3- Eğer global olarak devreye almayıp,sadece belli ya da belirli vlan'lara açmak istiyorsanız aşağıdaki yapabilirsiniz.
<pre># set dhcpsnooping vlan 1 enable</pre>
Yukardaki komutta sadece "vlan 1" için aktif ettik.
<pre># set dhcpsnooping vlan 1-10 enable</pre>
Bu komutta da vlan 1 ile 10 arası devreye aldık.

4- Şimdi de untrust portlar için(default olarak tüm portlar zaten untrust'tır.Trust portları dhcpsnooping'i devreye almadan önce işaretlemiştik.) limit koyalım.
<pre># set dhcpsnooping limit fe.1.1-46 none</pre>
Bu komutla untrust tüm portlara rate limiti "none" yaparak DHCP paketlerinin rahatça geçebilmesini sağladık.Fakat istersek bu limiti "none" değil de "0-50" arasındaki bir değerle sınırlandırabilirdik.

# set dhcpsnooping limit fe.1.1-46 rate 50

Yukardaki gibi limiti " 50" yapabiliriz.Limiti "none" yapmanın avantajı eğer bir portun ucuna hub eklenmiş ve birden fazla host bulunuyorsa bunlar rahatça IP alabilecektir.Fakat "rate" limiti kısıtlı tutarsak hub kullanan host'lardan bazıları IP alamayabilirler.

5- Son olarak dhcpsnooping 'i devreye aldıktan sonra router veya switch üzerinde veritabanında IP ve MAC bilgileri yazılır.Bu bilgileri kontrol edelim:

# show dhcpsnooping binding

Total number of bindings:  4


MAC Address       IP Address     VLAN   Interface    Type    Lease (min)
-----------------  ---------------  ----  -----------  -------  -----------
00:01:6C:*:*:*     10.1.70.165     1      fe.1.12  DYNAMIC           41
00:11:85:*:*:*     10.1.70.220     1      fe.1.12  DYNAMIC           45
00:11:85:*:*:*     10.1.70.166     1      fe.1.12  DYNAMIC           51
00:1C:25:*:*:*     10.1.70.131     1      fe.1.23  DYNAMIC           48

Yukardaki çıktıda portlar üzerindeki IP ve MAC adresi bilgileri,hangi portlarda olduğunu,vlan'larını,DHCP lease sürelerini görebilirsiniz.

 

* <a href="http://tr.wikipedia.org/wiki/DHCP" target="_blank">http://tr.wikipedia.org/wiki/DHCP</a>

** <a href="http://www.agciyiz.net/index.php/guvenlik/dhcp-snooping-ataklari/" target="_blank">http://www.agciyiz.net/index.php/guvenlik/dhcp-snooping-ataklari/</a></body></html>