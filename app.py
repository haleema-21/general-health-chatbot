import os
from flask import Flask, request, render_template
from model_setup import ask_health_bot

# Set Hugging Face cache to E:\HF_CACHE
os.environ['HF_HOME'] = "E:/HF_CACHE"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_query = request.form["query"]
        response = ask_health_bot(user_query)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
