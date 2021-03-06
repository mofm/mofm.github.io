<html><body><strong>DHCP Relay Agent Nedir?</strong>
DHCP Relay Agent,DHCP sunucu bulunmayan bir subnette DHCP ve BOOTP isteklerini,bir ya da daha fazla DHCP sunucu bulunan farklı bir subnete iletilmesine izin verir.

<strong>Enterasys DHCP Relay Agent</strong>

Enterasys switch ve backbone cihazlarında DHCP Relay Agent "ip helper-address" komutu ile ayarlanabilir.Örnek olarak DHCP sunucunun bulunduğu bir VLAN ile DHCP istemcinin bulunduğu VLAN arasında relay agent ayarlayalım;



<blockquote><em>Interface ge.1.1 ----&gt; VLAN 5 ----&gt; DHCP istemcinin bulunduğu VLAN ve interface
Interface ge.1.2 ----&gt; VLAN 10 ---&gt; DHCP sunucunun bulunduğu VLAN ve interface ----&gt; 10.80.20.34 ----&gt; DHCP Sunucu IP</em> </blockquote>



İlk olarak DHCP istemcinin bulunduğu VLAN için router CLI'e geçerek "ip helper-address" komutunu ve diğer ayarları girelim.

<code>-&gt; router
-&gt; enable
-&gt; configure
-&gt; interface vlan 5 
-&gt; no shutdown
-&gt; ip address 10.50.20.1 255.255.252.0
-&gt; ip helper-address 10.80.20.24
-&gt; ip rip send version 2
-&gt; ip rip receive version 2
-&gt; ip rip enable
-&gt; exit</code>

Buraya DHCP istemci VLAN'ınında gerekli ayarları yaptık.Şimdi DHCP sunucunun bulunduğu VLAN için gerekli ayarlamaları yapalım.CLI arabirimde kaldığımız yerden devam ediyorum;

<code>-&gt; interface vlan 10
-&gt; no shutdown 
-&gt; ip address 10.80.20.1 255.255.252.0
-&gt; ip rip send version 2
-&gt; ip rip receive version 2
-&gt; ip rip enable
-&gt; exit
-&gt; router rip
-&gt; exit</code>

Bu adımlardan sonra kenar uç cihazında gerekli vlan'ları oluşturup ve bu vlan'lara ait 'egress' ayarlarını yaparak test edebilirsiniz. </body></html>