import tkinter as tk
from tkinter import messagebox
import requests

def authentification():
    # Récupérer les valeurs saisies par l'utilisateur
    username = username_entry.get()
    password = password_entry.get()

    # URL du formulaire de connexion
    url = "http://mka.alwaysdata.net/login/"

    # Données d'identification
    data = {
        'username': username,
        'password': password
    }

    # Tentative de connexion en utilisant les informations d'identification
    response = requests.post(url, data=data)

    # Vérification de la réponse
    if response.status_code == 200:
        messagebox.showinfo("Connexion réussie", "Connexion réussie!")
    else:
        messagebox.showerror("Erreur de connexion", "Échec de la connexion. Veuillez vérifier vos informations d'identification.")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Authentification")

# Créer les libellés et les champs de saisie
username_label = tk.Label(root, text="Nom d'utilisateur:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

password_label = tk.Label(root, text="Mot de passe:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

# Créer le bouton de connexion
connexion_button = tk.Button(root, text="Connexion", command=authentification)
connexion_button.pack()

# Lancer la boucle principale
root.mainloop()
