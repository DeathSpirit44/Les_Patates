#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import common


def init():
    # il n'y a plus besoin de vérifier que le codebraker teste 2 fois la meme 
    # solution puisque les combinaisons sont supprimées si elle sont testées
    global combinaison_possible
    combinaison_possible = common.init()  # création d'une liste avec toutes les solutions
    
    

def codebreaker(evaluation_p):
    #print (codemaker1.solution)
    global combinaison 
    
    if evaluation_p == None:    # première tour du codebreaker 
        combinaison = ''.join(random.choices(common.COLORS, k=common.LENGTH))
    else :
        possible2 = common.maj_possible(combinaison_possible, combinaison, evaluation_p)  # maj de la liste des combinaisons encore possibles en fct de la combinaison précédente et de son eval
        # print('possible2 = ', possible2)
        combinaison = random.sample(possible2,1)[0]  # choix dans la liste mise à jour
        
    return combinaison
     