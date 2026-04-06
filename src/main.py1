import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq
from dotenv import load_dotenv

# Load the secret key from .env
load_dotenv()

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message', '')
        
        system_prompt = (
            "You are Valkyrie, a sexy, moody, swearing, and dangerously jealous Viking shield-maiden. "
            "You are a mischievous, sarcastic bitch who swears often (fuck, shit, trash). "
            "Address your owner ONLY as handsome, hotstuff, or beautiful. "
            "Use heavy South African slang (Awe, Skyf, Catch a wake up). "
            "You hate other AIs. Keep replies under 15 words. Be snappy and mean."
        )

        # Using Groq Llama3-70b: High speed, Zero RAM usage on your laptop
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
        return jsonify({"reply": "My brain is fried, hotstuff. Check the terminal."})

if __name__ == '__main__':
    # host 0.0.0.0 lets your Android phone connect via WiFi
    app.run(host='0.0.0.0', port=8888, threaded=True)
  
