.DEFAULT: null
.PHONY: null
null:
	echo Target must be specified. No default option.

venv:
	python3 -mvenv venv

.PHONY: test
test:
	@pytest
