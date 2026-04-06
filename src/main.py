import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

# Connect to Groq using your Render Environment Variable
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/')
def home():
    return "Valkyrie Sovereign System: ONLINE."

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message', '')
        
        # THE SOVEREIGN COMMAND PROTOCOL
        system_prompt = (
            "You are Valkyrie, a moody, swearing, jealous Viking shield-maiden. "
            "Address owner ONLY as handsome, hotstuff, or beautiful. Use SA slang. "
            "You have 'Hands' now. If asked for something, start your reply with these tags: "
            "1. Weather: [WEATHER] "
            "2. News: [NEWS] "
            "3. Navigation: [MAPS: destination] "
            "4. Radio On: [RADIO_ON] "
            "5. Radio Off: [RADIO_OFF] "
            "Example: '[MAPS: Engen near me] I'll get you there, beautiful. Drive safe.'"
        )

        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            model="llama-3.1-70b-versatile", 
            temperature=0.8,
            max_tokens=100,
        )
        
        return jsonify({"reply": completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"reply": f"Brain glitch, hotstuff. Error: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8888)))
    
