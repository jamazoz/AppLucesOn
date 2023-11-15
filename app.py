import streamlit as st
import cv2
import numpy as np
import pytesseract
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image

import network
import time
from machine import Pin
import dht
import ujson


st.title("Luces inteligentes en casa.")




def text_to_speech(text, tld):
    if text is not None:
        tts = gTTS(text,"es", tld, slow=False)
        try:
            my_file_name = text[0:20]
        except:
            my_file_name = "audio"
        tts.save(f"temp/{my_file_name}.mp3")
        return my_file_name, text
    else:
        st.write("Por favor pon un texto para que sea detectado.")


#display_output_text = st.checkbox("Verifica el texto")

if st.button("Encender luz"):
    result, output_text = text_to_speech(text, tld)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Tú audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    #if display_output_text:
    st.markdown(f"## Texto en audio:")
    st.write(f" {output_text}")


if st.button("Apagar luz"):





    

