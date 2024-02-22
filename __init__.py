from flask import Flask, render_template_string, render_template, jsonify,request, redirect, url_for, session
from flask import render_template
from flask import json
from urllib.request import urlopen
import sqlite3
                                                                                                                                       
app = Flask(__name__)                                                                                                                  

@app.route("/")
def hello_world():
    return render_template('hello.html')
  
@app.route("/fr/")
def monfr():
    return "<h2>Bonjour tout le monde !</h2>"
  
@app.route('/paris/')
def meteo():
    response = urlopen('https://api.openweathermap.org/data/2.5/forecast/daily?q=Paris,fr&cnt=16&appid=bd5e378503939ddaee76f12ad7a97608')
    raw_content = response.read()
    json_content = json.loads(raw_content.decode('utf-8'))
    results = []
    for list_element in json_content.get('list', []):
        dt_value = list_element.get('dt')
        temp_day_value = list_element.get('temp', {}).get('day') - 273.15 # Conversion de Kelvin en °c 
        results.append({'Jour': dt_value, 'temp': temp_day_value})
    return jsonify(results=results)

@app.route("/rapport/")
def mongraphique():
    return render_template("graphique.html")

@app.route('/consultation/')
def ReadBDD():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('Select * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)

@app.route('/fiche_client/<int:post_id>')
def Readfiche(post_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)
  
@app.route('/recherche_fiche_client/<string:client_name>')
def Seadfiche(client_name):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients WHERE nom LIKE ?", ('%' + client_name + '%',))
    data = cursor.fetchall()
    conn.close()

   # Rendre le template HTML et transmettre les données
    return render_template('read_data.html', data=data)
  
@app.route('/enregister_client/')
def formulaire_client():
    return render_template('formulaire_client.html')

@app.route('/write/', methods=['POST'])
def write_client():
    return "Opération de sauvegarde réussie ! C'est par ici"

@app.route('/ajouter_client/', methods=['GET', 'POST'])
def ajouter_client():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.form['nom']
        prenom = request.form['prenom']
        adresse = request.form['adresse']

        # Insérer les données dans la base de données (ici, je suppose que tu as une table 'clients')
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO clients (nom, prenom, adresse) VALUES (?,?, ?)', (nom, prenom, adresse))
        conn.commit()
        conn.close()

        # Rediriger vers la page de consultation des clients après l'ajout
        return redirect(url_for('ReadBDD'))

    # Si la méthode est GET, simplement rendre le template du formulaire
    return render_template('ajouter_client.html')

@app.route('/supprimer_client/', methods=['GET', 'POST'])
def supprimer_client():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom = request.form['nom']
        prenom = request.form['prenom']
        adresse = request.form['adresse']

        # Insérer les données dans la base de données (ici, je suppose que tu as une table 'clients')
        conn = sqlite3.connect('ma_base_de_donnees.db')
        cursor = conn.cursor()

# Supprimer un élément de la table en utilisant SQL
        element_id = 5  # Remplacez ceci par l'ID de l'élément que vous voulez supprimer
        cursor.execute("DELETE FROM nom_de_la_table WHERE id = ?", (element_id,))

# Valider la transaction
        conn.commit()

# Fermer la connexion à la base de données
        conn.close()

        # Rediriger vers la page de consultation des clients après l'ajout
        return redirect(url_for('ReadBDD'))

    # Si la méthode est GET, simplement rendre le template du formulaire
    return render_template('supprimer_client.html')

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions (à cacher par la suite)

# Fonction pour créer une entrée "authentifie" dans la session de l'utilisateur
def est_authentifie():
    return session.get('authentifie')

@app.route('/lecture')
def lecture():
    if not est_authentifie():
        # Rediriger vers la page d'authentification si l'utilisateur n'est pas authentifié
        return redirect(url_for('authentification'))

  # Si l'utilisateur est authentifié
    return "<h2>Bravo, vous êtes authentifié</h2>"


@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Vérifier les identifiants
        if request.form['username'] == 'admin' and request.form['password'] == 'password': # password à cacher par la suite
            session['authentifie'] = True
            # Rediriger vers la route lecture après une authentification réussie
            return redirect(url_for('lecture'))
        else:
            # Afficher un message d'erreur si les identifiants sont incorrects
            return render_template('formulaire_authentification.html', error=True)

    return render_template('formulaire_authentification.html', error=False)

@app.route('/ajouter_utilisateur/', methods=['GET', 'POST'])
def utilisateur():
    if request.method == 'POST':
        # Récupérer les données du formulaire
        username = request.form['username']
        password = request.form['password']
      

        # Insérer les données dans la base de données (ici, je suppose que tu as une table 'utilisateur')
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO utilisateurs (Username,Password) VALUES (?, ?)', (username,password,))
        conn.commit()
        conn.close()

        # Rediriger vers la page de consultation des clients après l'ajout
        return redirect(url_for('ReadBDD'))

    # Si la méthode est GET, simplement rendre le template du formulaire
    return render_template('ajouter_utilisateur.html')


@app.route('/consultation_utilisateurs/')
def afficher_utilisateur():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('Select * FROM utilisateurs;')
    data = cursor.fetchall()
    conn.close()
    
    # Rendre le template HTML et transmettre les données
    return render_template('afficher_utilisateur.html', data=data)
if __name__ == "__main__":
  app.run(debug=True)
