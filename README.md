# cicd_test

![Build Status](https://github.com/ugolabo/devops-capstone-project/actions/workflows/ci-build.yaml/badge.svg)

## Description

Tester un CI/CD.

## Git

- `git push -u origin main` démarre CI.
- Consulter le menu Actions dans GitHub; vers la gauche du menu Code, dans un repo.

## Linter

- flake8 implanté avec ci-build.yaml dans le dossier .github/ comme CI.
	- Consulter requirements.txt
- https://www.flake8rules.com/
- `flake8 code.py` ou `python -m flake8 code.py`

## Test unitaires

- Avec Python 3.10+, il faut utiliser pytest (plutôt que nose, nose2, etc.).
	- Consulter requirements.txt
- https://docs.pytest.org/en/7.4.x/
	- Attention à la façon de nommer les dossiers, les fichiers, les fonctions de test dans les fichiers.
- `pytest -v` à la racine du répertoire du projet pour que pytest découvre le dossier tests/ et les fichiers de tests.
- `pytest -v --cov=models` ou `pytest --cov=models tests/` avec couverture des tests.
- `pytest -v --cov=models --cov-report=html` pour produire un report de couverture.

## Répertoire

Avec le commande (sur cmd) `tree /f`

```text
│   .gitignore
│   défi3.py
│   model.py
│   notes.txt
│   README.md
│   requirements.txt
│
└───.github
    └───workflows
            ci-build.yaml
```