<html><body><p>Squid tam bir derya ve bunlardan birkaç kısa not :

<strong>* Squid proxy arkasındaki ip'ler hakkında bilgi vermemek için :</strong>

/etc/squid/squid.conf içerisine ,

<code>forwarded_for off  ,-- satırını ekleyin.</code>

 

<strong>* Squid Proxy Server'ın versiyonu hakkında dışarıya bilgi vermemek için:</strong>

<code>httpd_suppress_version_string on  , -- satırını "/etc/squid/squid.conf" dosyanıza ekleyin.</code>

 

<strong>* Bazı proxy detect taraması yapan yazılımlardan ve buna benzer sitelerden ( <a href="http://checker.samair.ru/" target="_blank">http://checker.samair.ru/</a> , <a href="http://ip.my-proxy.com/" target="_blank">http://ip.my-proxy.com/</a> , vs) squid proxy server'ınızı gizlemek için aşağıdaki satırları konfigurasyon dosyanıza ekleyin :</strong>

header_access Allow allow all
header_access Authorization allow all
header_access WWW-Authenticate allow all
header_access Proxy-Authorization allow all
header_access Proxy-Authenticate allow all
header_access Cache-Control allow all
header_access Content-Encoding allow all
header_access Content-Length allow all
header_access Content-Type allow all
header_access Date allow all
header_access Expires allow all
header_access Host allow all
header_access If-Modified-Since allow all
header_access Last-Modified allow all
header_access Location allow all
header_access Pragma allow all
header_access Accept allow all
header_access Accept-Charset allow all
header_access Accept-Encoding allow all
header_access Accept-Language allow all
header_access Content-Language allow all
header_access Mime-Version allow all
header_access Retry-After allow all
header_access Title allow all
header_access Connection allow all
header_access Proxy-Connection allow all
header_access All deny all

<em>Buraya küçük bir not düşeyim , 3.0 versiyon ve üzeri squid kullanıcıları "header_access" yerine "request_header_access" kullanmalıdır."header_access" 2.6 ve daha eski sürümler için geçerlidir.</em></p></body></html>