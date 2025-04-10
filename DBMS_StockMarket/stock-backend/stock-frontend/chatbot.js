document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    appendMessage('You', userInput);
    document.getElementById('user-input').value = '';

    fetch('/chatbot', {
        method: 'POST',
        body: JSON.stringify({ message: userInput }),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        appendMessage('Bot', data.reply);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function appendMessage(sender, message) {
    const chatBox = document.getElementById('chat-box');
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message');
    if (sender === 'You') {
        messageElement.classList.add('user-message');
    } else {
        messageElement.classList.add('bot-message');
    }
    messageElement.textContent = `${sender}: ${message}`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}
function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    if (message === "") return;

    const chatBox = document.getElementById('chat-box');
    const userMsg = document.createElement('div');
    userMsg.textContent = "You: " + message;
    chatBox.appendChild(userMsg);

    // Simulate bot reply
    const botMsg = document.createElement('div');
    botMsg.textContent = "Bot: (Thinking...)";
    chatBox.appendChild(botMsg);

    input.value = "";
}
