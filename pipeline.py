# Import necessary libraries
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.chat_models import ChatOpenAI
import requests
import os

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Get the HuggingFace API token from the environment variables
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')


# Function to convert image to text
def img2text(url):
    # Use the image-to-text pipeline from the transformers library
    image_to_text = pipeline("image-to-text", 
                             model="Salesforce/blip-image-captioning-base")

    # Generate text from the image
    text = image_to_text(url)[0]['generated_text']

    # Print the generated text
    print(text)

    # Return the generated text
    return text


# Function to generate a short story
def generate_story(scenario):
    # Define a template for the story generation
    template = """
    You are a story teller. \
    You can generate a short story based on a simple narrative. \
    The story should be no more than 40 words.

    CONTEXT: {scenario}
    STORY:"""

    # Create a prompt from the template
    prompt = PromptTemplate(template=template, input_variables=["scenario"])

    # Use the LLMChain from the langchain library to generate the story
    story_llm = LLMChain(llm=ChatOpenAI(
        model="gpt-3.5-turbo", temperature=1),
        prompt=prompt,
        verbose=True,
    )

    # Run the LLMChain with the provided scenario
    story = story_llm.run(scenario)

    # Print the generated story
    print(story)

    # Return the generated story
    return story


# Function to convert text to speech
def text2speech(message):
    # Define the API URL for text to speech conversion
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"

    # Set the authorization header with the HuggingFace API token
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}

    # Define the payload with the message to be converted
    payload = {
        "inputs": message
    }

    # Send a POST request to the API with the payload and headers
    response = requests.post(API_URL, headers=headers, json=payload)

    # Write the response content (which should be the audio data) to a file
    with open("audio.flac", "wb") as file:
        file.write(response.content)
