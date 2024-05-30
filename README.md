# TEN libraries
[TEN](https://github.com/Aadit-Ambadkar/ten) is a programming language made by Aadit Ambadkar. This repository includes some extensions, libraries and projects I made using TEN.
The only change to the TEN source code has been adding support for libraries:
```py
from lib import example1, example2

libraries = [example1, exmaple2]
```
```py
r = False
for lib in libraries:
    r = lib.exec(contents[i], q[0])
    if (r):
        q.appendleft(r)
        break
if not (r):
    try:
        q.appendleft(int(contents[i]))
    except:
        pass
```