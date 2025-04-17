# Contributing

Thank you for considering contributing! This document outlines the various ways you can contribute to this project and how to get started.

## Bug Reports and Feature Requests

### Found a Bug?

Before reporting an issue, please perform [a quick search](https://github.com/mstuttgart/pynocchio/issues) to check if it has already been reported. If it exists, feel free to comment on the existing issue. Otherwise, open [a new GitHub issue](https://github.com/mstuttgart/pynocchio/issues).

When reporting a bug, ensure you include:

- A clear and concise title.
- A detailed description with relevant information.
- Steps to reproduce the issue and the expected behavior.
- If possible, a code sample or an executable test case demonstrating the issue.

### Have a Suggestion for an Enhancement or New Feature?

We use GitHub issues to track feature requests. Before creating a feature request:

- Ensure you have a clear idea of the enhancement. If unsure, consider discussing it first in a GitHub issue.
- Check the documentation to confirm the feature does not already exist.
- Perform [a quick search](https://github.com/mstuttgart/pynocchio/issues) to see if the feature has already been suggested.

When submitting a feature request, please:

- Provide a clear and descriptive title.
- Explain why the enhancement would be useful, possibly referencing similar features in other libraries.
- Include code examples to demonstrate how the feature would be used.

Contributions are always welcome and greatly appreciated!

## Contributing Fixes and New Features

When contributing fixes or new features, start by forking or branching from the [main branch](https://github.com/mstuttgart/pynocchio/tree/main) to ensure you work on the latest code and minimize merge conflicts.

All contributed [PRs](https://github.com/mstuttgart/pynocchio/pulls) must include valid test coverage to be considered for merging. If you need help with writing tests, don't hesitate to ask.

Thank you for your support!

## Running Tests

To set up the development environment and install all required dependencies, run:

```shell
$ virtualenv -p python3 .venv
$ source .venv/bin/activate
$ make setup
```

The project provides automated style checks, tests, and coverage reports:

```shell
$ make check
```

You can also run them individually:

```shell
$ make pre-commit
$ make test
```

To retrieve uncovered lines, use:

```shell
$ make coverage
```

To run specific tests, use the `pytest` command:

```shell
$ pytest tests/test_page.py
```

For more granular testing:

```shell
$ pytest tests/test_page.py::test_create_page
```

To run tests against the real API, create a `.env` file in the project's root directory with the following content:

```ini
SKIP_REAL_TEST=False
```

This will enable tests that interact with the live API. Ensure you have the necessary permissions and understand the implications of running tests against the real API.

## Code Style

pynocchio uses a collection of tools to maintain consistent code style. These tools are orchestrated using [pre-commit](https://pre-commit.com/), which can be installed locally to check your changes before opening a PR. The CI process will also run these checks before merging.

To run pre-commit checks locally:

```shell
$ make pre-commit
```

The full list of formatting requirements is specified in the [`.pre-commit-config.yaml`](https://github.com/mstuttgart/pynocchio/blob/main/.pre-commit-config.yaml) file located in the project's root directory.
