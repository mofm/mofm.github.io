<html><body><pre>  ,           ,
 /             \
((__-^^-,-^^-__))
 `-_---' `---_-'
  `--|o` 'o|--'
     \  `  /
      ): :(
      :o_o:
       "-"</pre>
Freetalk konsol tabanlı bir jabber client'tır.Konsoldan freetalk programı ile jabber'a bağlanıp özgürce iletişim kurabilirsiniz. Özgürce kullanabileceğiniz,konfigure edilebilen,isterseniz geliştirilebilen özgür bir yazılımdır.Son kararlı sürümü "freetalk-3.2"dir. Freetalk indirmek için <a href="http://savannah.gnu.org/download/freetalk/freetalk-3.2.tar.gz">buradan </a>

<strong>Freetalk kullanımı:</strong>

freetalk  [<var>seçenek</var>] örnek [seçenek] : - j=Jabber id , -jid=jabber-id(Jabber kullanıcı id'si)

Script kullanımı ; -s=<var>SCRIPT-FILE</var> | –script=<var>SCRIPT-FILE </var>

-V  | -version = version numarasını gösterir.

-? | –help | –usage = yardım ekranını getirir.
<h3><strong>Feetalk komutları :</strong></h3>
<h3><strong>connect</strong></h3>
<strong>komut:</strong> /connect

Konfigure edilmiş servera bağlanır.
<pre>~\/~ /connect
Connecting...
~\/~</pre>
Eğer sunucu konfigure edilmemişse,hata mesajı verir ve durur;
<pre>~\/~ /connect
Server not set
~\/~</pre>
<h3>disconnect</h3>
<strong>komut :</strong> /disconnect

O an bağlı bulunan server ile bağlantısını keser.
<pre>~\/~ /disconnect
Disconnected from <var>server</var>. Reason (0): User request
~\/~</pre>
<h3>server</h3>
<strong>komut:</strong> <strong>/server </strong><em> [servername]</em>

<em>Bağlanmak istediğiniz herhangi biri servere bağlar ya da bağlı bulunduğunuz serverı size gösterir.</em>
<pre>~\/~ /server
Current server:
~\/~ /server jabber.org
~\/~ /server
Current server: jabber.org
~\/~</pre>
<h3>jid</h3>
<strong>komut:</strong> <strong>/jid</strong><em> [kullanıcı_adı@domain[/kaynak]]</em>

<em>Kayıtlı olduğunuz kullanıcı adı ile bağlanmak için ya da bağlı bulunan kullanıcının adını ekrana yazdırır.</em>
<pre>~\/~ /jid
Current JID:
~\/~ /jid avati@jabber.org
~\/~ /jid
Current JID: avati@jabber.org</pre>
<em>
</em>
<h3>add</h3>
<strong>komut:</strong> <strong>/add</strong><em> kullanıcı_adı@domain</em>

<em>Bu komut adresini yazdığınız adresi sizin buddy list'ize ekler.</em>
<pre>~\/~ /add harshavardhanacool@gmail.com
~\/~
<h3>allow</h3>
<strong>komut :</strong> <strong>/allow</strong><em> kullanıcı_adı@domain

</em><em> </em></pre>
Adresini yazdığınız kullanıcının sizin durumunuzu görmesine izin verir.
<pre>~\/~ /allow haddock@marlinspike.org</pre>
<h3>deny</h3>
<strong>komut:</strong> <strong>/deny</strong><em> kullanıcı_adı@domain</em>

<em>Yazdığınız kişi sizin durumunuzu görmesini engellersiniz.</em>
<pre>~\/~ /deny cacafonix@village.gl</pre>
<h3>quit</h3>
<strong>komut:</strong><strong> </strong><strong>/quit</strong><em> mesaj</em>

<em>Freetalk programından çıkmanızı sağlar.</em>
<pre>~\/~ /quit
shell$</pre>
<h3>restart</h3>
<strong>komut:</strong> <strong>/restart</strong>

<strong>Bu komutla programı yeniden başlatırsınız.</strong>
<pre>~\/~ /restart
Loading dictionary [/usr/share/dict/words]... [38619] words
Jabber ID:
<h3>who</h3>
</pre>
<strong>komut:</strong> <strong>/who</strong>

<strong>Bu komut listenizde bulunan kişileri durumları ile birlikte gösterir.</strong>
<pre>~\/~ /who
 * abindian@gmail.com (ab)
   twistedlogix@gmail.com
 * tejasvk@gmail.com -&gt; [Away] (on metarnity leave)
   basavanagowda@gmail.com
   amarts@gmail.com (ts3)
~\/~
<h3>status</h3>
</pre>
<strong>komut:</strong><strong> /status</strong><em> [online|away|chat|xa|dnd] [Mesaj]</em>

<em>Bu komutla durumunuzu değiştirebilirsiniz.</em>
<pre>~\/~ /status online Using Freetalk
~\/~ /status
Current status: online Using Freetalk
~\/~
<h3>whoami</h3>
</pre>
<strong>komut:</strong> <strong>/whoami</strong>

<strong>O an hangi kimlikle giriş yaptığınızı gösterir.</strong>
<pre>~\/~ /whoami
~\/~ /whoami
Jabber ID: avati@zresearch.com
Jabber Server: jabber.org
Status: hacking
~\/~</pre>
<h3>version</h3>
<strong>komut:</strong> <strong>/version</strong>

<strong>Freetalk programının versiyonunu ekrana yazar.</strong>
<pre>~\/~ /version
freetalk (Freetalk) 3.2
Copyright (C) 2005, 2007 FreeTalk Core Team
…

~\/~</pre>
<h3>logout</h3>
<strong>komut:</strong> <strong>/logout</strong>

<strong>Bu komut /disconnect komutu ile aynıdır.</strong>
<pre>~\/~ /logout
Disconnected from <var>server</var>, reason(0): User request
~\/~</pre>
<h3>history</h3>
<strong>komut: </strong><strong>/history</strong><em> [kullanıcı_adı]</em>

Bu komutla geçmiş görüşmeleri ekrana yazdırabilirsin.Eğer kullanıcı adı girilmemişse o an ki açık olan oturumdaki geçmişi gösterir.
<pre>~\/~ /history emre.eryilmaz@jabber.org

Prints the history of messages with</pre>
<pre>emre.eryilmaz@jabber.org paginated by <code>less</code>.</pre>
~\/~ /history

Prints this history of messages of the current session.

~\/~
<h3>login</h3>
<strong>komut:</strong> <strong>/login</strong>

<strong>/disconnect ile çıkış yaptıktan daha sonra bu komutla normal giriş yapabilirsiniz.</strong>
<pre>~\/~ /login
Jabber ID: emre.eryilmaz@jabber.org
Password:
Enable TLS/SSL (Y/N)? [Y]: y
Port [5223]: 2401
Connecting...
~\/~
<h3>help</h3>
</pre>
<strong>komut:</strong> <strong>/help</strong><em> [freetalk-komutu]</em>

<em>/help komutu yanına yazılan diğer komut hakkında bilgi gösterir.</em>
<pre>~\/~ /help /history
/history - /history [BUDDY]
         Display history page by page
~\/~</pre>
<h3>freetalk</h3>
<strong>komut:</strong> <strong>/freetalk</strong><em> kullanıcı_adı</em>

<em>Bu komutla yazdığınız kullanıcının freetalk kullanıp kullanmadığını öğrenirsiniz.</em>
<pre>~\/~ /freetalk emre.eryilmaz@jabber.org

Yes emre.eryilmaz@jabber.org is using freetalk.

~\/~</pre>
Şimdilik en önemli olan komutlardan bahsettik.

Eğer freetalk programının açıldığında otomatik olarak giriş yapmasını istiyorsak

"<tt><em><strong>~/.freetalk/freetalk.scm</strong></em>"  yolundaki dosyayı aşağıdaki örnekteki gibi editleyebiliriz.</tt>
<pre>;; Sample ~/.freetalk/freetalk.scm
;; It sets connection parameters and tries to connect on
;; starting freetalk
(and (strings=? (ft-get-jid) "")
                (ft-set-jid! "emre.eryilmaz@jabber.org")
                (ft-set-password! "f00b4r")
                (ft-set-sslconn! 1)
                (ft-set-server! "jabber.org")
                ;; Proxy support
                (ft-set-proxyserver! "your.proxy.org")
                (ft-set-proxyport! "8080"))</pre></body></html>