"""from data.dao_salle import DataSalle
from models.salle import Salle
dao = DataSalle()
conn = dao.get_connection()

if conn.is_connected():
    print("la connexion a ete effecute avec succe")

#ajouter une salle--------------------------------------------------------------------------------
s= Salle("12C","generale","Classe",24)
dao.insert_salle(s)

# partie update salle----------------------------------------------------------------------------
s.capacite = 38
dao.update_salle(s)
print("mis a jour effectue")

#ajout de la methode delete ----------------------------------------------------------------------
dao.delete_salle("12A")
print("suppression effectue avec succes")

# rechercher une salle a partir de son code
s= dao.get_salle("12C")
if s:
    print(f"\nSalle trouvée : {s.description}")

# recuperation de toutes les salles de la base de donnee
print("\n--- Liste de toutes les salles ---")
toutes = dao.get_salles()
for s in toutes:
    s.afficher_infos() """

#j'ai commenter la premiere partie en haut afin de tester mes fonction que j;ai creer dans services
from models.salle import Salle
from services.services_salle import  ServiceSalle

serv= ServiceSalle()
print("--------test de la couche services pour l'ajout ----------------------")
s1 = Salle("C303", "Laboratoire Multimédia", "Informatique", 12)
succes, message = serv.ajouter_salle(s1)
print(f"Ajout C303 : {message}")


print("--------test de la couche services pour rechercher  -----------------")
print("\nRecherche C303 :")
salle = serv.rechercher_salle("C303")
if salle:
    salle.afficher_infos()

print("--------test de la couche services pour modifier  -------------------")
s = serv.rechercher_salle("C303")

if s:
    s.categorie = "Biologie"
    success, message = serv.modifier_salle(s)
    print(message)

print("--------test de la couche services pour afficher   -------------------")
print("\nListe des salles :")
for salle in serv.recuperer_salles():
    salle.afficher_infos()


