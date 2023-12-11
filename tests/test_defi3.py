"""
Test de defi3.py
"""
import models.defi3 as defi3

def test_calculer_score_type():
    """Tester le type que donne l'input"""
    # Créer des instances
    mot1 = "allo"
    mot2 = "bye"
    resultat1 = defi3.calculer_score(mot1)
    resultat2 = defi3.calculer_score(mot2)
    # Implanter les tests
    assert str(type(resultat1)) == "<class 'str'>"
    assert str(type(resultat2)) == "<class 'str'>"

def test_calculer_score_valeur():
    """Tester la valeur que donne l'input"""
    # Créer des instances
    mot1 = "allo"
    mot2 = "bye"
    resultat1 = defi3.calculer_score(mot1)
    resultat2 = defi3.calculer_score(mot2)
    # Implanter les tests
    assert resultat1 == "allo: 4"
    assert resultat2 == "bye: 8"

def test_calculer_score_input():
    """Tester de mauvais inputs"""
    # Créer des instances
    mot1 = ""
    mot2 = "123"
    mot3 = True
    resultat1 = defi3.calculer_score(mot1)
    resultat2 = defi3.calculer_score(mot2)
    resultat3 = defi3.calculer_score(mot3)
    # Implanter les tests
    assert resultat1 == ": 0"
    assert resultat2 == "123: 0"
    assert resultat3 == ": 0"
 