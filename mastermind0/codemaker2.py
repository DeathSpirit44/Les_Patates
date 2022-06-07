#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
import random
import common

def init():
    """
    Cette fonction, appellée à chaque début de partie, initialise un certain nombre de
    variables utilisées par le codemaker
    """
    global solution
    solution = ''.join(random.choices(common.COLORS, k=common.LENGTH))
 
    
def evaluation (combinaison, solution):
    
    if len(solution) != len(combinaison):
        sys.exit("Erreur : les deux combinaisons n'ont pas la même longueur")
    
    sol = [i for i in solution]
    
    bp = 0  # Nombre de plots bien placés
    for i in range(len(solution)):
        if solution[i] == combinaison[i]:
            bp += 1
    
    color_ok = 0
    for i in range (len(combinaison)):
        for v in range (len(sol)):
            if combinaison[i] == sol[v]:
                color_ok += 1  
                sol[v] = "," #on remplace les termes déjà vérifiés par des virgules pour ne pas avoir d'erreur d'indice
                break
                
    
    mp = color_ok-bp
    return(bp, mp)


sol = ["v", "b", "b", "b"]
comb = ["g", "v", "b", "g"]

# print (evaluation(comb, sol))


def codemaker(combinaison):
    import codebreaker2
    
    taille_liste = 0
    for elt in codebreaker2.combinaison_possible: # boucle for permettant de tester chaque élément encore possible si il était utilisé comme solution
        possible = codebreaker2.combinaison_possible.copy()  
        ev = evaluation(combinaison, elt) 
        liste_possible = common.maj_possible(possible, combinaison, ev) # on met a jour la liste en prenant comme nouvelle solution l'élément elt de la lisye des possibles
        if len (liste_possible) >= taille_liste:   # permet de comparer les tailles des nouvelles listes pour chaque nouvelle solution
            taille_liste = len(liste_possible)
            newsolution = elt                       # on ne garde que lélément dont la taille de la liste maj est la plus grande
    return evaluation(combinaison, newsolution)

"""
Description du raisonnement et de la démarche:
    pour chaque élément de la liste des combinaisons encore possibles, on teste la taille de la liste si elle était réduite 
    en comparant la combinaison propoposée par le codebreaker et cet élément s'il était solution.
    On garde alors l'élément dont la liste est le moins réduite si on le prend comme nouvelle solution.
    Cela permet ainsi d'augmenter le temps que met le codebreaker à trouver la bonne solution.
""" 


