🩺 General Health Chatbot

A simple web-based chatbot that answers general health-related queries using a pre-trained Hugging Face model. Built with Python, Flask, and Transformers, this chatbot helps users get safe and helpful responses to common medical questions.

---

## 🌟 Key Features

- 🤖 General health query response system
- 🧠 Powered by Google’s `flan-t5-small` transformer model
- 🖥️ Web-based interface built with Flask and HTML/CSS
- 💻 Fully local deployment (no external APIs needed)
- 🔐 Safe, basic responses (no serious medical diagnoses)

---

## 🚀 Tech Stack

| Technology    | Purpose                      |
|---------------|-------------------------------|
| Python 3.x     | Backend logic & model handling |
| Flask          | Web framework                 |
| Hugging Face Transformers | Model loading          |
| HTML/CSS       | Front-end structure & design   |
| JavaScript *(optional)* | UI interactivity         |

---

## 🗂️ Project Structure

Health_chatbot/
├── app.py                  # Flask web server
├── model_setup.py          # Model loading and response generation
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Frontend HTML
└── static/
    └── style.css           # Styling



---
📸 Screenshot
<img width="1882" height="360" alt="image" src="https://github.com/user-attachments/assets/9ea9605f-0d0c-49f8-b333-4a1ae7f2a60e" />

---

## 💬 Example Questions to Try

- What is a sore throat?
- How to stay healthy during winter?
- What does hyperventilating mean?
- How to treat a mild headache?

---
 Future Improvements
🔐 Add authentication for user sessions

🌐 Deploy on platforms like Render or Vercel

🗣️ Add speech-to-text feature

📊 Add analytics to track question trends

---

⚙️ Installation & Running Locally

Step 1: Clone the Repository
bash
Copy
Edit
git clone https://github.com/haleema-21/general-health-chatbot.git
cd general-health-chatbot
Step 2: (Optional) Create Virtual Environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
Step 3: Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
Step 4: Run the Application
bash
Copy
Edit
python app.py
Go to your browser and open:
http://127.0.0.1:5000

---
🔐 Disclaimer
⚠️ This chatbot is not a replacement for professional medical advice. It is intended for educational purposes only.
