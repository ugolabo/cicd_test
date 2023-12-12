# cicd_test

![Build Status](https://github.com/ugolabo/cicd_test/actions/workflows/ci-build.yaml/badge.svg)

## Description

Tester un CI sur Github (la 1re partie d'un CI/CD).

- Le projet est un code source Python à une fonction qui calcule la valeur d'un mot selon la valeur des lettres du Scrabble.
- Le code source est accompagné d'un autre code source pour faire les tests unitaires.
- Le CI est automatisé par un fichier ci-build.yaml qui déclenche le processus de CI.
	- Consulter le fichier dans le dossier .github/workflows/.
	- Consulter le menu Actions dans GitHub; vers la gauche du menu Code.
- Il n'y a pas de 2e partie (CD d'un CI/CD), car le projet ne se prête pas à un déploiement. Ce n'est pas un site web, une application mobile, un API ou un projet interactif.
	
## Répertoire

Avec les commandes (dans cmd) `tree /f` ou `tree` pour les dossiers seulement.

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

## Git

- Avec le Git bash: `git push -u origin main` pour démarrer le CI.
	- Consulter le fichier .github/workflows/ci-build.yaml pour le démarrage.

## ci-build.yaml

- Nom (`name`) du CI: CI Build
- Démarrage (`on`) du CI:
	- `git push` vers la branche main.
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
	- Il n'y a pas d'étapes pour déployer vers un cloud ou autre (CD), car le projet ne se prête pas à un déploiement. Ce n'est pas un site web, une application mobile, un API ou un projet interactif.

### Linting

- Avant le CI, le linting est fait avec les modules flake8 et pylint.
- `flake8 code.py` ou `python -m flake8 code.py`.
	- https://www.flake8rules.com/
	- https://flake8.pycqa.org/en/latest/index.html
	- https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/python/linting/flake8.html
- `pylint code.py` ou `python -m pylint code.py`.
- https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/python/linting/pylint.html
- Avec le CI, le linting est automatisé.
	- Consulter requirements.txt pour l'installation.
	- Consulter le fichier .github/workflows/ci-build.yaml pour le démarrage.

## Tests unitaires

- Avant le CI, les tests unitaires sont faits avec le module pytest.
	- Avec Python 3.10+, il faut utiliser le module pytest plutôt que nose, nose2, etc.
- `pytest -v` à la racine du répertoire du projet pour que pytest découvre le dossier tests/ et les fichiers de tests.
- `pytest -v --cov=models` ou `pytest --cov=models tests/` avec la couverture des tests.
- `pytest -v --cov=models --cov-report=html` pour produire un report de couverture des tests.
	- https://docs.pytest.org/en/7.4.x/
	- Attention à la façon de nommer les dossiers, les fichiers, les fonctions de test dans les fichiers.
- Avec le CI, les tests unitaires sont automatisés.
	- Consulter requirements.txt pour l'installation.
	- Consulter le fichier .github/workflows/ci-build.yaml pour le démarrage.
