from os import system, name 
from time import sleep 
from random import randint
from copy import deepcopy
  
class Cellule() :
    def __init__(self):
        self.symbole = "O"

    def survie(self,plateau, colonne, case) :
        self.compteur = 0
        testCo = -1
        while testCo < 2 :
            testCa = -1
            while testCa < 2 :
                if self.test(plateau, colonne, case, testCo,testCa) == True :
                    self.compteur += 1
                testCa += 1
            testCo += 1
        if self.compteur == 2 or self.compteur == 3 :
            return True
        else :
            return False

    def test(self,plateau, colonne, case, testCo,testCa) :
        try :
            if plateau[colonne+testCo][case+testCa].symbole == "O" :
                if colonne+testCo != colonne or case+testCa != case :
                    if (colonne+testCo >= 0 and case+testCa >= 0) :
                        return True
            return False
        except :
            return False

class Vide() :
    def __init__(self):
        self.symbole = " "
    def naissance(self,plateau, colonne, case) :
        compteur = 0
        testCo = -1
        while testCo < 2 :
            testCa = -1
            while testCa < 2 :
                if self.test(plateau, colonne, case, testCo,testCa) == True :
                    compteur += 1
                testCa += 1
            testCo += 1
        if compteur == 3 :
            return True
        else :
            return False

    def test(self,plateau, colonne, case, testCo,testCa) :
        try :
            if plateau[colonne+testCo][case+testCa].symbole == "O" :
                if colonne+testCo != colonne or case+testCa != case :
                    if (colonne+testCo >= 0 and case+testCa >= 0) :
                        return True
            return False
        except :
            return False

def mode(plateau) :
    while 1 :
        entree = input("Entrer R pour un générateur random ou D pour définir vous meme l'emplacement des cellules : ")
        if entree == "R" :
            return generationCellule(plateau)
        elif entree == "D" : 
            return placementCellule(plateau)
        print("Saisie invalide")


def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear') 

def affichagePlateau(plateau) :
    clear()
    contour(len(plateau))
    for hauteur in range(len(plateau[0])) :
        print("|",end='')
        for colonnes in range(len(plateau)) :
            print(plateau[colonnes][hauteur].symbole,end='')
        print("|")
    contour(len(plateau))


def contour(taille) :
    for case in range(taille+2) :
        print("-",end='')
    print()

def affichagePlacementCellule(plateau) :
    clear()
    print(" ",end='')
    for case in range(len(plateau)+1) :
        print(" ",end='')
        print(case%10,end='')

    print()
    affichagePlateauPlacement(plateau)

def affichagePlateauPlacement(plateau) :
    contourPlacement(len(plateau))
    for hauteur in range(len(plateau[0])) :
        print(hauteur%10,end='')
        print("|",end='')
        for colonnes in range(len(plateau)) :
            print(plateau[colonnes][hauteur].symbole,end='')
            print(" ",end='')
        print("|")
    contourPlacement(len(plateau))

def contourPlacement(taille) :
    for case in range(taille+1) :
        print("-",end='')
        print(" ",end='')
    print()


def taillePlateau() :
    while True :
        try :
            taille = int(input("Entrer la taille du plateau : "))
            return taille
        except :
            print("Entrer un taille valide")
            continue


def generationPlateau(taille) :
    plateau = []
    for longueur in range(taille*3) :
        plateau.append([])
        for case in range(taille) :
           plateau[longueur].append(Vide())
    return plateau

def generationCellule(plateau) :
    for colonnes in range(len(plateau)) :
        nb_cellules = randint(0,len(plateau[colonnes]))
        for i in range(nb_cellules) :
            plateau[colonnes][randint(0,len(plateau[colonnes])-1)] = Cellule()
    return plateau

def placementCellule(plateau) :
    while 1 :
        affichagePlacementCellule(plateau)
        entree = input("Entrer S pour lancer la simulation sinon ecrivez NumColonne:NumLigne pour ajouter/supprimer une cellule dans une case ex: 2:4 : ") 
        if len(entree) >= 3 :
            tab = entree.split(':')
            if len(tab) == 2 :
                try :
                    colonne = int(tab[0])
                    ligne = int(tab[1])
                    if plateau[colonne][ligne].symbole == "O" :
                        plateau[colonne][ligne] = Vide()
                    elif plateau[colonne][ligne].symbole == " " :
                        plateau[colonne][ligne] = Cellule()
                except :
                    pass
        if entree == "S" :
            break
        print("Saisie invalide")
    return plateau

def tourSuivant(plateau, nouveauPlateau) :
    for colonnes in range(len(plateau)) :
        for case in range(len(plateau[colonnes])) :
            if plateau[colonnes][case].symbole == "O" :
                if plateau[colonnes][case].survie(plateau,colonnes,case) == True :
                    nouveauPlateau[colonnes][case] = Cellule()
            else :
                if plateau[colonnes][case].naissance(plateau,colonnes,case) == True :
                    nouveauPlateau[colonnes][case] = Cellule()
    return nouveauPlateau


def main() :
    plateau = generationPlateau(taillePlateau())
    plateauVide = deepcopy(plateau)
    plateau = mode(plateau)
    affichagePlateau(plateau)
    tours = 0
    while 1:
        tours += 1
        if input("Appuyez sur entrez pour continuer, ou ecrivez quelque chose pour mettre fin au jeux ") != "" :
            return
        plateau = deepcopy(tourSuivant(plateau, deepcopy(plateauVide)))
        affichagePlateau(plateau)
        print("Le jeux a effectuer {} génération".format(tours))
main()
