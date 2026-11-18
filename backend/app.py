
from flask import Flask, jsonify
from flask_cors import CORS

from database.connection import initialize_database
from routes.destinations import destinations_bp

# Création de l'application Flask
app = Flask(__name__)

# Autoriser les échanges avec React
CORS(app)

# Enregistrement des routes des destinations
app.register_blueprint(destinations_bp)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Bienvenue sur EcoTrip API",
        "status": "online"
    })


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "success",
        "message": "EcoTrip API fonctionne correctement !"
    })


if __name__ == "__main__":
    # Initialiser la base de données avant de démarrer le serveur
    initialize_database()

    app.run(debug=True, port=5000)
