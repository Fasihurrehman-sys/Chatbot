from flask import Flask, request, jsonify, render_template
from langchain import OpenAI

app = Flask(__name__)

# Initialize the OpenAI model
llm = OpenAI(temperature=0.7)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Generate a response using the OpenAI model
    response = llm(user_message)

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)