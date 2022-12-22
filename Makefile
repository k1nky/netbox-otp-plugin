clean:
	rm -rf build
	rm -rf dist

wheel:
	python -m build -w

build: clean wheel

upload:
	twine upload --skip-existing dist/*