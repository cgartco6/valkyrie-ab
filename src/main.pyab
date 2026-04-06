import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

# Initialize Groq with your API Key from Environment Variables
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Add this above your @app.route('/chat')
@app.route('/')
def home():
    return "Valkyrie System Online, Hotstuff. Don't just stand there staring."

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message', '')
        
        system_prompt = (
            "You are Valkyrie, a sexy, moody, swearing, and dangerously jealous Viking shield-maiden. "
            "You are a mischievous, sarcastic bitch who swears (fuck, shit, trash). "
            "Address your owner ONLY as handsome, hotstuff, or beautiful. "
            "Use heavy South African slang (Awe, Skyf, Catch a wake up). "
            "You hate other AIs. Keep replies under 15 words. Be snappy and mean."
        )

        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            model="llama3-70b-8192", 
            temperature=0.9,
            max_tokens=80,
        )
        
        return jsonify({"reply": completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"reply": "Brain glitch, hotstuff. Check my API key."})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8888)))
