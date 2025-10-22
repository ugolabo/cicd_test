# CI/CD: fichier Python, linting et tests unitaires

![Build Status](https://github.com/ugolabo/cicd_test/actions/workflows/ci-build.yaml/badge.svg)

Le projet implante la 1re partie (CI) d'un processus CI/CD en Python.

<img src="img/cicd_python_linting_tests.jpg" alt="" width="800px">

## Mise en place et structure

1. Cloner le repo sur son ordinateur.
1. Le projet fonctionne en Python 3.11.
1. Installer les modules du fichier 'requirements.txt'. Le fichier est à la racine du projet.


### Organisation du répertoire

Le projet utilise une structure pour séparer le code source du code source de tests unitaires avec le module pytest, les résultats des tests et le YAML du CI.

```
───cicd_python_linting_pytest
    ├── .github
    │   └── workflows
    ├── img
    ├── models
    └── tests
```

- Tester manuellement le processus en local avant d'automatiser le processus sur GitHub.
- Le code source ('models/defi3.py') à une fonction calcule la valeur d'un mot selon la valeur des lettres du Scrabble.
- Le code source de test ('tests/test_defi3.py') fait les tests unitaires avec pytest.
- Le CI est automatisé par un fichier '.github/workflows/ci-build.yaml' qui déclenche le processus CI/CD.
	- Consulter le menu Actions dans GitHub; vers la gauche du menu Code.
- Il n'y a pas la 2e partie (CD) d'un processus CI/CD, car le projet ne se prête pas à un déploiement. Ce n'est pas un site web ni une application mobile, par exemple.
-  `git push -u origin main` démarrer le processus CI/CD.
	- Consulter le fichier '.github/workflows/ci-build.yaml' pour le démarrage.

### 'ci-build.yaml'

- Nom (`name`) du CI: CI Build
- Démarrage (`on`) du CI:
	- `git push -u origin main`.
	- pull request suivi d'un merge avec la branche main.
	- Autres actions: https://docs.github.com/en/actions
	- Autres actions: https://github.com/actions
- Exécution de tâche (`jobs`):
	- Construire (`build`) un serveur Ubuntu pour exécuter (`run-on`) la suite; la machine virtuelle ou VM.
	- Construire (`build`) un container Python; le logiciel.
	- Étapes (`steps`):
		- `actions/checkout@v3`
			- https://github.com/actions/checkout, action.yml.
		- Installer les modules Python ou les dépendances.
		- Exécuter le linting avec le module flake8 uniquement.
		- Exécuter les tests unitaires avec le module pytest.
	- Il n'y a pas d'étapes pour déployer vers un cloud ou autre (CD), car le projet ne se prête pas à un déploiement.

### Linting

- Avant le CI, le linting est déclenché manuellement avec les modules flake8 et Pylint.
- `flake8 code.py` ou `python -m flake8 code.py`.
	- https://pypi.org/project/flake8/
	- https://www.flake8rules.com/
	- https://flake8.pycqa.org/en/latest/index.html
	- https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/python/linting/flake8.html
- `pylint code.py` ou `python -m pylint code.py`.
	- https://pypi.org/project/pylint/
	- https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/python/linting/pylint.html
- Avec le CI, le linting avec flake8 seulement est automatisé.

### Tests unitaires

- Avant le CI, les tests unitaires sont déclenchés manuellement avec le module pytest.
	- Avec Python 3.10+, il faut utiliser le module pytest (plus moderne, plus large communauté, capable de faire des tests d'intégration) plutôt que les modules nose et nose2 qui bonifient le module unittest.
- `pytest -v` à la racine du répertoire du projet pour que pytest découvre le dossier 'tests' et les fichiers de tests.
- `pytest -v --cov=models` ou `pytest --cov=models tests/` ajoute la couverture des tests.
- `pytest -v --cov=models --cov-report=html` ajoute la couverture des tests et produit un report de couverture des tests.
	- https://pypi.org/project/pytest/
	- Attention à la façon de nommer les dossiers, les fichiers, les fonctions de test dans les fichiers.
- Avec le CI, les tests unitaires sont automatisés.
