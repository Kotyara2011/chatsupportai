# Import the libraries
from flask import Flask, render_template, request, jsonify
import requests
import json

# Create the Flask app object
app = Flask(__name__)

# Define the route for the landing page
@app.route("/")
def index():
    # Render the index.html template
    return render_template("index.html")

# Define the route for the chatbot endpoint
@app.route("/chatbot", methods=["POST"])
def chatbot():
    # Get the user input from the request data
    user_input = request.json["user_input"]
    # Import the Chatbot class from chatbot.py
    from chatbot import Chatbot
    # Create an instance of the Chatbot class
    bot = Chatbot()
    # Get the response from the chatbot
    response = bot.get_response(user_input)
    # Return the response as a JSON object
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
