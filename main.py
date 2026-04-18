from data.dao_salle import DataSalle
from models.salle import Salle
dao = DataSalle()
conn = dao.get_connection()

if conn.is_connected():
    print("la connexion a ete effecute avec succe")

#ajouter une salle
s= Salle("12A","Salle Reunion","Classe",24)

