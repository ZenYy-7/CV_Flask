from flask import Flask, render_template, jsonify
import json
import sqlite3

app = Flask(__name__) #creating flask app name

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/resume_1')
def resume_1():
    return render_template("resume_1.html")

@app.route('/resume_2')
def resume_2():
    return render_template("resume_2.html")

@app.route('/resume_template')
def resume_template():
    return render_template("resume_template.html")

@app.route('/submit_message', methods=['POST'])
def submit_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    
    # Connexion à la base de données SQLite
    conn = sqlite3.connect('messages.db')
    cursor = conn.cursor()
    
    # Insertion du message dans la base de données
    cursor.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()
    
    return 'Message envoyé avec succès!'
# Création d'une nouvelle route pour la lecture de la BDD
@app.route('/lecture/')
def ReadBDD():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM livres').fetchall()
    conn.close()

    # Convertit la liste de livre en un format JSON
    json_posts = [{'id': post['id'], 'title': post['title'], 'content': post['auteur']} for post in posts]

    # Renvoie la réponse JSON
    return jsonify(posts=json_posts)
if(__name__ == "__main__"):
    app.run()
