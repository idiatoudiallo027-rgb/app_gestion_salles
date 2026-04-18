from data.dao_salle import DataSalle
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
    s.afficher_infos()



