all:

install:
	mkdir -p ~/.weechat/python
	cp force_redraw.py ~/.weechat/python
	ln -s ~/.weechat/python/force_redraw.py ~/.weechat/python/autoload

.PHONY: all install
