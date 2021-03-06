<html><body><p>TTNet tarafından dağıtılan "Pikatel Combomax" marka ADSL modemini evdeki bağlantım için kullanıyorum ve bu gece biraz kurcalamaya karar verdim.Bu adsl modem Broadcom "BCM6338" chipseti kullanıyor.Daha fazla uzatmadan modemi kurcalayalım :)

İlk olarak modeme "telnet" ile bağlanalım.Öntanımlı "192.168.1.1" modem adresini değiştirmedim.Sizde aynı ya da daha farklı da olabilir.

</p><blockquote><tt> 
$ <strong>telnet 192.168.1.1</strong>
Trying 192.168.1.1...
Connected to 192.168.1.1.
Escape character is '^]'.
BCM96338 ADSL Router
Login: linuxman
Password: *******
&gt; 
</tt></blockquote>
Şu an modeme bağlandık ve birkaç komut denemesi yapalım.

<blockquote><tt>
&gt; ls
ls: not found
&gt; cd
cd: not found
&gt; mkdir
mkdir: not found
&gt; dir
dir: not found
</tt></blockquote>

Gördüğünüz gibi bu komutlar bulunamıyor ve şimdilik birşey göremiyoruz.Şimdi şu komutu deneyelim :

<blockquote><tt>
&gt; <strong>echo *</strong>
bin dev etc lib linuxrc mnt proc sbin usr var webs
</tt></blockquote>
Artık dizini listeleyebiliyoruz :)Modemimizi biraz daha karıştıralım ve modemin "CPU" hakkında bilgi edinelim.
<blockquote><tt>
&gt; <strong>cat proc/cpuinfo</strong>

system type             : 96338L-2M-8M
processor               : 0
cpu model               : BCM6338 V1.0
BogoMIPS                : 239.20
wait instruction        : no
microsecond timers      : yes
tlb_entries             : 32
extra interrupt vector  : yes
hardware watchpoint     : no
VCED exceptions         : not available
VCEI exceptions         : not available
</tt></blockquote>

Şimdi "RAM"i hakkında bilgi edinelim.
<blockquote><tt>
&gt; <strong>cat proc/meminfo</strong>

MemTotal:         6100 kB
MemFree:           432 kB
Buffers:           132 kB
Cached:            960 kB
SwapCached:          0 kB
Active:           1684 kB
Inactive:          328 kB
HighTotal:           0 kB
HighFree:            0 kB
LowTotal:         6100 kB
LowFree:           432 kB
SwapTotal:           0 kB
SwapFree:            0 kB
Dirty:               0 kB
Writeback:           0 kB
Mapped:           1424 kB
Slab:             2220 kB
Committed_AS:     3572 kB
PageTables:        244 kB
VmallocTotal:  1048560 kB
VmallocUsed:      1092 kB
VmallocChunk:  1047428 kB
</tt></blockquote>

Linux kernel versiyonunu öğrenelim.

<blockquote><tt>
&gt; <strong>cat proc/version</strong>

Linux version 2.6.8.1 (root@localhost.localdomain) (gcc version 3.4.2) #1 Mon Apr 2 17:30:21 CST 2007
</tt></blockquote>

Modullerini listeleyelim.

<blockquote><tt>
&gt; <strong>cat proc/modules</strong>

