import json
import mysql.connector

from models import salle
from models.salle import Salle

class DataSalle:
    def get_connection(self):
        with open ('Data/config.json','r') as f:
            config = json.load(f)
        connection = mysql.connector.connect(
            host=config['host'],
            user=config['user'],
            password=config['password'],
            database=config['database']
        )
        return connection

    #creation de la methode insert salle
    def insert_salle(self, salle):
        connection = self.get_connection()
        cursor = connection.cursor()
        query= "INSERT INTO salle (code, description, categorie, capacite) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (salle.code, salle.description, salle.categorie, salle.capacite))
        connection.commit()
        connection.close()

    #ajout de la methode update salle
    def update_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        query = """
        UPDATE salle
        SET description = %s, categorie = %s, capacite = %s
        WHERE code = %s
        """
        cursor.execute(query, (salle.description, salle.categorie, salle.capacite, salle.code))
        conn.commit()
        conn.close()


