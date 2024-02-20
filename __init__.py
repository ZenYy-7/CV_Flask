from flask import Flask, render_template, jsonify, request, redirect, url_for
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
# Route pour afficher le formulaire de contact
@app.route('/contact')
def contact_form():
    return render_template('contact.html')

# Route pour gérer la soumission du formulaire de contact
@app.route('/submit_contact_form', methods=['POST'])
def submit_contact_form():
    # Récupérer les données du formulaire soumis
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # Insérer les données dans la base de données SQLite
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO messages (name, email, message) VALUES (?, ?, ?)", (name, email, message))
    conn.commit()
    conn.close()

    # Rediriger ou afficher un message de confirmation
    return "Votre demande de contact a bien été envoyée."
if(__name__ == "__main__"):
    app.run()
