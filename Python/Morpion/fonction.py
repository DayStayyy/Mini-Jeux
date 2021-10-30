

#init lignes
ligne_1 = [" ", " ", " "]
ligne_2 = [" ", " ", " "]
ligne_3 = [" ", " ", " "]
list_ligne = [ligne_1, ligne_2, ligne_3]
list_joueur = []


def sys_nom() :
	nom = input("Quel est le nom du premier joueur ? ")
	joueurs = Joueur(nom, "O")
	list_joueur.append(joueurs)
	nom = input("Quel est le nom du deuxieme joueur ? ")
	joueurs = Joueur(nom, "X")
	list_joueur.append(joueurs)

def sys_tours(boucle, joueur_tours) :

if joueur_tours == 2 :
	joueur_tours = 0
	boucle = 2
if joueur_tours == 0 :
	joueur_tours = 1
	boucle = 2
if joueur_tours == 1 :
	joueur_tours = 0
	boucle = 2

def sys_demande() :

	coord = input("Joueur", list_joueur[sys_tours.joueur_tours].nom , "ou voulez vous placez votre symbole ? (ex: A3)")


def sys_coord(coord) :
	
	while 1==1 :
		coord = coord.minimise

		coord = list(coord)
		if  len(list) > 2 :
			print("Veuillez entre seulement deux coordonnées")
			break

		if coord[0] != "a" and coord[0] != "b" and coord[0] != "c" :
			print("Veuillez entre A,B ou C en premier")
			break

		if coord[1] != "1" and coord[1] != "2" and coord[1] != "3" :
			print("Veuillez entre 1,2 ou 3 en deuxieme")
			break

		if coord[0] == "a" :
			coord[0] = 0

		elif coord[0] == "b" :
			coord[0] = 1

		elif coord[0] == "c" :
			coord[0] = 2

		coord[1] = int(coord[1]) 
		sys_ligne()

def sys_ligne() :
	
	while  1==1:
		if list_ligne[coord[1]][coord[0]] == " " :
			list_ligne[coord[1]][coord[0]] = list_joueur[joueur_tours].symbole
			boucle_coordonnes = 0
		else :
			print ("L'emplacement choisi est deja utilisé")
			break


def sys_affichage() :
	print (" A B C ")
	print ("#############")
	print ("#", list_ligne[0][0], "|", list_ligne[0][1], "|", list_ligne[0][2], "# 1")
	print ("#", list_ligne[1][0], "|", list_ligne[1][1], "|", list_ligne[1][2], "# 2")
	print ("#", list_ligne[2][0], "|", list_ligne[2][1], "|", list_ligne[2][2], "# 3")
	print ("#############")


class Joueur(object):

	def __init__(self, nom, symbole):
		self.nom = nom
		self.symbole = symbole

