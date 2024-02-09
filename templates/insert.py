import requests
from bs4 import BeautifulSoup

# Définir les données du nouveau client à enregistrer
nouveau_client = {
    "nom": "Nom du nouveau client",
    "prenom": "Prénom du nouveau client",
    "email": "email@example.com",
    # Ajoutez d'autres champs selon vos besoins
}

# URL de votre endpoint pour enregistrer un nouveau client
url_enregistrement = "http://mka.alwaysdata.net/enregister_client/"

# Envoie de la requête POST avec les données du nouveau client
response = requests.post(url_enregistrement, data=nouveau_client)

# Vérifier si la requête a réussi
if response.status_code == 200:
    print("Nouveau client enregistré avec succès !")
    
    # Récupérer les données mises à jour de la page de consultation
    url_consultation = "http://mka.alwaysdata.net/consultation/"
    response_consultation = requests.get(url_consultation)
    
    # Vérifier si la requête de consultation a réussi
    if response_consultation.status_code == 200:
        # Utiliser BeautifulSoup pour extraire les données de la page
        soup = BeautifulSoup(response_consultation.content, "html.parser")
        # Ici, vous pouvez parcourir la structure HTML pour extraire les informations que vous souhaitez
        
        # Exemple : Afficher le titre de la page
        print("Données mises à jour de la page de consultation :")
        print(soup.title.text)
    else:
        print("Erreur lors de la récupération des données de consultation :", response_consultation.status_code)
else:
    print("Erreur lors de l'enregistrement du client :", response.status_code)
