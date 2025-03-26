from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ton token Hugging Face (Ne le partage jamais)
HUGGING_FACE_TOKEN = "VOTRE_CLE_API_ICI"  # Remplace par ton vrai token

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    question = data.get("message", "")

    headers = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}
    payload = {"inputs": question}

    response = requests.post(
        "https://api-inference.huggingface.co/models/microsoft/DialoGPT-medium",
        headers=headers,
        json=payload
    )

    if response.status_code == 200:
        result = response.json()
        return jsonify({"response": result.get("generated_text", "Désolé, je ne peux pas répondre.")})
    else:
        return jsonify({"response": "Erreur avec l'IA"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
