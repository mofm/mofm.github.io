<html><body><p>Active State adlı sitede gözüme çarpan "<strong>Password Generator</strong><em>" scripti.</em>
</p><blockquote><code>
#!/usr/bin/env python
"""
A simple script for making random passwords, WITHOUT 1,l,O,0.  Because
those characters are hard to tell the difference between in some fonts.</code>

<em>"""</em>
<pre><em>#Import Modules
import sys
from random import Random</em></pre>
<pre><em>rng = Random()
</em></pre>
<pre><em>righthand = '23456qwertasdfgzxcvbQWERTASDFGZXCVB'
lefthand = '789yuiophjknmYUIPHJKLNM'
allchars = righthand + lefthand</em></pre>
<pre><em>try:
passwordLength = int(sys.argv[1])
except:
#user didn't specify a length.  that's ok, just use 8
passwordLength = 8
try:
alternate_hands = sys.argv[2] == 'alt'
if not alternate_hands:
print "USAGE:"
print sys.argv[0], "[length of password]",
print "[alt (if you want the password to alternate hands]"
except:
alternate_hands = False</em></pre>
<pre><em>for i in range(passwordLength):
if not alternate_hands:
sys.stdout.write( rng.choice(allchars) )
else:
if i%2:
sys.stdout.write( rng.choice(lefthand) )
else:
sys.stdout.write( rng.choice(righthand) )</em></pre>
</blockquote></body></html>