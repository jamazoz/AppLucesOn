import paho.mqtt.client as mqtt
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
from time import sleep


# MQTT settings
MQTT_BROKER = os.getenv("broker.mqttdashboard.com")
MQTT_PORT = int(os.getenv("1883"))
MQTT_TOPIC = "luzcasa"
MQTT_USER = os.getenv("MQTT_USER")
MQTT_PW = os.getenv("MQTT_PW")





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
    st.markdown(f"## Tú audio:")

    #if display_output_text:
    st.markdown(f"## Texto en audio:")
    st.write(f" {output_text}")


if st.button("Apagar luz"):
    st.markdown(f"## Texto en audio:")
    st.write(f" {output_text}"



    

