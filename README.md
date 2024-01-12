# Image to Audio Story App

This repository contains code for an interactive application that transforms an uploaded image into an audio story. The app utilizes generative AI models for image captioning, natural language generation, and text-to-speech synthesis. Users can upload an image, and the app will generate a caption for the image, create a short story based on the caption, and convert the story into audio format. The application now uses FastAPI for the backend.

## Setup

### Clone the Repository:

```bash
git clone https://github.com/your-username/image-to-audio-story.git
cd image-to-audio-story
```

### Install Dependencies:

```bash
pip install -r requirements.txt
```

### Set Up Environment Variables:

Create a `.env` file in the project root directory. Add your Hugging Face Hub API token, and your OpenAI API token to the `.env` file:

```bash
HUGGINGFACEHUB_API_TOKEN=your_api_token_here
OPENAI_API_KEY=your_api_token_here
```

## Running the App

### Run the FastAPI Backend:

```bash
uvicorn backend:app --reload
```

### Run the Streamlit Frontend:

```bash
streamlit run app.py
```

### Access the App:

Open your web browser and go to http://localhost:8501 to use the app locally.

## How the App Works

### Upload Image:

Click on the "Upload an image..." button to select an image file (JPEG format is supported).

### Image Captioning:

The app uses the Salesforce/blip-image-captioning-base model to generate a caption for the uploaded image.

### Story Generation:

The caption serves as a scenario for story generation. The app employs the ChatOpenAI model (gpt-3.5-turbo) to generate a short story based on the provided scenario.

### Text-to-Speech Synthesis:

The generated story is converted into audio format using the espnet/kan-bayashi_ljspeech_vits model available on the Hugging Face Model Hub.

### Results Display:

The generated scenario and story are displayed in expandable sections for user convenience. The audio file (audio.flac) is played to allow users to listen to the narrated story.

## Additional Information

This app is built using the Streamlit framework for the web interface and FastAPI for the backend. The Hugging Face Model Hub is utilized for accessing pre-trained models for image captioning and text-to-speech synthesis. Make sure to respect the usage policies and terms of service of the respective model providers (Salesforce, OpenAI, Hugging Face).