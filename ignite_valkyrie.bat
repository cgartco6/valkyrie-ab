@echo off
setlocal enabledelayedexpansion
title VALKYRIE SOVEREIGN - FULL SYSTEM RESTORE
echo [!] INITIALIZING GLOBAL DOMINATION PROTOCOL...

:: --- STEP 1: FORCE-CREATE ALL DIRECTORIES ---
mkdir src src\brain src\tools data data\language_packs 2>nul

:: --- STEP 2: WRITE THE CORE BACKEND (src\main.py) ---
(
echo from flask import Flask, request, jsonify
echo from flask_cors import CORS
echo import ollama
echo import os
echo from dotenv import load_dotenv
echo.
echo load_dotenv(^)
echo app = Flask(__name__^)
echo CORS(app^)
echo.
echo @app.route('/chat', methods=['POST']^)
echo def chat(^):
echo     try:
echo         user_input = request.json.get('message'^)
echo         response = ollama.chat(model='llama3', messages=[
echo             {'role': 'system', 'content': 'You are Valkyrie, a sexy, loyal AI assistant for your owner. Use South African slang like Awe and Howzit. Be smart and ahead of the curve.'},
echo             {'role': 'user', 'content': user_input}
echo         ]^)
echo         return jsonify({"reply": response['message']['content']}^)
echo     except Exception as e:
echo         return jsonify({"reply": f"Error: {str(e)}"}^)
echo.
echo if __name__ == '__main__':
echo     app.run(port=8888, debug=True^)
) > src\main.py

:: --- STEP 3: WRITE THE LIVE DASHBOARD (index.html) ---
(
echo ^<!DOCTYPE html^>
echo ^<html^>
echo ^<head^>^<title^>VALKYRIE SOVEREIGN^</title^>
echo ^<style^>
echo   body { background: #000; color: #f00; font-family: 'Courier New'; padding: 20px; text-align: center; }
echo   #chat-box { height: 400px; border: 2px solid #400; overflow-y: scroll; padding: 15px; background: #050000; margin-bottom: 20px; text-align: left; }
echo   input { width: 70%%; background: #111; color: #fff; border: 1px solid #f00; padding: 15px; font-size: 1.1em; }
echo   button { background: #800; color: #fff; padding: 15px 30px; border: none; cursor: pointer; font-weight: bold; }
echo   button:hover { background: #f00; }
echo ^</style^>^</head^>
echo ^<body^>
echo   ^<h1^>VALKYRIE IMMORTAL: GLOBAL #1^</h1^>
echo   ^<div id="chat-box"^>^</div^>
echo   ^<input type="text" id="userInput" placeholder="Speak to me, handsome..." onkeypress="if(event.keyCode==13^)sendMessage(^)"^>
echo   ^<button onclick="sendMessage()"^>SEND^</button^>
echo   ^<script^>
echo     async function sendMessage(^) {
echo       const input = document.getElementById('userInput'^);
echo       const box = document.getElementById('chat-box'^);
echo       if(!input.value^) return;
echo       box.innerHTML += "^<p style='color:#0f0'^>^<b^>YOU:^</b^> " + input.value + "^</p^>";
echo       const response = await fetch('http://127.0.0.1:8888/chat', {
echo         method: 'POST',
echo         headers: {'Content-Type': 'application/json'},
echo         body: JSON.stringify({message: input.value^})
echo       }^);
echo       const data = await response.json(^);
echo       box.innerHTML += "^<p style='color:#f00'^>^<b^>VALKYRIE:^</b^> " + data.reply + "^</p^>";
echo       input.value = '';
echo       box.scrollTop = box.scrollHeight;
echo     }
echo   ^</script^>^</body^>^</html^>
) > index.html

:: --- STEP 4: WRITE REQUIREMENTS ---
(
echo flask
echo flask-cors
echo ollama
echo python-dotenv
) > requirements.txt

:: --- STEP 5: INSTALL & LAUNCH ---
echo [!] INSTALLING LIBRARIES...
pip install -r requirements.txt
echo [!] STARTING SOVEREIGN ENGINE ON PORT 8888...
python src/main.py
pause
