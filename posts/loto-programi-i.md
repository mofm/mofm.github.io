<html><body><blockquote><code>#!/usr/bin/env python
#-*-coding:utf-8-*-</code>
<pre>import random</pre>
<pre>print " Loto Çekiliş Programına Hoşgeldiniz!!!! "</pre>
<pre>secenek1=" (1) Sayısal Loto "
secenek2=" (2) Süper Loto "
secenek3=" (3) On numara "
secenek4=" (4) Şans Topu "</pre>
<pre>print secenek1
print secenek2
print secenek3
print secenek4
print
print "Çıkış için 'q' yazınız."</pre>
<pre>while True:</pre>
<pre>secim=raw_input("Lütfen çekiliş yapacağınız lotonun numarasını giriniz: ")</pre>
<pre>if secim=="1":
sayisal_loto=random.sample(range(1,49), 6)
sayisal_loto.sort()
print
print "Sayısal Loto uğurlu sayılarınız: ", sayisal_loto</pre>
<pre>if secim=="2":
super_loto=random.sample(range(1,54), 6)
super_loto.sort()
print
print "Süper Loto uğurlu sayılarınız: ", super_loto</pre>
<pre>if secim=="3":
on_numara=random.sample(range(1,80), 22)
on_numara.sort()
print
print "On Numara uğurlu sayılarınız: ", on_numara</pre>
<pre>if secim=="4":
sans_topu1=random.sample(range(1,34), 5)
sans_topu2=random.sample(range(1,14), 1)
sans_topu1.sort()
print
print "Şans Topu uğurlu sayılarınız: ",sans_topu1,"+",sans_topu2
if secim=="q":
break</pre>
</blockquote></body></html>