<html><body><p>Linux'de uçbirim basit hesap makinesi gibi kullanabilir.Toplama,çarpma,çıkarma,bölme işlemlerini basit bir komutla sonuçlandırabiliriz.İşmelerimizi "<strong>echo "$((__))</strong> " (<strong>'_'</strong>:yapacağımız matematiksel işlem) şeklinde yapıyoruz.Aşağıdaki örneklere bakalım.

<strong>TOPLAMA</strong>
</p><pre>$ echo $((50+30))</pre>
<pre>80</pre>
<strong>ÇIKARMA</strong>
<pre>$ echo $((50-30))</pre>
<pre>20</pre>
<strong>ÇARPMA</strong>
<pre>$ echo $((50*30))</pre>
<pre>1500</pre>
<strong>BÖLME</strong>
<pre>$ echo $((60/30))</pre>
<pre>2</pre>
Böyle yaptığımız yaptığımız  tam bölünmeyen,sonucu ondalık olan sayıları size yine tam olarak gösterecektir.Mesela ;
<pre>$ echo $((70/30))</pre>
<pre>2</pre>
Gördüğünüz gibi 70'in 30'a bölümü ondalık bir sayı olduğu için bize tam ifadesini yuvarlayarak verdi.Eğer tam bölünmeyenlerde yada karışık matematik işlemlerinde tam sonucu almak istiyorsak <strong>"bc" </strong>komutunu kullanmalıyız.Aşağıda basit örneklere bakınız.
<pre>$ echo "scale=5; 5/2"|bc</pre>
<pre>2,50000</pre>
<pre>$ echo "scale=70; 70/30"|bc</pre>
<pre>2.33333333333333333333333333333333333333333333333333333...</pre>
Gördüğünüz gibi sonucu tam olmayan ve karışık matematiksel işlemlerde yukardaki gibi <strong>"bc"</strong> komutunu kullanıyoruz.

<strong>ÜS ALMA</strong>
<pre>$ echo $((2**3))</pre>
<pre>8</pre>
Üs alma işlemi de yukarda görüldüğü gibi .

Kolay gelsin.

Örnek ekran Görüntüsü:

<a href="http://img641.imageshack.us/img641/8773/ekrangoruntusu.png"><img title="Konsolda hesap yapmak" src="http://img641.imageshack.us/img641/8773/ekrangoruntusu.png" alt="" width="490" height="323"></a></body></html>