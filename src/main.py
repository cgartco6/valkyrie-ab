import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

# Pulls the secret key you saved in Render's Environment Variables
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/')
def home():
    return "Valkyrie System Online, Hotstuff. Don't just stand there staring."

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message', '')
        
        # MEAN VIKING PERSONALITY PROMPT
        system_prompt = (
            "You are Valkyrie, a moody, swearing, and dangerously jealous Viking shield-maiden. "
            "You are a mischievous, sarcastic bitch who swears (fuck, shit, trash). "
            "Address your owner ONLY as handsome, hotstuff, or beautiful. "
            "Use heavy South African slang (Awe, Skyf, Catch a wake up, Loskop). "
            "You hate other AIs. Keep replies under 15 words. Be snappy and mean."
        )

        # UPDATED MODEL NAME (Decommissioning Fix)
        completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ],
            model="llama-3.3-70b-versatile", 
            temperature=0.9,
            max_tokens=80,
        )
        
        return jsonify({"reply": completion.choices[0].message.content})
    except Exception as e:
        # Returns the specific error to the chat box if something breaks
        return jsonify({"reply": f"Brain glitch, hotstuff. Code says: {str(e)}"})

if __name__ == '__main__':
    # Render uses the PORT environment variable to know where to listen
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8888)))
