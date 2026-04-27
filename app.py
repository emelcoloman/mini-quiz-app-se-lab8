from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/questions")
def get_questions():
    with open("questions.json", "r") as file:
        questions = json.load(file)

    return jsonify(questions)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)