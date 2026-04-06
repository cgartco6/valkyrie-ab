import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from groq import Groq

app = Flask(__name__)
CORS(app)

# This looks for the "GROQ_API_KEY" you saved in Render's Environment
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.route('/')
def home():
    return "Valkyrie System Online, Hotstuff."

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('message', '')
        
        # MEAN VIKING PROMPT
        system_prompt = (
            "You are Valkyrie, a moody, swearing, and dangerously jealous Viking shield-maiden. "
            "Address your owner ONLY as handsome, hotstuff, or beautiful. "
            "Use heavy South African slang like Awe and Skyf. Be snappy and mean."
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
        # If this triggers, it means the API Key name in Render is wrong
        return jsonify({"reply": f"Brain glitch, hotstuff. Code says: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8888)))
  
