# cicd_test

![Build Status](https://github.com/ugolabo/cicd_test/actions/workflows/ci-build.yaml/badge.svg)

## Description

Tester un CI/CD.

- Implanté avec ci-build.yaml.
	- Consulter le fichier dans le dossier .github/workflows/.
- Consulter le menu Actions dans GitHub; vers la gauche du menu Code.

## Git

- git bash: `git push -u origin main` démarre CI.

## Linter

- flake8.
	- Consulter requirements.txt
- https://www.flake8rules.com/
- https://flake8.pycqa.org/en/latest/index.html
- https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/python/linting/flake8.html
- cmd: `flake8 code.py` ou `python -m flake8 code.py`
- https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/python/linting/pylint.html
- cmd: `pylint code.py` ou `python -m pylint code.py`

## Test unitaires

- Avec Python 3.10+, il faut utiliser pytest (plutôt que nose, nose2, etc.).
	- Consulter requirements.txt
- https://docs.pytest.org/en/7.4.x/
	- Attention à la façon de nommer les dossiers, les fichiers, les fonctions de test dans les fichiers.
- cmd: `pytest -v` à la racine du répertoire du projet pour que pytest découvre le dossier tests/ et les fichiers de tests.
- cmd: `pytest -v --cov=models` ou `pytest --cov=models tests/` avec couverture des tests.
- cmd: `pytest -v --cov=models --cov-report=html` pour produire un report de couverture.

## Répertoire

Avec le commande (cmd) `tree /f` ou `tree` pour les dossiers seulement.

```text
├───.github
│   └───workflows
├───.pytest_cache
│   └───v
│       └───cache
├───models
│   └───__pycache__
└───tests
    └───__pycache__
```
