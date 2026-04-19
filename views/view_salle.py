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

#creation du Cadre Infos ainsi que les labels et entry-------------------------------------------------
        self.frame_infos = ctk.CTkFrame(self)
        self.frame_infos.pack(pady=10, padx=10, fill="x")


        self.entry_code = ctk.CTkEntry(self.frame_infos, placeholder_text="Code")
        self.entry_code.pack(pady=5)

        self.entry_description = ctk.CTkEntry(self.frame_infos, placeholder_text="Description")
        self.entry_description.pack(pady=5)

        self.entry_categorie = ctk.CTkEntry(self.frame_infos, placeholder_text="Catégorie")
        self.entry_categorie.pack(pady=5)

        self.entry_capacite = ctk.CTkEntry(self.frame_infos, placeholder_text="Capacité")
        self.entry_capacite.pack(pady=5)

# le Cadre des  Actions ------------------------------------------------------------------
