# Import the libraries
import spacy
import requests
import json

# Load the spacy model for English language
nlp = spacy.load("en_core_web_sm")

# Create a class named Chatbot
class Chatbot:
    # Define the __init__ method to initialize the chatbot
    def __init__(self):
        # Load the data from the data.json file
        self.data = self.load_data()
        # Initialize an empty list to store the user's history
        self.history = []

    # Define the load_data method to load the data from the data.json file
    def load_data(self):
        # Open the data.json file in read mode
        with open("data.json", "r") as file:
            # Load the JSON data from the file
            data = json.load(file)
            # Return the data
            return data

    # Define the process_input method to process the user input using spacy
    def process_input(self, user_input):
        # Create a spacy document from the user input
        doc = nlp(user_input)
        # Initialize an empty list to store the tokens
        tokens = []
        # Loop through each token in the document
        for token in doc:
            # Append the lowercased text of the token to the tokens list
            tokens.append(token.text.lower())
        # Return the tokens list
        return tokens

    # Define the match_intent method to match the user input with an intent from the data
    def match_intent(self, tokens):
        # Initialize a variable to store the highest score
        highest_score = 0
        # Initialize a variable to store the matched intent
        matched_intent = None
        # Loop through each intent in the data
        for intent in self.data["intents"]:
            # Initialize a variable to store the score for this intent
            score = 0
            # Loop through each example in this intent's inputs list
            for example in intent["inputs"]:
                # Create a spacy document from the example
                example_doc = nlp(example)
                # Loop through each token in the example document
                for token in example_doc:
                    # Check if the lowercased text of the token is in the tokens list
                    if token.text.lower() in tokens:
                        # Increment the score by 1
                        score += 1
            # Check if the score is higher than the highest score
            if score > highest_score:
                # Update the highest score with the score
                highest_score = score
                # Update the matched intent with this intent's name
                matched_intent = intent["name"]
        # Return the matched intent or None if no match found
        return matched_intent

    # Define the generate_response method to generate a response based on the matched intent and perform an action if needed
    def generate_response(self, matched_intent):
        # Initialize an empty dictionary to store the response data
        response_data = {}
        # Check if there is a matched intent or not
        if matched_intent:
            # Loop through each intent in the data
            for intent in self.data["intents"]:
                # Check if this intent's name matches with the matched intent
                if intent["name"] == matched_intent:
                    # Choose a random response from this intent's responses list and store it as message in response data 
                    response_data["message"] = random.choice(intent["responses"])
                    # Check if this intent has an action or not 
                    if "action" in intent:
                        # Store this intent's action as action in response data 
                        response_data["action"] = intent["action"]
                    else:
                        # Store None as action in response data 
                        response_data["action"] = None
        
        else:
            # Store a default message as message in response data 
            response_data["message"] = "Sorry, I did not understand that. Please try again."
            # Store None as action in response data 
            response_data["action"] = None
        
        # Return the response data 
        return response_data

    # Define the get_response method to get a response from the chatbot based on a user input 
    def get_response(self, user_input):
        # Process the user input using spacy and store it as tokens 
        tokens = self.process_input(user_input)
        # Match the tokens with an intent from the data and store it as matched_intent 
        matched_intent = self.match_intent(tokens)
        # Generate a response based on the matched intent and store it as response_data 
        response_data = self.generate_response(matched_intent)
        # Return the response data 
        return response_data

