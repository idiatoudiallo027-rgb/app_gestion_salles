import customtkinter as ctk
from tkinter import ttk, messagebox
from services.services_salle import ServiceSalle
from models.salle import Salle

#creation de la class viewSalle
class ViewSalle(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.service_salle = ServiceSalle()
        self.title("GESTION DES SALLES ")
        self.geometry("800x600")


#creation du Cadre Infos ET  les labels et entry-------------------------------------------------
        self.frame_infos = ctk.CTkFrame(self)
        self.frame_infos.pack(pady=10, padx=10, fill="x")

        self.entry_code = ctk.CTkEntry(self.frame_infos, placeholder_text="Code")
        self.entry_code.pack(pady=5)

        self.entry_description = ctk.CTkEntry(self.frame_infos, placeholder_text="Description")
        self.entry_description.pack(pady=5)

        self.entry_categorie = ctk.CTkEntry(self.frame_infos, placeholder_text="Categorie")
        self.entry_categorie.pack(pady=5)

        self.entry_capacite = ctk.CTkEntry(self.frame_infos, placeholder_text="Capacite")
        self.entry_capacite.pack(pady=5)

# le Cadre des  Actions  ------------------------------------------------------------------
        self.frame_actions = ctk.CTkFrame(self)
        self.frame_actions.pack(pady=10)

#ajout du cadre de la liste des salles
        #Cadre List des salles--------------------------------------------------
        self.cadreList = ctk.CTkFrame(self, corner_radius=10, width=400)
        self.cadreList.pack(pady=10, padx=10, fill="both", expand=True)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "description", "categorie", "capacite"),
            show="headings"
        )

        # En-têtes-----
        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacite")

        # la dimension des colonnes
        self.treeList.column("code", width=80,)
        self.treeList.column("description", width=150)
        self.treeList.column("categorie", width=120)
        self.treeList.column("capacite", width=100)

        self.treeList.pack(expand=True, fill="both", padx=10, pady=10)

# Boutons (SANS command= pour le moment, apres cela je l'ai  ajouter)
        self.btn_ajouter = ctk.CTkButton(self.frame_actions, text="Ajouter", fg_color="green", font=("Arial", 20))
        self.btn_ajouter.configure(command=self.ajouter_salle)
        self.btn_ajouter.grid(row=0, column=0, padx=10, pady=10)

        self.btn_modifier = ctk.CTkButton(self.frame_actions, text="Modifier", fg_color="orange", font=("Arial", 20))
        self.btn_modifier.configure(command=self.modifier_salle)
        self.btn_modifier.grid(row=0, column=1, padx=10, pady=10)

        self.btn_supprimer = ctk.CTkButton(self.frame_actions, text="Supprimer", fg_color="red", font=("Arial", 20))
        self.btn_supprimer.configure(command=self.supprimer_salle)
        self.btn_supprimer.grid(row=0, column=2, padx=10, pady=10)

        self.btn_rechercher = ctk.CTkButton(self.frame_actions, text="Rechercher",fg_color="blue", font=("Arial", 20))
        self.btn_rechercher.configure(command=self.rechercher_salle)
        self.btn_rechercher.grid(row=0, column=3, padx=10, pady=10)

        self.lister_salles()

#la fonction vider_champs---------------------------------------------------
    def vider_champs(self):
        self.entry_code.delete(0, "end")
        self.entry_description.delete(0, "end")
        self.entry_categorie.delete(0, "end")
        self.entry_capacite.delete(0, "end")

# fonction ajouter --------------------------------------------------------------------------
    def ajouter_salle(self):
        try:
            code = self.entry_code.get()
            description = self.entry_description.get()
            categorie = self.entry_categorie.get()
            capacite = int(self.entry_capacite.get())
            salle = Salle(code, description, categorie, capacite)
            ok, message = self.service_salle.ajouter_salle(salle)
            if ok:
                messagebox.showinfo("Succès", message)
                self.vider_champs()
                self.lister_salles()
            else:
                messagebox.showerror("Erreur", message)
        except ValueError:
            messagebox.showerror("Erreur", "veuillez saisir un nombre entier .")


#fonction modifier----------------------------------------------------------------------
    def modifier_salle(self):
        try:
            code = self.entry_code.get()
            description = self.entry_description.get()
            categorie = self.entry_categorie.get()
            capacite = int(self.entry_capacite.get())
            salle = Salle(code, description, categorie, capacite)
            ok, message = self.service_salle.modifier_salle(salle)
            if ok:
                messagebox.showinfo("Succès", message)
                self.vider_champs()
                self.lister_salles()
            else:

                messagebox.showerror("Erreur", message)
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier .")


#fonction supprimer ------------------------------------------------------------------------------
    def supprimer_salle(self):
        code = self.entry_code.get()
        if not code:
            messagebox.showerror("Erreur", "saisissez le code de la salle.")
            return
        ok, message = self.service_salle.supprimer_salle(code)
        if ok:
            messagebox.showinfo("Succès", message)
            self.vider_champs()
            self.lister_salles()
        else:
            messagebox.showerror("Erreur", message)


#fonction rechercher-----------------------------------------------------------------------------
    def rechercher_salle(self):
        code = self.entry_code.get()
        if not code:
            messagebox.showerror("Erreur", "Veuillez saisir le code de la salle.")
            return
        salle = self.service_salle.rechercher_salle(code)
        if salle:
            self.entry_description.delete(0, "end")
            self.entry_description.insert(0, salle.description)
            self.entry_categorie.delete(0, "end")
            self.entry_categorie.insert(0, salle.categorie)
            self.entry_capacite.delete(0, "end")
            self.entry_capacite.insert(0, str(salle.capacite))
        else:
            messagebox.showerror("Erreur", "Salle introuvable.")


#fonction lister les salles--------------------------------------------------------------------
    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())
        liste = self.service_salle.recuperer_salles()
        for s in liste:
            self.treeList.insert("", "end", values=(s.code, s.description, s.categorie, s.capacite))
