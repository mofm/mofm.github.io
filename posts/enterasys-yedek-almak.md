<html><body><p>Büyük bir ağa bakıyorsanız ve ağ üzerinde kenar switchler farklı konfigurasyonlara sahip ise bunları yedeklemek ve herhangi bir sorun anında yedeklerden restore etmek büyük bir önem taşıyor.

Enterasys kenar switchlerde konfigurasyonları yedeklemek ve bu yedeği bir TFTP sunucusuna aktarmak için birkaç adım :
</p><h4>1.Adım:</h4>
Eğer varsa eski konfigurasyonları listeleyelim :

<strong>#  dir </strong> <em></em>

Images:
==================================================================
Filename:      c2-series_05.00.75
Version:       05.00.75
Size:          7677952 (bytes)
Date:          Tue Aug  7 09:41:04 2007
CheckSum:      4d76baca7158f071f9ef1245d22c5466
Compatibility: C2G124-24, C2G124-48, C2H124-48, C2G124-48P, C2H124-48P
C2K122-24, C2G170-24, C2G134-24P, C3G124-24, C3G124-24P
C3G124-48, C3G124-48P

Filename:      c2-series_05.02.07.0006 (Active) (Boot)
Version:       05.02.07.0006
Size:          9479168 (bytes)
Date:          Sat Oct 10 15:22:25 2009
CheckSum:      06bebc6af033e7e27a0327f04c991164
Compatibility: C2G124-24, C2G124-48, C2H124-48, C2G124-48P, C2H124-48P
C2K122-24, C2G170-24, C2G134-24P, C3G124-24, C3G124-24P
C3G124-48, C3G124-48P, C3K122-24, C3K122-24P, C3K172-24

Files:                           Size
================================ ========
configs:
07102011                         12389
logs:
current.log                      167441

Yukarıda görüldüğü gibi "<em>07102011</em>" dosya isimli bir yedek mevcut.
<h4>2.Adım:</h4>
Switch üzerindeki şu anki konfigurasyonun yeni yedeğini alalım,

<strong># show config outfile configs/26102011</strong>

"<em>26102011</em>" dosya ismiyle yedeğimizi oluşturduk.
<h4>3.Adım:</h4>
Şimdi yedeğini aldığımız konfigurasyon dosyasını uzaktaki TFTP sunucusuna yükleyelim.

<strong># copy configs/26102011 tftp://192.168.1.12/26102011</strong><a href="http://10.1.60.7/c2-series_05.02.13.0003" target="_blank"></a></body></html>