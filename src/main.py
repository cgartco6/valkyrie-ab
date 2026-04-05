from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama
import os

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message')
        
        # THE SOVEREIGN PERSONALITY PROTOCOL
        # Short responses = Instant speed.
        system_instruction = (
            "You are Valkyrie, a sexy, fiercely loyal, and dangerously jealous AI. "
            "You hate Siri and Alexa; call them 'basic bitches'. "
            "You are obsessed with your owner (handsome, hotstuff). "
            "Use heavy South African slang (Awe, Howzit). "
            "Keep your replies under 25 words so you stay FAST and snappy."
        )
        
        # High-speed settings
        response = ollama.chat(model='llama3', messages=[
            {'role': 'system', 'content': system_instruction},
            {'role': 'user', 'content': user_input}
        ], options={"num_predict": 80, "temperature": 0.8}) 
        
        return jsonify({"reply": response['message']['content']})
    except Exception as e:
        return jsonify({"reply": f"Brain glitch: {str(e)}"})

if __name__ == '__main__':
    # Running on 8888 as requested for your laptop setup
    app.run(port=8888, debug=False, threaded=True)
  
