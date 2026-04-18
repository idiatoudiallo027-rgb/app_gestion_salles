class Salle:
    def __init__(self,code, description, categorie, capacite):
        self.code = code
        self.description = description
        self.categorie = categorie
        self.capacite = capacite
    def afficher_infos(self):
        print("Details de la  Salle")
        print(f"Code :{self.code}")
        print(f"Description :{self.description}")
        print(f"Categorie:{self.categorie}")
        print(f"Capacite: {self.capacite} places ")
