.DEFAULT_GOAL := help
sources = src tests

.PHONY: install  ## Install the package, dependencies, and pre-commit for local development
install:
	python -m pip install -e .[dev]
	# TODO: pre-commit install --install-hooks

.PHONY: format  ## Auto-format python source files
format:
	python -m black $(sources)
	python -m ruff --fix $(sources)
	python -m ruff format $(sources)

.PHONY: lint  ## Lint python source files
lint:
	python -m ruff $(sources)
	python -m ruff format --check $(sources)
	python -m black $(sources) --check --diff

.PHONY: codespell  ## Use Codespell to do spellchecking
codespell:
	@echo "TODO:"

.PHONY: test  ## Run all tests
test:
	python -m pytest --cov-report term --cov-report=xml --cov=$(sources)

.PHONY: testcov  ## Run tests and generate a coverage report
testcov:
	@echo "TODO:"

.PHONY: all  ## Run the standard set of checks performed in CI
all: lint test

.PHONY: clean  ## Clear local caches and build artifacts
clean:
	# remove Python file artifacts
	rm -rf `find . -name __pycache__`
	rm -f `find . -type f -name '*.py[co]'`
	rm -f `find . -type f -name '*~'`
	rm -f `find . -type f -name '.*~'`
	rm -rf .cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	# remove build artifacts
	rm -rf build
	rm -rf dist
	rm -rf `find . -name '*.egg-info'`
	rm -rf `find . -name '*.egg'`
	# remove test and coverage artifacts
	rm -rf .tox/
	rm -f .coverage
	rm -f .coverage.*
	rm -rf coverage.xml
	rm -rf htmlcov/
	rm -rf .pytest_cache
	rm -rf htmlcov

.PHONY: docs  ## Generate the docs
docs:
	@echo "TODO:"

.PHONY: build  ## Build a source distribution and a wheel distribution
build: all clean
	python -m build

.PHONY: publish  ## Publish the distribution to PyPI
publish: build
	python -m twine upload dist/* --verbose

.PHONY: help  ## Display this message
help:
	@grep -E \
		'^.PHONY: .*?## .*$$' $(MAKEFILE_LIST) | \
		sort | \
		awk 'BEGIN {FS = ".PHONY: |## "}; {printf "\033[36m%-19s\033[0m %s\n", $$2, $$3}'
