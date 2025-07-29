# D-D General Assistant
Overview
This Python script creates a Dungeons & Dragons (D&D) question-answering system using Google's Gemini 1.5 Flash model. It filters input to only respond to prompts related to D&D, based on a predefined keyword list.

Step1
pip install flask google-generativeai python-dotenv

Step2
Create a file:
app.py (this is the main file for running the server)
gemini_service.py (used to receive services from gemini by retrieving the api_key from .env after authentication)
template (used to store the .index web page)
Create a web page with index

Create an API

Purpose and Use Case
Ensures the AI stays focused on Dungeons & Dragons content.

Can be used in chatbots, educational tools, Discord bots, or any fantasy RPG Q&A system.

Prevents the model from answering unrelated questions.
