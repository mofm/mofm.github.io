<html><body><blockquote><code>#!/usr/bin/env python
#-*-coding:utf-8-*-
#Linux Bilgilendirme Projesi</code>
<pre>print "Linux Konsol Bilgilendirme Projesi'ne Hoşgeldiniz"
while True:
arama=raw_input("Lütfen meta giriniz: ")</pre>
<pre>veritabani={ "linux":"GNU/Linux, Linux çekirdeği kullanan Unix benzeri işletim sistemlerini çağrıştıran genel kullanım şeklidir.
Linux açık kaynak kod geliştirme modelinin ve özgür yazılımının en öne çıkan örneklerinden birisidir; tipik olarak tüm
kaynak kodu tamamıylakullanılabilir, ücretsizce değiştirilebilir ve herhangi biri tarafından yeniden dağıtılabilir.",
"debian":"Debian, Debian Projesi kapsamında dünyanın çeşitli bölgelerindeki gönüllüler tarafından hazırlanan; GNU/Linux,
 GNU/Hurd gibi farklı çekirdek seçeneklerine dayalı tamamen özgür bir Linux dağıtımıdır. En yaygın GNU/Linux dağıtımlarından
biri konumundaki Debian aynı zamanda; Mepis, Ubuntu,Yoper, Knoppix, Libranet, Linspire, Xandros ve Adamantix gibi birçok GNU/Linux
dağıtımına da kaynak teşkil etmekte ve Google başta olmak üzere iyi tanınan birçok Web sitesinde de tercih edilmektedir. Debian,
farklı işletim sistemi çekirdekleriyle birlikte i386, AMD64, PowerPC, SPARC, DEC Alpha, ARM, MIPS, HPPA, S390, IA-64
gibi çok sayıda donanım platformunda da çalışabilmektedir."}</pre>
<pre>print veritabani.get(arama,"Aradığınız öğe halen eklenmemiştir.")</pre>
<pre>if arama=="q":
break</pre>
</blockquote></body></html>