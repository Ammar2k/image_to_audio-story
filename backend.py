# Import necessary libraries
import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from random import randint
import uuid

# Import custom pipeline functions
from pipeline import img2text, generate_story, text2speech

# Define the directory where images will be stored
IMAGEDIR = "images/"

# Initialize FastAPI application
app = FastAPI()


# Define a POST endpoint for file upload
@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):
    # Generate a unique filename for the uploaded file
    file.filename = f"{uuid.uuid4()}.jpg"
    # Read the contents of the uploaded file
    contents = await file.read()

    # Write the contents to a new file in the specified directory
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)

    # Print the path of the saved file
    print(IMAGEDIR + file.filename)

    # Use the pipeline functions to process the image
    scenario = img2text(IMAGEDIR + file.filename)  # Extract text from image
    story = generate_story(scenario)  # Generate a story based on the text
    text2speech(story)  # Convert the story to speech

    # Prepare the response with the extracted text and the generated story
    response = {"scenario": scenario, "story": story}

    # Return the response
    return response


# Define a POST endpoint to serve a random image file
@app.post("/show/")
async def read_random_file():
    # List all files in the image directory
    files = os.listdir(IMAGEDIR)
    # Choose a random index to select a file
    random_index = randint(0, len(files) - 1)
    # Construct the path to the random file
    path = f"{IMAGEDIR}{files[random_index]}"
    # Return the file as a response
    return FileResponse(path)
