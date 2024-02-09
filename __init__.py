from flask import Flask, render_template_string, render_template, jsonify
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
    # Récupérer les données du formulaire
    nom = request.form['nom']
    prenom = request.form['prenom']
    email = request.form['email']
    # Supposons que vous ayez d'autres données à récupérer ici

    # Préparer les données pour l'envoi au site distant
    data = {
        'nom': nom,
        'prenom': prenom,
        'email': email,
        # Ajoutez d'autres données si nécessaire
    }

    # Effectuer la requête POST vers le site distant
    try:
        response = requests.post('https://mka.alwaysdata.net/consultation/', data=data)
        # Vérifier si la requête a réussi
        if response.status_code == 200:
            return "Opération de sauvegarde réussie !"
        else:
            return "Erreur lors de l'envoi des données au site distant."
    except Exception as e:
        return f"Une erreur s'est produite : {str(e)}"
                  
if __name__ == "__main__":
  app.run(debug=True)
