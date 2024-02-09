import requests
from bs4 import BeautifulSoup

# Définir les données du nouveau client à enregistrer
nouveau_client = {
    "nom": "Nom du nouveau client",
    "prenom": "Prénom du nouveau client",
    "email": "email@example.com",
    # Ajoutez d'autres champs selon vos besoins
}

# URL de la page de consultation
url_consultation = "http://mka.alwaysdata.net/consultation/"

# Récupérer la page HTML existante
response = requests.get(url_consultation)

# Vérifier si la requête a réussi
if response.status_code == 200:
    # Utiliser BeautifulSoup pour analyser la page HTML
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Créer une nouvelle balise HTML pour le nouveau client
    nouveau_client_html = soup.new_tag("div")
    nouveau_client_html.append(f"Nom: {nouveau_client['nom']}, Prénom: {nouveau_client['prenom']}, Email: {nouveau_client['email']}")
    
    # Ajouter la balise HTML du nouveau client à la page
    soup.body.append(nouveau_client_html)
    
    # Convertir la structure HTML mise à jour en chaîne de caractères
    html_mis_a_jour = str(soup)
    
    # Envoyer la page HTML mise à jour au serveur pour la sauvegarder
    response_mise_a_jour = requests.post(url_consultation, data={"html": html_mis_a_jour})
    
    # Vérifier si la mise à jour a réussi
    if response_mise_a_jour.status_code == 200:
        print("Page mise à jour avec succès !")
    else:
        print("Erreur lors de la mise à jour de la page :", response_mise_a_jour.status_code)
else:
    print("Erreur lors de la récupération de la page de consultation :", response.status_code)
