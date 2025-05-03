from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message', '')
    # Example response logic
    bot_response = f"I received your message: {user_message}"
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
