import google.generativeai as genai
from dotenv import load_dotenv
import flask
from flask import request, jsonify
from flask_cors import CORS
import os

app = flask.Flask(__name__)
load_dotenv()
CORS(app)

api_key = os.getenv('API_KEY')
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-1.5-flash')


@app.route("/correct", methods=["POST"])
def correct():
    data = request.json
    text = data['text']
    result = model.generate_content(f"Correct the following text: {text}")
    return jsonify({"text": result.text})

if __name__ == '__main__':
    app.run(port=5000) 
