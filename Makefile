

VERSION    = `python -c 'import sequtils; print sequtils.__version__'`


help:
	@echo "clean    - remove all build, test, coverage and Python artifacts"
	@echo "release  - package and upload a release"
	@echo "build    - package module"
	@echo "install  - install the package to the active Python's site-packages"


.PHONY: clean
clean:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +


.PHONY: tag
tag:
	VER=$(VERSION) && if [ `git tag | grep "$$VER" | wc -l` -ne 0 ]; then git tag -d $$VER; fi
	VER=$(VERSION) && git tag $$VER -m "sequtils v$$VER"


.PHONY: release
release: tag
	VER=$(VERSION) && git push origin :$$VER || echo 'Remote tag available'
	VER=$(VERSION) && git push origin $$VER
	python setup.py sdist upload -r atgtagtest
	python setup.py sdist upload -r atgtag


.PHONY: build
build: clean
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist


.PHONY: install
install: clean
	python setup.py install
