.PHONY: dist upload clean

dist:
	python3 setup.py sdist bdist_wheel

upload:
	twine upload dist/*

clean:
	rm -rf dist
	rm -rf build
	rm -rf *.egg-info

