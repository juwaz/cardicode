install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --doctest-modules

format:
	black *.py


lint:
	touch __init__.py; pylint --rcfile=.pylintrc `pwd`; trap 'rm -f __init__.py' EXIT

all: install lint test
