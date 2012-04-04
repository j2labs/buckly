# Buck.ly

buck.ly is a bit.ly clone, written in Brubeck and sorta paying homage to Jeff
Buckley.


## Screenshots

It looks like this:

![URL entry](https://github.com/j2labs/buckly/raw/master/screenshots/1.png)

Enter a URL, hit save, and you'll be greeted with a short URL that will expand to the original, and increment a count on how many times it's been dereferenced.

![A shortened URL](https://github.com/j2labs/buckly/raw/master/screenshots/2.png)

If you enter that URL in your browser, you'll be redirected to the URL.

![Expanded URL](https://github.com/j2labs/buckly/raw/master/screenshots/3.png)


## How It Works

The url shortening code is based works by counting up from 0 and simply
converts from that count to base 52.  Normally, base 62 is a good choice, but
I removed the vowels to prevent accidentally creating curse words in short
urls.

*The base conversion code is from this snippet: 
[http://code.activestate.com/recipes/111286/](http://code.activestate.com/recipes/111286/)*

There is a `LinkExpansionHandler` that will take a short URL code and send an
HTTP 302 to redirect a browser to the expanded URL.


## API

There is also a very simple API. It just implements HTTP GET and returns the 
expanded URL.

Check out the [Todos](https://github.com/j2labs/todos) project for a better
experience building APIs. *Uses backbone.js too!*

![Simple API example](https://github.com/j2labs/buckly/raw/master/screenshots/4.png)
