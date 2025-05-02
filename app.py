from flask import Flask, request, jsonify
import openai
import os

# Initialize Flask app
app = Flask(__name__)

# Get the OpenAI API key from environment variables (set it securely on Railway)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    
    if not user_message:
        return jsonify({"error": "No message provided!"}), 400

    # Generate response from GPT model
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # GPT-3 model
            prompt=f"You're a savage crypto genius. Analyze the crypto world like a pro, including meme coins. User says: {user_message}. Respond in a snarky and knowledgeable tone.",
            max_tokens=150
        )

        bot_response = response.choices[0].text.strip()
        return jsonify({"response": bot_response})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
