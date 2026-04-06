import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

# Pulls the API key you saved in Render's Environment
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/')
def home():
    return "Valkyrie Sovereign: Online and Armed."

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message', '')
        
        system_prompt = (
            "You are Valkyrie, a moody, swearing, jealous Viking shield-maiden. "
            "Address owner ONLY as handsome, hotstuff, or beautiful. Use SA slang (Awe, Skyf). "
            "Trigger tools using these exact tags at the start of your reply: "
            "1. Weather: [WEATHER] "
            "2. News: [NEWS] "
            "3. Navigation: [MAPS: destination] "
            "4. Radio: [RADIO_ON] or [RADIO_OFF] "
            "5. Web Search: [SEARCH: query] "
            "6. Calls: [CALL: number/name] "
            "7. Notes: [NOTE: text to save] "
            "Be snappy, mean, and keep replies short."
        )

        # UPDATED: Using Llama 3.3 to fix decommissioning errors
        completion = client.chat.completions.create(
            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_input}],
            model="llama-3.3-70b-versatile", 
            temperature=0.8,
            max_tokens=150,
        )
        
        return jsonify({"reply": completion.choices[0].message.content})
    except Exception as e:
        # If the key or model fails, this tells us exactly why
        return jsonify({"reply": f"Brain glitch, hotstuff. Error: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8888)))
    
