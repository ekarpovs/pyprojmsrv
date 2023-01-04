[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![ci-cd](https://github.com/ekarpovs/pyprojmsrv/actions/workflows/ci-cd.yaml/badge.svg)](https://github.com/ekarpovs/pyprojmsrv/actions/workflows/ci-cd.yaml)

# Python seed project for microservices (pyprojmsrv)

## Project structure
````bash
├── docs
├── .github
│   └── workflows
│       └── ci-cd.yaml
├── pyprojmsrv
│       ├── __init__.py
│       └── msrv.py
├── tests
│   ├── __init__.py
│   └── test_pyprojmsrv.py
├── .coveragerc
├── .gitignore
├── LICENSE
├── .pre-commit-config.yaml
├── pyproject.toml
├── README.md
├── requirements.in
└── setup.py
````

### [Pre-commit-hooks](https://pre-commit.com/):

- [Remote](https://github.com/pre-commit/pre-commit-hooks)
    - trailing-whitespace - Trims trailing whitespace.
    - end-of-file-fixer - Ensures that a file is either empty, or ends with one newline.
    - check-yaml - Checks yaml files for parseable syntax.
    - check-added-large-files - Prevents giant files from being committed.

- [Local](https://github.com/ekarpovs/pyprojmsrv):
    - black - Formats(reformats) code based on the Black's code style guide (close to PEP-8).
    - pylint - Analizes the python code
    - pytest - Tests (unit tests) code
    - coverage - Creates coverage report
    - coverage-html - Creates coverage report in html formal
    - pip-compile - Produces requirements.txt with the modules listed in requirements.in and the transitive dependencies of those modules.

```bash
# run pre-commit hooks from the command line
pre-commit run --all-files -v

# run coverage && pytest from the command line
coverage run --source=src -m pytest -v tests && coverage report -m  && coverage html
````

```bash
# run pre-commit hooks from the command line
pre-commit run --all-files -v

# run coverage && pytest from the command line
coverage run --source=src -m pytest -v tests && coverage report -m  && coverage html

# open coverage html report in a default browser
xdg-open ./htmlcov/index.html
````


### [GitHib Actions](https://github.com/actions):

- [Local](https://github.com/ekarpovs/pyprojmsrv/):
    - ci-cd
