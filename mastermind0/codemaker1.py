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
    
    sol = [i for i in solution]  # copie utile à la ligne 31 pour modifier la solution copiée sans modifier la vrai variable solution
    
    bp = 0  # Nombre de plots bien placés
    for i in range(len(solution)):
        if solution[i] == combinaison[i]:
            bp += 1
    
    color_ok = 0    # couleurs que l'on retrouve dans la combinaison et dans la solution (bien et mal placés confondues)
    for i in range (len(combinaison)):
        for v in range (len(sol)):
            if combinaison[i] == sol[v]:
                color_ok += 1  
                sol[v] = "," # on remplace les termes déjà vérifiés par des virgules pour ne pas compter une bonne couleur en double et sans avoir d'erreur d'indice
                break
                
     
    mp = color_ok-bp    # le nombre de mal placées correspond au nombre de bonnes couleurs - le nombre de couleurs bien placées
    return(bp, mp)


sol = ["v", "b", "b", "b"]
comb = ["g", "v", "b", "g"]

# print (evaluation(comb, sol))


def codemaker(combinaison):
    """
    Cette fonction corrige la combinaison proposée par le codebreaker
    (donnée en argument) 
    """
    global solution
    return evaluation(combinaison, solution)   
    
