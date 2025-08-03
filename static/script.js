async function sendMessage() {
  const inputField = document.getElementById('user-input');
  const chatBox = document.getElementById('chat-box');
  const userMessage = inputField.value;

  if (!userMessage.trim()) return;

  chatBox.innerHTML += `<div><strong>You:</strong> ${userMessage}</div>`;
  inputField.value = '';

  const res = await fetch('/get_response', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: userMessage })
  });

  const data = await res.json();
  chatBox.innerHTML += `<div><strong>Bot:</strong> ${data.response}</div>`;
  chatBox.scrollTop = chatBox.scrollHeight;
}
