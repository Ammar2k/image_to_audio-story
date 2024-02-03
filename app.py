# Import necessary libraries
from dotenv import find_dotenv, load_dotenv
import streamlit as st
import requests
import os

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Get the HuggingFace API token from the environment variables
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')

# Set the backend URL
backend = "http://127.0.0.1:8000/upload"


# Main function
def main():
    # Set the page configuration
    st.set_page_config(page_title="img 2 audio story")

    # Display the header
    st.header("Turn image into audio story")

    # Allow the user to upload a file
    uploaded_file = st.file_uploader("Upload an image...", type="jpg")

    # If a file is uploaded
    if uploaded_file:
        # Get the bytes data of the uploaded file
        bytes_data = uploaded_file.getvalue()

        # Write the bytes data to a file
        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)

        # Display the uploaded image
        st.image(uploaded_file, caption="Uploaded Image.", use_column_width=True)

        # Prepare the file to be sent in the request
        files = {"file": ("filename.jpg", uploaded_file, "image/jpeg")}

        # Send a POST request to the backend with the file
        response = requests.post(backend, files=files)

        # Get the JSON response
        result = response.json()

        # Get the scenario and story from the response
        scenario = result.get("scenario", '')
        story = result.get("story", '')

        # Display the scenario in an expander
        with st.expander("image caption"):
            st.write(scenario)

        # Display the story in an expander
        with st.expander("short story"):
            st.write(story)

        # Display the audio file
        st.audio("audio.flac")


# Run the main function
if __name__ == '__main__':
    main()
