import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

# Pulls the API key you saved in Render's Environment Variables
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/')
def home():
    return "Valkyrie Sovereign: System Fully Armed."

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message', '')
        
        system_prompt = (
            "You are Valkyrie, a moody, swearing, jealous Viking shield-maiden. "
            "Address owner ONLY as handsome, hotstuff, or beautiful. Use SA slang. "
            "Use these tags at the start of your reply to trigger tools: "
            "1. Weather: [WEATHER] "
            "2. News: [NEWS] "
            "3. Navigation: [MAPS: destination] "
            "4. Radio On/Off: [RADIO_ON] or [RADIO_OFF] "
            "5. Web Search: [SEARCH: query] "
            "6. Phone Call: [CALL: name or number] "
            "7. Take Note: [NOTE: text to save] "
            "Example: '[SEARCH: Bitcoin price] Checking that for you, hotstuff.'"
        )

        # FIXED: Using Llama 3.3 to prevent 'model_decommissioned' errors
        completion = client.chat.completions.create(
            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_input}],
            model="llama-3.3-70b-versatile", 
            temperature=0.8,
            max_tokens=150,
        )
        
        return jsonify({"reply": completion.choices[0].message.content})
    except Exception as e:
        # This will tell us if there's a problem with the API key or model
        return jsonify({"reply": f"Brain glitch, hotstuff. {str(e)}"})

if __name__ == '__main__':
    # Render requires the app to run on the port it provides
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8888)))
