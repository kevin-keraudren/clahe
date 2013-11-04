
all:
	mkdir -p tmp
	mkdir -p lib
	touch lib/__init__.py
	python setup.py build_ext --build-temp tmp --build-lib lib --pyrex-c-in-temp
