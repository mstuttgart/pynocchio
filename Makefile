.PHONY: help check clean build coverage lint pre-commit setup test run deploy

# Help target to display available commands
help:
	@echo "Usage: make <target>"
	@echo ""
	@echo "Available targets:"
	@echo "    check         Run pre-commit, docs, tests, and build"
	@echo "    clean         Clean up generated files and caches"
	@echo "    build         Build artefacts distribution"
	@echo "    coverage      Identify code not covered with tests"
	@echo "    lint          Run lint checks on the module"
	@echo "    lint-hint     Run lint checks on the module with hints"
	@echo "    lint-fix      Run lint checks on the module and fix them"
	@echo "    pre-commit    Run pre-commit against all files"
	@echo "    setup         Set up the development environment"
	@echo "    test          Run tests (in parallel)"
	@echo "    run			 Run application"
	@echo "    deploy        Build executable of pynocchio"
	@echo "    rcc           Run rcc to compile the resources .qrc file"
	@echo "    help          Show this summary of available commands"

# Run all checks
check:
	$(MAKE) pre-commit
	$(MAKE) test
	$(MAKE) build

# Clean up generated files and caches
clean:
	find . -name "*.mo" -delete
	find . -name "*.pyc" -delete
	rm -rf .mypy_cache/ .pytest_cache/ .ruff_cache/ dist/ tox/
	rm -rf .coverage .coverage.xml htmlcov junit.xml
	rm -rf .pytest_cache/ .ruff_cache/ .mypy_cache/
	rm -rf build
	pyside6-project clean .

# Build package distribution
build:
	rm -rf *.egg-info/
	pyside6-project build .

# Run coverage analysis
coverage:
	pytest --cov=src --cov-config=pyproject.toml --cov-report=term-missing --no-cov-on-fail --cov-report=html --junitxml=junit.xml -o junit_family=legacy

# Run lint checks
lint:
	isort --check src tests
	black --check src tests
	ruff check src tests

lint-hint:
	mypy src --ignore-missing-imports --explicit-package-bases

# Run pre-commit hooks
pre-commit:
	pre-commit run --all-files

# Set up the development environment
setup:
	pip install -e ".[dev]"
	pip install -e ".[coverage]"
	pip install -e ".[build]"
	pre-commit install --hook-type pre-commit
	pre-commit install --hook-type pre-push
	pre-commit autoupdate
	mypy --install-types

# Run tests
test:
	pytest -v

# Run pynocchio
run:
	python3 run.py

# run rcc to compile the resources .qrc file
rcc:
	pyside6-rcc resources/resources.qrc -o src/app_rc.py

# build executable of pynocchio
deploy:
	pyside6-project deploy .

appimage:
	pyinstaller  --onedir -n AppRun src/__init__.py
	cp deploy/appimage/* dist/*/
	appimagetool dist/*/
