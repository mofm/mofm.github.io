<html><body><p>Wordpress'de kalıcı bağlantı ayarı yapılırken bazı aksaklıklar çıkabilir.

Bunlardan ilk <em>.htaccess</em> dosyasının olmaması ve yazılamaması.

<strong>Çözüm:</strong> Eğer .htaccess yoksa, blogu kurduğumuz anadizine ".htaccess" adlı bir dosya oluşturup CHMOD izinlerini "666" yapıyoruz.Daha sonra admin panelinde <strong>Ayarlar&gt;Kalıcı Bağlantılar</strong> özel bağlantılarda istediğimiz permalink türevini yazıp değişiklikleri kaydet butonuna basıyoruz.

Eğer ki sorun çözüldü ise sevindim ama çözülmedi <strong>404</strong> hatası verip yazıları açmıyorsa büyük ihtimalde apache webserverınızda <em>mod_rewrite</em> modülü aktif edilmemiştir.Bunun "<a title="Apache webserverda mod_rewrite modülünü aktif etmek(debian ve türevleri için)" href="init.php?u=Oi8vd2Vicy5ob21lbGludXguY29tL2FwYWNoZS13ZWJzZXJ2ZXJkYS1tb2RfcmV3cml0ZS1tb2R1bHVudS1ha3RpZi1ldG1la2RlYmlhbi12ZS10dXJldmxlcmktaWNpbg%3D%3D&amp;b=5">Apache webserverda mod_rewrite modülünü aktif etmek(debian ve türevleri için)</a>" yazısını okuyabilirsiniz.</p></body></html>