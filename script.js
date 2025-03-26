async function envoyerMessage() {
    let question = document.getElementById("question").value;
    let chatBox = document.getElementById("chatBox");

    // Ajoute le message de l'utilisateur
    chatBox.innerHTML += `<div class="user-message">Vous: ${question}</div>`;

    // Appelle ton backend sécurisé
    let response = await fetch("https://ton-serveur.onrender.com/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: question })
    });

    let result = await response.json();
    let reponseIA = result.response;

    // Ajoute la réponse de l'IA en vert
    chatBox.innerHTML += `<div class="ai-message">IA: ${reponseIA}</div>`;

    // Efface la question après l'envoi
    document.getElementById("question").value = "";
}
