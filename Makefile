clean:
	rm -rf build
	rm -rf dist

wheel:
	python3 -m build -w

build: clean wheel

upload:
	twine upload --skip-existing dist/*