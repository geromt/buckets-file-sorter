all: install

install:
	mkdir -p ~/.local/share/buckets
	cp ./app/main.py ~/.local/share/buckets
	cp ./app/sorter.py ~/.local/share/buckets
	ln -s ~/.local/share/buckets/main.py ~/.local/bin/buckets

clean:
	rm -fr ~/.local/share/buckets
	rm -f ~/.local/bin/buckets