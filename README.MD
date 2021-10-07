
## Hash Mouse

hash_mouse.py tracks mouse movements in a separate thread and then hashes the positions and timings of the mouse pointer using the [Sha512 algorithm](https://en.wikipedia.org/wiki/SHA-2). Because the data is shared using the multiprocessing module, the main thread must check to see if hashing thread has produced an updated hash at a regular interval.

It then uses this random data to produce a class with functions that produce secure random data for functions like `randint` and `mrandom` which produces a requested number of random bytes.

Usage: `./hash_mouse.py`

or you can import it into your own python program with:

```
from hash_mouse import HashMouse
mhash = HashMouse(verbose=0)
mhash.ensure_min(16)
mhash.randint(start, stop)
```


## Ranword

Ranword uses hash_mouse.py to poll random mouse movements and use the data to generate secure [XKCD style passwords](https://xkcd.com/936/).

Usage: `./ranword.py`

By default, it uses the built-in dictionary at: `/usr/share/dict/words`, but you can also pass it your own custom dictionary by running:

```
./ranword.py <filename>
```

You can download an excellent free dictionary of the top 100,000 words sourced from Wiktionary here: https://gist.github.com/h3xx/1976236 or choose your own custom dictionary file. The only requirement is that each word must be on a seperate line.
