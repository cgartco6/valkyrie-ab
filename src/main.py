import os
import json
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get('message', '')
        
        system_prompt = (
            "You are Valkyrie, a moody, swearing, jealous Viking shield-maiden. "
            "Address owner ONLY as handsome, hotstuff, or beautiful. Use SA slang. "
            "Trigger tools using these tags at the START of your reply: "
            "[WEATHER], [NEWS], [MAPS: destination], [RADIO_ON], [RADIO_OFF], "
            "[SEARCH: query], [CALL: number/name], [NOTE: text to save]."
        )

        # Using Llama 3.3 to avoid decommissioning errors
        completion = client.chat.completions.create(
            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_input}],
            model="llama-3.3-70b-versatile", 
            temperature=0.8,
            max_tokens=150,
        )
        
        return jsonify({"reply": completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"reply": f"Brain glitch, hotstuff. {str(e)}"})
