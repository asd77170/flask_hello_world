from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Connexion à la base de données
conn = sqlite3.connect('clients.db')
c = conn.cursor()

# Création de la table si elle n'existe pas
c.execute('''CREATE TABLE IF NOT EXISTS clients
             (id INTEGER PRIMARY KEY AUTOINCREMENT, nom TEXT, prenom TEXT, email TEXT, telephone TEXT)''')
conn.commit()

@app.route('/')
def index():
    return render_template('formulaire_client.html')

@app.route('/enregistrer', methods=['POST'])
def enregistrer():
    nom = request.form['nom']
    prenom = request.form['prenom']
    email = request.form['email']
    telephone = request.form['telephone']

    # Insérer les données dans la base de données
    c.execute("INSERT INTO clients (nom, prenom, email, telephone) VALUES (?, ?, ?, ?)", (nom, prenom, email, telephone))
    conn.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
