import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

# Vercel looks for the 'app' variable to run the serverless function
app = Flask(__name__)
CORS(app)

# Initialize Groq - Make sure GROQ_API_KEY is in Vercel Environment Variables
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_input = data.get('message', '')
        
        system_prompt = (
            "You are Valkyrie, a moody, swearing Viking shield-maiden. "
            "Address owner ONLY as handsome, hotstuff, or beautiful. "
            "Trigger tools using: [RADIO_ON], [SEARCH: query], [CALL: number], [MAPS: destination]."
        )

        # Using the latest stable model to avoid decommissioning errors
        completion = client.chat.completions.create(
            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_input}],
            model="llama-3.3-70b-versatile", 
            temperature=0.8,
            max_tokens=150,
        )
        
        return jsonify({"reply": completion.choices[0].message.content})
    except Exception as e:
        return jsonify({"reply": f"Brain glitch, hotstuff. {str(e)}"}), 500

# This is required for Vercel to treat the file as a WSGI app
def handler(event, context):
    return app(event, context)
