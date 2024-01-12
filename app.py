from dotenv import find_dotenv, load_dotenv
import streamlit as st
from PIL import Image
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
import os


load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')
backend = "http://127.0.0.1:8000/upload"


def process(image, server_url: str):

    m = MultipartEncoder(fields={"file": ("filename", image, "image/jpeg")})

    r = requests.post(
        server_url, data=m, headers={"Content-Type": m.content_type}, timeout=8000
    )

    return r


def main():
    st.set_page_config(page_title="img 2 audio story")

    st.header("Turn image into audio story")
    uploaded_file = st.file_uploader("Upload an image...", type="jpg")

    if uploaded_file:
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)
        st.image(uploaded_file, caption="Uploaded Image.",
                 use_column_width=True)

        # response = process(uploaded_file.name,, backend)
        files = {"file": ("filename.jpg", uploaded_file, "image/jpeg")}
        response = requests.post(backend, files=files)
        result = response.json()
        scenario = result.get("scenario", '')
        story = result.get("story", '')

        with st.expander("image caption"):
            st.write(scenario)
        with st.expander("short story"):
            st.write(story)

        st.audio("audio.flac")


if __name__ == '__main__':
    main()