ip_nat_pt 103680 0 - Live 0xc0100000
ip_conntrack_pt 110816 1 ip_nat_pt, Live 0xc00e3000
ipt_state 544 2 - Live 0xc00de000
ipt_mark 416 0 - Live 0xc00dc000
ipt_limit 896 2 - Live 0xc00da000
ipt_connlimit 1696 0 - Live 0xc00d8000
ipt_TCPMSS 2304 2 - Live 0xc00d1000
ipt_REDIRECT 768 0 - Live 0xc00d3000
ipt_MASQUERADE 1536 1 - Live 0xc00cd000
ipt_MARK 704 5 - Live 0xc00cf000
ipt_LOG 4064 2 - Live 0xc00b3000
ipt_FTOS 992 0 - Live 0xc00b5000
ip_nat_tftp 1888 0 - Live 0xc00cb000
ip_nat_rtsp 4816 0 - Live 0xc00c8000
ip_nat_ftp 2976 0 - Live 0xc00c0000
ip_conntrack_tftp 1824 0 - Live 0xc00be000
ip_conntrack_rtsp 15680 1 ip_nat_rtsp, Live 0xc00c3000
ip_conntrack_ftp 20608 1 ip_nat_ftp, Live 0xc00b7000
nat_cache 7856 0 - Live 0xc0059000
ip_nat_ipsec 46720 0 - Live 0xc00a6000
ip_conntrack_ipsec 30640 0 - Live 0xc009d000
ip_nat_h323 2208 0 - Live 0xc009b000
ip_conntrack_h323 10768 1 ip_nat_h323, Live 0xc0097000
ip_nat_pptp 2048 0 - Live 0xc0095000
ip_conntrack_pptp 3312 0 - Live 0xc0093000
ip_nat_gre 1280 0 - Live 0xc0063000
ip_conntrack_gre 2064 2 ip_nat_pptp,ip_conntrack_pptp, Live 0xc0061000
iptable_mangle 960 1 - Live 0xc0020000
iptable_nat 15312 11 ip_nat_pt,ipt_REDIRECT,ipt_MASQUERADE,ip_nat_tftp,ip_nat_rtsp,ip_nat_ftp,ip_nat_ipsec,ip_nat_h323,ip_nat_pptp,ip_nat_gre, Live 0xc005c000
ip_conntrack 28720 21 ip_nat_pt,ip_conntrack_pt,ipt_state,ipt_connlimit,ipt_REDIRECT,ipt_MASQUERADE,ip_nat_tftp,ip_nat_rtsp,ip_nat_ftp,ip_conntrack_tftp,ip_conntrack_rtsp,ip_conntrack_ftp,nat_cache,ip_nat_ipsec,ip_conntrack_ipsec,ip_nat_h323,ip_conntrack_h323,ip_nat_pptp,ip_conntrack_pptp,ip_conntrack_gre,iptable_nat, Live 0xc008a000
iptable_filter 928 1 - Live 0xc001e000
ip_tables 14144 13 ipt_state,ipt_mark,ipt_limit,ipt_connlimit,ipt_TCPMSS,ipt_REDIRECT,ipt_MASQUERADE,ipt_MARK,ipt_LOG,ipt_FTOS,iptable_mangle,iptable_nat,iptable_filter, Live 0xc004e000
bcm_usb 15952 0 - Live 0xc0008000
bcm_enet 23824 0 - Live 0xc0047000
bcmprocfs 13440 0 - Live 0xc0010000
br2684 62272 0 - Live 0xc0036000
blaa_dd 6880 0 - Live 0xc000d000
adsldd 140320 0 - Live 0xc0066000
atmapi 64640 3 br2684,blaa_dd,adsldd, Live 0xc0025000
</tt></blockquote>
Modemde çalışan "prosesleri" görelim.

<blockquote><tt>
&gt; <strong>ps</strong>

 1 admin        64 S   init                
    2 admin           SWN [ksoftirqd/0]
    3 admin           SW&lt; [events/0]
    4 admin           SW&lt; [khelper]
    5 admin           SW&lt; [kblockd/0]
    6 admin           SW  [pdflush]
    7 admin           SW  [pdflush]
    8 admin           SW  [kswapd0]
    9 admin           SW&lt; [aio/0]
   10 admin           SW  [mtdblockd]
   17 admin        96 S   -sh 
   47 admin       232 S   cfm 
  139 admin        52 S   pvc2684d 
  230 admin       128 S   dhcpd 
  237 admin       148 S   snmpd
  250 admin       280 S   httpd
  254 admin       172 S   pppd -c 8.35.1 -i nas_8_35 -u linuxman@ttnet -p *****
  482 admin       184 S   upnp -L br0 -W ppp_8_35_1 -D 
  796 admin       180 S   dproxy -D Home 
 1371 admin       304 S   telnetd
 1372 admin       336 S   telnetd
 1383 admin       272 S   sh -c ps 
 1384 admin       264 R   ps 
</tt></blockquote>

Network ayarları hakkında detaylı bilgi alalım.
<blockquote><tt>
&gt; <strong>ifconfig</strong>

br0             Link encap:Ethernet  HWaddr 00:08:5C:8E:B7:DC  
                inet addr:192.168.1.1  Bcast:192.168.1.255  Mask:255.255.255.0
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:5061439 errors:0 dropped:0 overruns:0 frame:0
                TX packets:5372416 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:0 
                RX bytes:420761271 (401.2 MiB)  TX bytes:2239306342 (2.0 GiB)

