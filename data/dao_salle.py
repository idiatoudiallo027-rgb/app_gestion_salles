import json
import mysql.connector
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
