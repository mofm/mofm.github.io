<html><body><p>Sisteminizde birden çok siteye webalizer istatistiklerini sunmak istiyorsanız bunu birkaç konfigurasyonla yapabiliriz.Örneğin sunucuda " <strong>virtual1.example.com</strong>" ve " <strong>virtual2.example.com</strong> " adında iki virtualhostumuz olsun.Bu hostların log dosyaları  " <strong>/var/log/httpd/virtual1-access_log</strong>"  ve " <strong>/var/log/httpd/virtual2-access_log</strong> "
olsun.
İlk önce sisteminizde "webalizer" kurulu değil ise kurun: 



</p><blockquote># yum install webalizer</blockquote>



Webalizer sisteme kurulduktan sonra "<strong> /etc/webalizer.conf</strong> " konumunda konfigurasyon dosyası bulunur.Bizim sistemimizde birden çok site barınacağı için her site için ayrı bir konfigurasyon dosyası oluşturacağız.Bu dosyaları düzenli bir şekilde tutmak için bir klasör oluşturup onun içinde bulunduralım.



<blockquote># mkdir /etc/webalizer
#mv /etc/webalizer.conf /etc/webalizer/webalizer.conf.example  (Eski ayar dosyasını örnek olarak saklayalım)
#touch /etc/webalizer/virtualhost1.conf (birinci sitemiz için ayar dosyasımızı oluşturduk.)
#touch /etc/webalizer/virtualhost2.conf (İkinci sitemiz için ayar dosyamızı oluşturduk)
#mkdir /var/www/virtual1/stats (İstatiskleri yayınlayacağımız dizini oluşturduk.)
#mkdir /var/www/virtual2/stats</blockquote>



Artık sitelerimiz için ayarları dosylarına girebiliriz.

<strong>virtual1.conf :</strong>



<blockquote>LogFile         /var/log/httpd/virtual1-access_log
OutputDir       /var/www/virtual1/stats
HistoryName     /var/lib/webalizer/virtual1.hist
Incremental     yes
IncrementalName /var/lib/webalizer/virtual1.current
HostName        virtual1.example.com
PageType        htm*
PageType        cgi
PageType        php
PageType        shtml
DNSCache        /var/lib/webalizer/dns_cache.db
DNSChildren     10
Quiet           yes
FoldSeqErr      yes
HideURL         *.gif
HideURL         *.GIF
HideURL         *.jpg
HideURL         *.JPG
HideURL         *.png
HideURL         *.PNG
HideURL         *.svg
HideURL         *.SVG
SearchEngine    yahoo.com  p=
SearchEngine    google.com q=
SearchEngine    msn.com    MT=
SearchEngine    bing.com   q=</blockquote>



<strong>virtual2.conf :</strong>



<blockquote>LogFile         /var/log/httpd/virtual2-access_log
OutputDir       /var/www/virtual2/stats
HistoryName     /var/lib/webalizer/virtual2.hist
Incremental     yes
IncrementalName /var/lib/webalizer/virtual2.current
HostName        virtual2.example.com
PageType        htm*
PageType        cgi
PageType        php
PageType        shtml
DNSCache        /var/lib/webalizer/dns_cache.db
DNSChildren     10
Quiet           yes
FoldSeqErr      yes
HideURL         *.gif
HideURL         *.GIF
HideURL         *.jpg
HideURL         *.JPG
HideURL         *.png
HideURL         *.PNG
HideURL         *.svg
HideURL         *.SVG
SearchEngine    yahoo.com  p=
SearchEngine    google.com q=
SearchEngine    msn.com    MT=
SearchEngine    bing.com   q=</blockquote>



Böylece ayarlarımızı dosyalarımıza işledik.Şimdi istatistiklerimizi cron düzenli bir şekilde yenilenen hale getirelim. " <strong>/etc/cron.daily/webalizer</strong> " dosyasını aşağıdaki gibi değiştirin :

<strong>/etc/cron.daily/webalizer</strong> :



<blockquote>#!/bin/bash
if [ -s /var/log/httpd/virtual1-access_log ]; then
/usr/bin/webalizer -Q -c /etc/webalizer/virtual1.conf
fi
if [ -s /var/log/httpd/virtual2-access_log ]; then
/usr/bin/webalizer -Q -c /etc/webalizer/virtual2.conf
fi
</blockquote>


 
Bu konfigurasyonu da yaptıktan sonra ilk istatistiklerimizi aşağıdaki komut ile oluşturalım :



<blockquote># for i in /etc/webalizer/*.conf; do webalizer -c $i; done</blockquote>



" <strong>/etc/httpd/conf.d/webalizer</strong> " dosyasındaki ayarlarınızı düzelttikten sonra tarayıcıdan istatistiklere <strong>http://virtual1.example.com/stats</strong> ve <strong>http://virtual2.example.cpm/stats </strong>adreslerinden bakabiliriz.</body></html>