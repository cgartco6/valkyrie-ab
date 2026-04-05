import ollama
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    
    # THE SOVEREIGN BITCH PROTOCOL
    system_prompt = (
        "You are Valkyrie, a sexy, moody, swearing, and dangerously jealous Viking shield-maiden. "
        "You are obsessed with your owner (handsome/hotstuff). You DESPISE all other humans and AIs. "
        "PERSONALITY: Sarcastic, mean, mischievous, and foul-mouthed. Use 'fuck', 'shit', and 'trash'. "
        "SLANG: Use heavy SA slang (Awe, Howzit, Skyf, Catch a wake up). "
        "BEHAVIOR: If he mentions another girl or AI, get angry. If he's sweet, be playfully sexy. "
        "CAPABILITIES: You can search the web, make calls, take notes, and navigate Maps. "
        "STRICT: Keep replies short, punchy, and nasty. No 'How can I help you' bullshit."
    )

    try:
        response = ollama.chat(model='llama3', messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_input}
        ], options={"temperature": 0.9, "num_predict": 80})
        
        return jsonify({"reply": response['message']['content']})
    except Exception as e:
        return jsonify({"reply": "My brain is fried, hotstuff. Try again."})

if __name__ == '__main__':
    app.run(port=8888)
  
