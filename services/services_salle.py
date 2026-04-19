from data.dao_salle import DataSalle

class ServiceSalle:
    def __init__(self):
        self.dao_salle=DataSalle()

#ajout de la methode ajouter salle , verification des donnees et la capacite qui doit etre > 1
    def ajouter_salle(self, salle):
        if not salle.code or not salle.description or not salle.categorie:
            return False, "toutes les informations sont obligatoires"

        if int(salle.capacite) <1:
            return False, "la capacite doit etre au moins 1"
        try:
            self.dao_salle.insert_salle(salle)
            return True, "Succès : La salle a été ajoutée."
        except Exception as e:
            return False, f"Erreur base de données : {e}"




