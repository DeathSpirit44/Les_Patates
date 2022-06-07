#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import codemaker1

def check_codemaker(log): 
    try:        # le try permet d'eviter une erreur si jamais le fichier n'existe pas
        with open (log + ".txt", 'r') as log :  # on ouvre le fichier en mode lecture
            codebreaker = log.readlines()       # transformation en liste des éléments du fichier pour pouvoir les utiliser par la suite
            # print (codebreaker, solution)
          
            solution = codebreaker[-2].strip()   # le .strip() permet de suprimer le \n des éléments provenant du fichier texte
            
            for i in range (len(codebreaker)//2):   # on teste pour chaque combinaison proposée que l'evaluation soit cohérente avec la solution finale
                test = codemaker1.evaluation(codebreaker[2*i].strip(), solution)
                test = str(test[0]) + "," + str(test[1])
                if test != codebreaker[2*i+1].strip(): 
                    print ("Le codemaker est un tricheur")
                    return False
                
            print ("Tout va bien") 
            return True
            
    except Exception:  # si  le fichier n'existe pas, on renvoie False
        print ("fichier introuvable : " + log)
        return None 
        
                

check_codemaker("fkldjq")
        