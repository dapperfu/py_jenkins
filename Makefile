.DEFAULT: null
.PHONY: null
null:
	echo Target must be specified. No default option.

venv:
	python3 -mvenv venv

.PHONY: lint
lint:
	@pylint --rcfile=pylint.cfg .

.PHONY: flake8
flake8:
	@flake8

.PHONY: test
test:
	@pytest
