<html><body><p>Squid Proxy Server üzerinde ident tanımlamak ve sadece bu tanımlanan kullanıcılara izin vermek için küçük bir örnek :

<small>ident_lookup_access allow all</small>
<small>acl ofisusers  ident emre mehmet adem mustafa</small>
<small>http_access allow ofisusers</small>
<small>http_access deny all</small><small></small>

Daha ayrıntılı bilgi için <a href="http://www.visolve.com/squid/squid26/accesscontrols.php" target="_blank">http://www.visolve.com/squid/squid26/accesscontrols.php</a></p></body></html>