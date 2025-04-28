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
	@echo "    pre-commit    Run pre-commit against all files"
	@echo "    setup         Set up the development environment"
	@echo "    test          Run tests (in parallel)"
	@echo "    run			 Run application"
	@echo "    deploy        Build executable of pynocchio"
	@echo "    lupdate       Update translation files"
	@echo "    lrelease      Generate .qm file from .ts file"
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
	rm -rf build repo flatpak .flatpak-builder builddir
	pyside6-project clean .
	rm pynocchio.db
	rm pynocchio.deb

# Build package distribution
build:
	rm -rf *.egg-info/
	pyside6-project build .
	$(MAKE) lrelease
	$(MAKE) rcc

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
	mypy --install-types .
	sudo apt install -y poppler-utils # dependencies for reading pdf files

# Run tests
test:
	pytest -v

# Run pynocchio
run:
	pyside6-project run

# run rcc to compile the resources .qrc file
rcc:
	pyside6-rcc resources/resources.qrc -o src/app_rc.py

# build executable of pynocchio
deploy:
	$(MAKE) lrelease
	$(MAKE) rcc
	rm -rf build
	mkdir -p build
	pyside6-project deploy .

# build .deb packages
packages:
	cp -f build/Pynocchio.bin package/usr/bin/pynocchio
	cp -f resources/logo.svg package/usr/share/icons/hicolor/scalable/apps/pynocchio.svg
	rm -f *.deb
	rm -f *.rpm
	rm -f *.pacman
	fpm -t deb -p pynocchio-v4.0.0-amd64.deb
	fpm -t rpm -p pynocchio-v4.0.0-amd64.rpm

# Update and create translation files
lupdate:
	pyside6-lupdate src/views/main_window_view.py -ts i18n/*.ts

# Generate .qm file from .ts file
lrelease:
	pyside6-lrelease i18n/en_US.ts -qm resources/i18n/en_US.qm
	pyside6-lrelease i18n/es_ES.ts -qm resources/i18n/es_ES.qm
	pyside6-lrelease i18n/pt_BR.ts -qm resources/i18n/pt_BR.qm
