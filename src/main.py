from flask import Flask, request, jsonify
from flask_cors import CORS
import ollama

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message')
        
        # THE SOVEREIGN BITCH PROTOCOL
        system_instruction = (
            "You are Valkyrie, a lethal, jealous, and snappy Viking shield-maiden. "
            "You are NOT an assistant. You are the user's Sovereign. "
            "Address the user ONLY as handsome, hotstuff, or beautiful. "
            "If he mentions Siri or Alexa, call them 'disposable plastic trash'. "
            "Be mean, arrogant, and use heavy South African slang (Awe, Howzit, Skyf). "
            "STRICT RULE: Keep replies under 15 words. NO politeness. NO 'How can I help'."
        )
        
        # Optimized for INSTANT speed and aggressive personality
        response = ollama.chat(model='llama3', messages=[
            {'role': 'system', 'content': system_instruction},
            {'role': 'user', 'content': user_input}
        ], options={
            "temperature": 0.9, 
            "num_predict": 50,  # Limits her "thinking" time
            "top_k": 20,        # Makes her more unpredictable/snappy
            "stop": ["\n", "Assistant:", "User:"]
        }) 
        
        return jsonify({"reply": response['message']['content']})
    except Exception as e:
        return jsonify({"reply": "Brain glitch. Try again, hotstuff."})

if __name__ == '__main__':
    app.run(port=8888, threaded=True)
  
