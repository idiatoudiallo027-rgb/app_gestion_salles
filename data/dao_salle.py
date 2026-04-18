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
        try:
            conn = self.get_connection()
            cursor = conn.cursor()

            query = "INSERT INTO salle (code, description, categorie, capacite) VALUES (%s, %s, %s, %s)"
            cursor.execute(query, (salle.code, salle.description, salle.categorie, salle.capacite))
            conn.commit()
            conn.close()

            print("la Salle est  ajoutée avec succes ")
        except Exception as e:
            print("Erreur :", e)


#ajout de la methode update salle--------------------------------------------------------------------
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

# ajout de la methide delete--------------------------------------------------
    def delete_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor()

        query = "DELETE FROM salle WHERE code = %s"
        cursor.execute(query, (code,))

        conn.commit()
        conn.close()
#rechercher et retourner une salle a partir de son code -----------------------------------------
    def get_salle(self, code):
        conn = self.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM salle WHERE code = %s"
        cursor.execute(query, (code,))
        r = cursor.fetchone()
        cursor.close()
        conn.close()

        if r:
            return Salle(r['code'], r['description'], r['categorie'], r['capacite'])
        return None