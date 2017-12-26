VENV=.venv

.DEFAULT: null
.PHONY: null
null:
	@echo No default target.

.PHONY: venv
venv: ${VENV}

${VENV}:
	@python3 -mvenv ${@}
	@${VENV}/bin/python setup.py install

.PHONY: lint
lint:
	@pylint --rcfile=pylint.cfg .

.PHONY: flake8
flake8:
	@flake8

.PHONY: test
test:
	@pytest

.PHONY: clean
clean:
	rm -rf ${VENV}
