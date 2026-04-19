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

# le Cadre des  Actions  ------------------------------------------------------------------
        self.frame_actions = ctk.CTkFrame(self)
        self.frame_actions.pack(pady=10)

# Boutons (SANS command= pour l'instant)
        self.btn_ajouter = ctk.CTkButton(self.frame_actions, text="Ajouter")
        self.btn_ajouter.pack(side="left", padx=5)

        self.btn_modifier = ctk.CTkButton(self.frame_actions, text="Modifier")
        self.btn_modifier.pack(side="left", padx=5)

        self.btn_supprimer = ctk.CTkButton(self.frame_actions, text="Supprimer")
        self.btn_supprimer.pack(side="left", padx=5)

        self.btn_rechercher = ctk.CTkButton(self.frame_actions, text="Rechercher")
        self.btn_rechercher.pack(side="left", padx=5)