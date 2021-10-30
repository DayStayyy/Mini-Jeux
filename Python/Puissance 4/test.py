import os 	

class Joueur(object):

	def __init__(self, nom, symbole):
		self.nom = nom
		self.symbole = symbole

#init variables
joueur_tours = 1
etage = 0
nb = 0

#init liste
colonne_0 = [" ", " ", " ", " ", " ", " "]
list_joueur	= []
list_colonne=[]


list_etage = [etage,etage,etage,etage,etage,etage,etage]






print (" 1 2 3 4 5 6 7 \n"
	   "|",list_colonne[0][5],"|",list_colonne[1][5],"|",list_colonne[2][5],"|",list_colonne[3][5],"|",list_colonne[4][5],"|",list_colonne[5][5],"|",list_colonne[6][5],"|""\n"
	   "|",list_colonne[0][4],"|",list_colonne[1][4],"|",list_colonne[2][4],"|",list_colonne[3][4],"|",list_colonne[4][4],"|",list_colonne[5][4],"|",list_colonne[6][4],"|""\n"
	   "|",list_colonne[0][3],"|",list_colonne[1][3],"|",list_colonne[2][3],"|",list_colonne[3][3],"|",list_colonne[4][3],"|",list_colonne[5][3],"|",list_colonne[6][3],"|""\n"
	   "|",list_colonne[0][2],"|",list_colonne[1][2],"|",list_colonne[2][2],"|",list_colonne[3][2],"|",list_colonne[4][2],"|",list_colonne[5][2],"|",list_colonne[6][2],"|""\n"
	   "|",list_colonne[0][1],"|",list_colonne[1][1],"|",list_colonne[2][1],"|",list_colonne[3][1],"|",list_colonne[4][1],"|",list_colonne[5][1],"|",list_colonne[6][1],"|""\n"
	   "|",list_colonne[0][0],"|",list_colonne[1][0],"|",list_colonne[2][0],"|",list_colonne[3][0],"|",list_colonne[4][0],"|",list_colonne[5][0],"|",list_colonne[6][0],"|""\n"
)



message = "Joueur ou voulez vous placez votre pion ? (ex: 3) "
emplacement = input(message)
		
emplacement = int(emplacement)

if emplacement > 0 and emplacement < 8 :
	emplacement -= 1
				
if list_colonne[emplacement][5] != " " :
	print("gnagnagna")
else : 
	("wesh")
			




list_colonne[1][5] = "0"
print (list_colonne[1][5])
list_etage[emplacement] += 1
	


print (" 1 2 3 4 5 6 7 \n"
	   "|",list_colonne[0][5],"|",list_colonne[1][5],"|",list_colonne[2][5],"|",list_colonne[3][5],"|",list_colonne[4][5],"|",list_colonne[5][5],"|",list_colonne[6][5],"|""\n"
	   "|",list_colonne[0][4],"|",list_colonne[1][4],"|",list_colonne[2][4],"|",list_colonne[3][4],"|",list_colonne[4][4],"|",list_colonne[5][4],"|",list_colonne[6][4],"|""\n"
	   "|",list_colonne[0][3],"|",list_colonne[1][3],"|",list_colonne[2][3],"|",list_colonne[3][3],"|",list_colonne[4][3],"|",list_colonne[5][3],"|",list_colonne[6][3],"|""\n"
	   "|",list_colonne[0][2],"|",list_colonne[1][2],"|",list_colonne[2][2],"|",list_colonne[3][2],"|",list_colonne[4][2],"|",list_colonne[5][2],"|",list_colonne[6][2],"|""\n"
	   "|",list_colonne[0][1],"|",list_colonne[1][1],"|",list_colonne[2][1],"|",list_colonne[3][1],"|",list_colonne[4][1],"|",list_colonne[5][1],"|",list_colonne[6][1],"|""\n"
	   "|",list_colonne[0][0],"|",list_colonne[1][0],"|",list_colonne[2][0],"|",list_colonne[3][0],"|",list_colonne[4][0],"|",list_colonne[5][0],"|",list_colonne[6][0],"|""\n")


		



	



os.system("pause")
