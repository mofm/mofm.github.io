<html><body><strong>Ethernet Arayüzü: eth0</strong>

<strong>Örnek IPv4 bilgileri:</strong>
IP adresi: 17x.3x.3x.50
Netmask: 255.255.255.0
Gateway: 17x.3x.3x.1
Broadcast : 17x.3x.3x.255

<strong>Örnek IPv6 bilgileri:</strong>
IP adresi: 2a00:xx80:3x::f50
Netmask: ffff:ffff:ffff::
Gateway: 2a00:xx80:3x::1

Gentoo Linux üzerinde hem IPv4 ve Yalın <a href="http://tr.wikipedia.org/wiki/IPv6" title="IPv6" target="_blank">IPv6</a> tanımlaması yapalım.Tanımlamaları yapmadan önce sisteminizde "sys-apps/iproute2" paketi yoksa kuralım(<em>ethernet arayüzümüz ile ilgili işlemleri yapmak için iki tane işleyici mevcut: "ifconfig" ve "iproute2"."ifconfig" öntanımlı olarak "sys-apps/net-tools" paketi birlikte gelir.Fakat "iproute2" ifconfig'den daha güçlü ve esnek bir işleyicidir.Öntanımlı olarak gelmez.Bunu kullanmanız tavsiye edilir.</em>)  :



<blockquote># emerge sys-apps/iproute2</blockquote>



 Kurulum tamamlandıktan sonra "/etc/conf.d/net" dosyasına network bilgilerimizi girelim:



<blockquote># vi /etc/conf.d/net</blockquote>



Aşağıdaki gibi bilgileri girelim;

<code>modules="iproute2"
config_eth0="17x.3x.3x.50/24 2a00:xx80:3x::f50/64"
routes_eth0="default gw 17x.3x.3x.1
default via 2a00:xx80:3x::1 dev eth0"</code>

NOT: Yukardaki gibi "routes_eth0=" satırında ilk gateway birinci satıra,ikinci gateway ikinci satırda olması gerekmektedir.

Network bilgilerini yukardaki gibi girdikten sonra "net.eth0" scriptini yeniden başlatalım.



<blockquote># /etc/init.d/net.eth0 restart
</blockquote>



</body></html>