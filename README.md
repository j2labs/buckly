# Buck.ly

buck.ly is a bit.ly clone, written in Brubeck and sorta paying homage to Jeff
Buckley.  This is not meant to be a serious tool and is written primarily for teaching
purposes.

The url shortening code is based works by counting up from 0 and simply
converts from that count to base 52.  Normally, base 62 is a good choice, but
I removed the vowels to prevent accidentally creating curse words in short urls.

The base conversion code is from this snippet: 
[http://code.activestate.com/recipes/111286/](http://code.activestate.com/recipes/111286/)
