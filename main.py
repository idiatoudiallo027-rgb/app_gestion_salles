from data.dao_salle import DataSalle

dao = DataSalle()
conn = dao.get_connection()

if conn.is_connected():
    print("la connexion a ete effecute avec succe")