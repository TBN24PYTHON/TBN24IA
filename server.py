from flask import Flask, request, jsonify, render_template
import os
import requests

app = Flask(__name__)

# Récupérer le token depuis les variables d'environnement
API_TOKEN = os.getenv("HF_API_TOKEN")

if not API_TOKEN:
    raise ValueError("Le token de l'API Hugging Face est manquant. Définissez HF_API_TOKEN dans les variables d'environnement.")

API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
HEADERS = {"Authorization": f"Bearer {API_TOKEN}"}

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")  # 🔥 Affiche la page HTML du chatbot

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_input = data.get("message")

        if not user_input:
            return jsonify({"error": "Message manquant"}), 400

        response = requests.post(API_URL, headers=HEADERS, json={"inputs": user_input})

        if response.status_code != 200:
            return jsonify({"error": "Erreur lors de la requête à l'API"}), 500

        result = response.json()
        bot_reply = result.get("generated_text", "Je n'ai pas compris.")

        return jsonify({"response": bot_reply})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
