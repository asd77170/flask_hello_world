import requests

def authentification(username, password):
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
        print("Connexion réussie!")
    else:
        print("Échec de la connexion. Code de statut:", response.status_code)

# Appel de la fonction d'authentification avec les informations d'identification appropriées
authentification("votre_nom_utilisateur", "votre_mot_de_passe")
