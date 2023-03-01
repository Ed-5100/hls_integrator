HLSi: HLS ❤️ RTL and SoC system builders
=======================================

Requirements
------------

- Python3: 3.10 or later
- Poetry: to manage virtual environment and dependencies

To install Poetry:

```
curl -sSL https://install.python-poetry.org/ | python3.10 -
```


Installation
------------

You can install HLSi using Poetry:

```
poetry install
```

Usage
-----

Available soon :-).


Contribute
----------

All tests and pre-commit checks shall pass before committing to this repository.  Test coverage shall be checked before committing as well.

If you are installing for development and testing:

```
poetry install --with=dev
```

Before your first commit, you must install pre-commit for Git:

```
poetry run pre-commit install
```

To invoke `pre-commit` without committing the changes:

```
poetry run pre-commit run --all-files
```

To run tests:

```
poetry run pytest
```

To run coverage tests and find code regions that are not covered:

```
poetry run coverage run -m pytest
poetry run coverage report --show-missing
# or `poetry run coverage html` to get html report
```
