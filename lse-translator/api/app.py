from flask import Flask, request, jsonify
from src.translator import Translator

app = Flask(__name__)
translator = Translator('../../config.json')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    input_text = data.get('input_text')
    translated_text = translator.translate(input_text)
    return jsonify({'translated_text': translated_text})

