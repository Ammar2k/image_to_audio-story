import os
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from random import randint
import uuid

from pipeline import img2text, generate_story, text2speech


IMAGEDIR = "images/"

app = FastAPI()


@app.post("/upload/")
async def create_upload_file(file: UploadFile = File(...)):

    file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()

    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)

    print(IMAGEDIR + file.filename)
    scenario = img2text(IMAGEDIR + file.filename)
    story = generate_story(scenario)
    text2speech(story)
    # response = {"scenario": scenario, "story": story}

    return {"scenario": scenario, "story": story}


@app.post("/show/")
async def read_random_file():
    files = os.listdir(IMAGEDIR)
    random_index = randint(0, len(files) - 1)

    path = f"{IMAGEDIR}{files[random_index]}"

    return FileResponse(path)
