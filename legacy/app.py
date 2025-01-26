# from flask import Flask, request, jsonify
# from openai import OpenAI
# import os

# app = Flask(__name__)

# import openai

# @app.route('/generate-response', methods=['POST'])
# def generate_response():
#     # Set OpenAI API Key
#     openai.api_key = "sk-proj-..."  # Ensure this key is valid
    
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {
#                     "role": "system", 
#                     "content": "Provide motivational, concise messages tailored to someone's daily schedule."
#                 },
#                 {"role": "user", "content": "Just Give me some life and schedule advice"}
#             ]
#         )
#         return jsonify({"response": response['choices'][0]['message']['content']})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500