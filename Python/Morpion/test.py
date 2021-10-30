import os

#init variables
boucle_principale = 1
boucle_coordonnes = 1
modif = 0
joueur_tours = 2
a = 2
suite = 0

#init lignes
ligne_1 = [" ", " ", " "]
ligne_2 = [" ", " ", " "]
ligne_3 = [" ", " ", " "]
list_ligne = [ligne_1, ligne_2, ligne_3]
list_joueur = []
coord_list = []

class Joueur(object):

	def __init__(self, nom, symbole):
		self.nom = nom
		self.symbole = symbole


nom = input("Quel est le nom du premier joueur ? ")
joueurs = Joueur(nom, "O")
list_joueur.append(joueurs)
nom = input("Quel est le nom du deuxieme joueur ? ")
joueurs = Joueur(nom, "X")
list_joueur.append(joueurs)

print ("  A   B   C ")
print ("#############")
print ("#", list_ligne[0][0], "|", list_ligne[0][1], "|", list_ligne[0][2], "# 1")
print ("#", list_ligne[1][0], "|", list_ligne[1][1], "|", list_ligne[1][2], "# 2")
print ("#", list_ligne[2][0], "|", list_ligne[2][1], "|", list_ligne[2][2], "# 3")
print ("#############")





if joueur_tours == 2 :
	joueur_tours = 0
	boucle = 2
if joueur_tours == 0 :
	joueur_tours = 1
	boucle = 2	
if joueur_tours == 1 :
	joueur_tours = 0
	boucle = 2
			
message = "Joueur " + list_joueur[joueur_tours].nom + " ou voulez vous placez votre symbole ? (ex: A3) "
coord = input(message)
coord = str(coord)
coord = coord.lower()

for i in coord :
	coord_list.append(i)



if coord_list[0] == "a" :
	coord_list[0] = 0

elif coord_list[0] == "b" :
		coord_list[0] = 1

elif coord_list[0] == "c" :
	coord_list[0] = 2

coord_list[1] = int(coord_list[1])
coord_list[1] -= 1


print(list_ligne[coord_list[1]][coord_list[0]])
if list_ligne[coord_list[1]][coord_list[0]] == " " :
	print("gg")


list_ligne[coord_list[1]][coord_list[0]] = list_joueur[joueur_tours].symbole

print ("  A   B   C ")
print ("#############")
print ("#", list_ligne[0][0], "|", list_ligne[0][1], "|", list_ligne[0][2], "# 1")
print ("#", list_ligne[1][0], "|", list_ligne[1][1], "|", list_ligne[1][2], "# 2")
print ("#", list_ligne[2][0], "|", list_ligne[2][1], "|", list_ligne[2][2], "# 3")
print ("#############")
