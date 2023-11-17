import json

import requests
import streamlit as st
from streamlit_lottie import st_lottie

def app():
    def load_lottiefile(filepath: str):
        with open(filepath, "r") as f:
            return json.load(f)
        

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code !=200:
            return None
        return json
    
    lottie_coding = load_lottiefile("lottiefiles/coding.json")
    lottie_hello = load_lottieurl("https://lottie.host/29cde157-2606-475b-99c3-687d8511a666/5jr1xQx8MY.json")

    st.title("Hello Welcome to StarHaze Blog")
    st_lottie(
        lottie_coding,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",
        height=None,
        width=None,
        key=None,
    )
    st.subheader('StarHaze is a website created for users to')
    st.subheader('share their valuable thoughts with the world.')
    st.markdown('Created by: [Mark Anthony Alegre](https://github.com/Ashwani132003)')
    st.markdown('Contact via mail: [mark.anthony.alegre05@gmail.com]')
    