eth0            Link encap:Ethernet  HWaddr 00:08:5C:8E:B7:DC  
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:4793160 errors:329 dropped:0 overruns:0 frame:0
                TX packets:5023907 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:1000 
                RX bytes:547037243 (521.6 MiB)  TX bytes:1825231120 (1.6 GiB)
                Interrupt:23 Base address:0x2800 

lo              Link encap:Local Loopback  
                inet addr:127.0.0.1  Mask:255.0.0.0
                UP LOOPBACK RUNNING  MTU:16436  Metric:1
                RX packets:4 errors:0 dropped:0 overruns:0 frame:0
                TX packets:4 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:0 
                RX bytes:365 (365.0 B)  TX bytes:365 (365.0 B)

nas_8_35        Link encap:Ethernet  HWaddr 00:08:5C:8E:B7:DF  
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:5458874 errors:0 dropped:0 overruns:0 frame:0
                TX packets:5051758 errors:0 dropped:19208 overruns:0 carrier:0
                collisions:0 txqueuelen:1000 
                RX bytes:2212357361 (2.0 GiB)  TX bytes:577014523 (550.2 MiB)

ppp_8_35_1      Link encap:Point-Point Protocol  
                inet addr:8*.*.*.*  P-t-P:8*.**.*.*  Mask:255.255.255.255
                UP POINTOPOINT RUNNING NOARP MULTICAST  MTU:1492  Metric:1
                RX packets:4068092 errors:0 dropped:0 overruns:0 frame:0
                TX packets:3791577 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:3 
                RX bytes:488070832 (465.4 MiB)  TX bytes:314043576 (299.4 MiB)

usb0            Link encap:Ethernet  HWaddr 00:08:5C:8E:B7:DD  
                UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
                RX packets:350896 errors:0 dropped:0 overruns:0 frame:0
                TX packets:432777 errors:0 dropped:0 overruns:0 carrier:0
                collisions:0 txqueuelen:1000 
                RX bytes:43181752 (41.1 MiB)  TX bytes:514828098 (490.9 MiB)
</tt></blockquote>
IP Routing table için :

<blockquote><tt>
&gt; <strong>route show</strong>

Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
8*.**.*.*      *               255.255.255.255 UH    0      0        0 ppp_8_35_1
192.168.1.0     *               255.255.255.0   U     0      0        0 br0
default         8*.**.*.*      0.0.0.0         UG    0      0        0 ppp_8_35_1

</tt></blockquote>
IPTable için :

<blockquote><tt>
&gt; <strong>iptables -L -n</strong>

Chain INPUT (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     udp  --  0.0.0.0/0            0.0.0.0/0           udp dpt:161 
ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0           state RELATED,ESTABLISHED 
LOG        tcp  --  0.0.0.0/0            0.0.0.0/0           tcp flags:0x16/0x02 limit: avg 6/hour burst 5 LOG flags 0 level 1 prefix `Intrusion -&gt; ' 
DROP       all  --  0.0.0.0/0            0.0.0.0/0           

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     tcp  --  0.0.0.0/0            192.168.1.2         tcp dpt:5647 
TCPMSS     tcp  --  0.0.0.0/0            0.0.0.0/0           tcp flags:0x06/0x02 TCPMSS clamp to PMTU 
TCPMSS     tcp  --  0.0.0.0/0            0.0.0.0/0           tcp flags:0x06/0x02 TCPMSS clamp to PMTU 
ACCEPT     all  --  0.0.0.0/0            0.0.0.0/0           state RELATED,ESTABLISHED 
LOG        tcp  --  0.0.0.0/0            0.0.0.0/0           tcp flags:0x16/0x02 limit: avg 6/hour burst 5 LOG flags 0 level 1 prefix `Intrusion -&gt; ' 
DROP       all  --  0.0.0.0/0            0.0.0.0/0           

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination

</tt></blockquote>

Modemi yeniden başlatmak için :

<blockquote><tt>
&gt; <strong>reboot</strong>

</tt></blockquote>

Modemin web arayüzündeki web sayfaları anadizindeki "webs" dizini içindedir.Onlara da göz atmak isterseniz örnek olarak:

<blockquote><tt>
&gt; <strong>cat webs/main.html</strong>

</tt></blockquote></body></html>