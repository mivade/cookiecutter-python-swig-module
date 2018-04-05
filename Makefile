.PHONY: help clean test

help:
	@echo "Usage: make <help|clean|test>"

clean:
	rm -rf extmodule

test: clean
	cookiecutter --no-input .
	cd extmodule && python setup.py install
	cd ~ && python -c "import extmodule; extmodule.square(2)"
