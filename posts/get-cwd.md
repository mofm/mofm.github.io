<html><body><blockquote><code>#!/usr/bin/env python
#-*- coding:utf-8 -*-</code>
<pre>import os</pre>
<pre>here=os.getcwd()</pre>
<pre>print here ," dizininde bulunmaktasınız."</pre>
<pre>icerik=raw_input("Eğer dizin içeriğini görmek isterseniz enter'a basınız. ")</pre>
<pre>if icerik=="evet" :
c=0
for i in os.listdir(here):
c=c+1
print c," . ", i</pre>
</blockquote></body></html>