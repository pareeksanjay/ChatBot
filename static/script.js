document.getElementById('send').onclick = async function() {
    const msg = document.getElementById('message').value;
    appendMessage('user', msg);
    const response = await fetch('/chat', {    // Your backend endpoint
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: msg })
    });
    const data = await response.json();
    appendMessage('bot', data.reply);
    document.getElementById('message').value = '';
};

function appendMessage(role, text) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `${role}-message`;
    msgDiv.innerText = text;
    document.getElementById('chat-window').appendChild(msgDiv);
}