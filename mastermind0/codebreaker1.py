#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import common



def init():
    global prop
    prop = []  # liste des combinaisons déja testée 

def codebreaker(evaluation_p):
    
    combinaison = ''.join(random.choices(common.COLORS, k=common.LENGTH))
    while combinaison in prop :             # on cherche une combinaison qui n'a pas encore été testée
        combinaison = ''.join(random.choices(common.COLORS, k=common.LENGTH))   # tant que la combinaison fait partie de la liste des testées, on en cherche une nouvelle
    prop.append(combinaison)   # ajout de la nouvelle combinaison à la liste des testées 
    return combinaison
     
