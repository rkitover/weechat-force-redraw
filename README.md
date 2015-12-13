# force_redraw.py

This is a trivial script to force a screen redraw on every new line in
a window. May be useful if you have a misbehaving terminal.

Currently it causes a lot of flicker, so is not very pleasant to use,
consider experimental.

## installation

To install the git version:

```bash
git clone https://github.com/rkitover/weechat-force-redraw.git
cd weechat-force-redraw
make install
```

Then either restart WeeChat or do a:

```
/script load force_redraw.py
```
