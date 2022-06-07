#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import play 
import matplotlib.pyplot as plt
import codemaker1
import codemaker2
import codebreaker0
import codebreaker1
import codebreaker2



def esperance1():
    esp = []    # liste du nombre d'essaies pour chaque partie
    for i in range(500): 
        e = play.play(codemaker1, codebreaker0, True)  #renvoie le nombre d'essaies de la partie
        esp.append(e)
    fig, axis = plt.subplots(figsize = (10, 5)) # mise en forme du graphique
    plt.hist(esp, bins = 200, color='blue', edgecolor='black', linewidth=2)   # histogramme avec 200 barres bleues traduisant les valurs de la liste esp
    
    plt.title('espérance')
    plt.xlabel("nb d'essais")
    plt.ylabel('frequence')
    plt.show()
    
# esperance1()


def esperance2():
    esp1 = []  # liste du nb d'essaie en faisant jouer codebreaker1
    esp0 = []  # liste du nb d'essaie en faisant jouer codebreaker0
    for i in range(500):
        e0 = play.play(codemaker1, codebreaker0, True)
        esp0.append(e0)
        e1 = play.play(codemaker1, codebreaker1, True)
        esp1.append(e1)
    fig, axis = plt.subplots(figsize = (10, 5))
    plt.hist([esp0, esp1], bins = 40, color=['blue', 'red'], edgecolor='black', linewidth=2)    
    
    plt.title('espérance')
    plt.xlabel("nb d'essais")
    plt.ylabel('frequence')
    plt.show()

# esperance2()

def esperance3():
    esp1 = [] # liste du nb d'essaie en faisant jouer codebreaker2
    esp0 = [] # liste du nb d'essaie en faisant jouer codebreaker1
    for i in range(100):
        e0 = play.play(codemaker1, codebreaker1, True)
        esp0.append(e0)
        e1 = play.play(codemaker1, codebreaker2, True)
        esp1.append(e1)
    fig, axis = plt.subplots(figsize = (10, 5))
    plt.hist([esp0, esp1], bins = 40, color=['red', 'green'], edgecolor='black', linewidth=2)    
    
    plt.title('espérance')
    plt.xlabel("nb d'essais")
    plt.ylabel('frequence')
    plt.show()
    
    moyenne = sum(esp1)/100
    print ('moyenne = ', moyenne)
 
# esperance3()

def esperance4(): 
    esp1 = [] # liste du nb d'essaie en faisant jouer codemaker1
    esp2 = [] # liste du nb d'essaie en faisant jouer codemaker2
    for i in range(10):
        e0 = play.play(codemaker1, codebreaker2, True)
        esp1.append(e0)
        e1 = play.play(codemaker2, codebreaker2, True)
        esp2.append(e1)
    fig, axis = plt.subplots(figsize = (10, 5))
    plt.hist([esp1, esp2], color = ['red', 'green'], edgecolor='black', linewidth=2)
    
    plt.title('espérance')
    plt.xlabel("nb d'essais")
    plt.ylabel('frequence')
    plt.show()
    
    
# esperance4()