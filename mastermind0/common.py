#!/usr/bin/env python3



LENGTH = 4
COLORS = ['R', 'V', 'B', 'J', 'N', 'M', 'O', 'G']
# Notez que vos programmes doivent continuer à fonctionner si on change les valeurs par défaut ci-dessus


def init ():        # cette fonction permet de créer la liste de l'ensemble des combinaisons possible
    global possible  # on met cette liste en variable globale pour pouvoir la réutiliser dans différentes fonctions
    possible = set()
    for c1 in COLORS:
        comb = c1
        for c2 in COLORS:
            comb = c1
            comb += c2
            for c3 in COLORS:
                comb = c1+c2
                comb += c3
                for c4 in COLORS:
                    comb = c1 +c2 +c3
                    comb += c4
                    possible.add(comb)
    return possible
    # print (possible)
    # print (len(possible))
                    
init()

def donner_possible (comb_test, eval_comb):
    import codemaker1
    possible2 = {i for i in possible}   # création d'un set comportant l'ensemble des combinaisons possibles 
    for i in possible :
        if codemaker1.evaluation(i, comb_test) != eval_comb:  # on compare la liste de toutes les possibilités à la combinaison proposée, la solution est forcément présente dans les combinaisons qui ont la meme evaluation que celle proposée par le codebreaker
            possible2.discard(i)    # on enlève du set les combinaisons dont lévaluation est différentes de la combinaison proposée car elles  ne peuvent pas être solution
    possible2.discard(comb_test)  # on enlève la combinaison testée puisqu'elle n'est pas juste
    return possible2 


def maj_possible(combinaisons_possibles, comb_testé, eval_comb):
    import codemaker1
    possible2 = combinaisons_possibles.copy()  # cette copie est utile pour la boucle for : cela permet de modifier la liste des combinaisons possibles et de parcourir dans la boucle for sa copie qui ne sera pas modifiée 
    for i in possible2 :
        if codemaker1.evaluation(i, comb_testé) != eval_comb:  #on compare la liste des possibilités à la combinaison proposée de la même facon que dans sonner_possible
            combinaisons_possibles.discard(i)    # on met à jour la liste des combinaisons possible en supprimant celles qui sont impossible
        # print ('maj des comb = ', possible2)
    combinaisons_possibles.discard(comb_testé)
    return combinaisons_possibles 
    