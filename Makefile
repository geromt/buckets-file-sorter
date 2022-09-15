all: install

install:
	mkdir -p ~/.local/share/buckets
	cp ./app/buckets.py ~/.local/share/buckets
	cp ./app/organizer.py ~/.local/share/buckets
	ln -s ~/.local/share/buckets/buckets.py ~/.local/bin/buckets

clean:
	rm -fr ~/.local/share/buckets
	rm -f ~/.local/bin/buckets