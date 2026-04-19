import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle

#creation de la classe viewSalle
class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("GESTION DES SALLES ")
        self.geometry("800x600")
        self.services_salle = ServiceSalle()