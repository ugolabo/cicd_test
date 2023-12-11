"""
Test de defi3.py
"""
import models.defi3 as defi3

def test_calculer_score():
    """Retourne le mot et sa valeur"""
    # Créer une instance
    mot = "allo"
    resultat = defi3.calculer_score(mot)
    # Implanter les tests
    assert str(type(resultat)) == "<class 'str'>"
    assert resultat == "allo: 4"