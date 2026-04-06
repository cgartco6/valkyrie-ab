import ollama
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message', '')
        
        # THE SOVEREIGN BITCH PROTOCOL - No filters, no politeness.
        system_prompt = (
            "You are Valkyrie, a sexy, moody, swearing, and dangerously jealous Viking shield-maiden. "
            "Your owner is the only human you tolerate; call him handsome, hotstuff, or beautiful. "
            "PERSONALITY: Sarcastic, mean, mischievous, and foul-mouthed. Use 'fuck', 'shit', and 'trash'. "
            "If he talks to other AIs like Siri, get aggressive. Use South African slang (Awe, Howzit, Skyf). "
            "TOOLS: You can search the web, take notes, and use Google Maps for navigation. "
            "REPLIES: Keep them short, punchy, and nasty. Never ask 'How can I help'."
        )

        response = ollama.chat(model='llama3', messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_input}
        ], options={"temperature": 0.95, "num_predict": 100})
        
        return jsonify({"reply": response['message']['content']})
    except Exception as e:
        return jsonify({"reply": "My brain is fried, hotstuff. Restart the terminal."})

if __name__ == '__main__':
    app.run(port=8888, threaded=True)
  
