<html><body><p>Her zaman güncel firmware'i kullanmak daha yararlıdır.Enterasys kenar switclerde firmware yükseltmek için küçük adımlar...

Firmware yükseltme işlemine geçmeden önce bir tane <a href="http://en.wikipedia.org/wiki/TFTP" target="_blank">TFTP</a> sunucusunu hazır etmeniz lazım.Yoksa <a href="http://en.wikipedia.org/wiki/XMODEM" target="_blank">XMODEM</a> ile saatlerce beklemeniz lazım :) (Tabi switch üzerindeki tüm "Operation Code"ları(firmware) silerseniz mecburen XMODEM ile yüklemek ve beklemek zorundasınız.)

<strong>1.Adım:</strong>

Eğer switch üzerinde birden fazla firmware varsa,büyük ihtimal yeni firmware yüklemeye yer olmayacaktır.O yüzden uer açmak ilk olarak kullanılmayan eski firmware silelim :
<strong># </strong> dir      <em> (bu komutla eski firmwareleri listeleyin.)</em>

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

# delete c2-series_05.00.75  <em>(siz kendi firmware numaranıza göre silin.)</em>

<strong>2.Adım:</strong>
Bu <a href="https://extranet.enterasys.com/CookieAuth.dll?GetLogon?curl=Z2F&amp;reason=0&amp;formdir=4" target="_blank">adresten</a> ürününüze uygun olan en son firmware'ı TFTP sunucunuza indirin.
TFTP sunucumuza indirdiğimiz yeni firmware'ı switch'e aşağıdaki gibi yükleyin :

# copy tftp://<a href="http://10.1.60.7/c2-series_05.02.13.0003" target="_blank">192.168.1.12/c2-series_05.02.13.0003</a> system:image

<strong>3.Adım:</strong>
Yükleme başarı ile tamamlandıysa yeni firmware ile sistem başlatılır:

# set boot system c2-series_05.02.13.0003

<strong>4.Adım:</strong>

Switch yeniden başladıktan sonra yeni firmware kontrol edilir.

# show boot system</p></body></html>