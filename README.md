## 🩺 General Health Chatbot

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

├── app.py

├── model_setup.py

├── requirements.txt

├── README.md

├── static/

│   ├── style.css

│   └── script.js

└── templates/
   
    └── index.html

| **Folder/File**        | **Description**                          |
| ---------------------- | ---------------------------------------- |
| `app.py`               | Flask backend application                |
| `model_setup.py`       | Loads Hugging Face model                 |
| `requirements.txt`     | Python packages required for the project |
| `README.md`            | Project documentation                    |
| `static/style.css`     | Custom CSS styling for frontend          |
| `static/script.js`     | JavaScript for frontend interactivity    |
| `templates/index.html` | Main HTML template for the chatbot UI    |




---
## 📸 Screenshot
<img width="1882" height="360" alt="image" src="https://github.com/user-attachments/assets/9ea9605f-0d0c-49f8-b333-4a1ae7f2a60e" />

---

## 💬 Example Questions to Try
  
• What is a balanced diet?  
• How much water should I drink daily?       
• What are some home remedies for cough?  
• How do I treat a minor burn at home?       
• What is the normal body temperature?  
• How to manage stress effectively?          
• What are the early signs of diabetes?  
• What is hyperventilation?                  
• What should I eat to improve immunity?  
• How can I sleep better at night?

---
## 🌱 Future Improvements

🔐 Add authentication for user sessions

🌐 Deploy on platforms like Render or Vercel

🗣️ Add speech-to-text feature

📊 Add analytics to track question trends

---

## ⚙️ Installation & Running Locally

## Step 1: Clone the Repository

git clone https://github.com/haleema-21/general-health-chatbot.git

cd general-health-chatbot

## Step 2: (Optional) Create Virtual Environment

python -m venv venv

venv\Scripts\activate

## Step 3: Install Required Packages

pip install -r requirements.txt

## Step 4: Run the Application

python app.py

Go to your browser and open:

http://127.0.0.1:5000

---
## 🔐 Disclaimer

⚠️ This chatbot is not a replacement for professional medical advice. It is intended for educational purposes only.
