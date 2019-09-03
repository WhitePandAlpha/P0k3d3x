filepath = 'PokeDex.txt' #Je donne le chemin d'acces du fichier
pokedex = {} #Je creer le dictionnaire "pokedex"
with open(filepath, 'r') as f : #J'ouvre le fichier de "filepath" 
    ligne = f.readline()
    while ligne :  #Je créer une boucle while afin de de lire ligne par ligne le contenu du fichier

            nom, type = ligne.split() #Je divise chaque ligne du fichier en plusieurs parties
            pokedex[nom] = (type)
            ligne = f.readline()

    print(pokedex)
    
def nom() : #Je creer une fonction afin d'afficher seulement les cles du dictionnaire

    print(pokedex.keys())
    
def type() : #Je creer une fonction afin d'afficher seulement les valeurs du dictionnaire
    
    print(pokedex.values())
    

        


