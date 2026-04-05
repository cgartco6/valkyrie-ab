from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama
import edge_tts
import asyncio

app = Flask(__name__)
CORS(app) # Allows your HTML to talk to this Python script

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    nickname = "handsome" # We'll pull this from .env later
    
    # 1. Talk to Llama3 (Ollama must be running)
    response = ollama.chat(model='llama3', messages=[
        {'role': 'system', 'content': f'You are Valkyrie. Be sexy, mean, and loyal to {nickname}. Use SA slang.'},
        {'role': 'user', 'content': user_input},
    ])
    
    reply = response['message']['content']
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
  
