<html><body><img class="alignright" title="Nagios" src="http://lh6.ggpht.com/_lrGAZKHmne0/TJkj9rB--CI/AAAAAAAACmk/VaJDtsbBq-Y/nagios-150x150%5B2%5D.png?imgmax=800" alt="" width="150" height="150">Debian Squeeze <em>nagios-images</em> paketi ile kurulan iconlardan "<em>ubuntu.gd2</em>" paketlenirken yanlış çevrildiği için nagios "status map"'de "<em>unknown</em>" işareti ile gösterilebilir.
Eğer düzgün bir şekilde ubuntu logosunun gözükmesini istiyorsanız "<em>ubuntu.png</em>" dosyasını düzgün bir şekilde <strong>gd2</strong> formatına çevirmemiz gerekir.
Bu çevirme işlemi için pngtogd2 aracı sistemimizde yüklü olması lazım.Eğer yüklü değilse "libgd-tools" paketini kurun.

<em><strong>#</strong> apt-get install libgd-tools</em>

Şimdi de logos/base dizininde bulunan "<em>ubuntu.png</em>" iconunu "<strong>.gd2</strong>" formatına çevirelim.

<strong>#</strong> <em>pngtogd2 ubuntu.png ubuntu.gd2 0 1</em>

Çevirme işlemi tamamlandıktan sonra "<em>extinfo_nagios2.cfg</em>" dosyasında gerekli yere "<em>statusmap_image  base/ubuntu.gd2</em>" şeklinde düzeltin.</body></html>