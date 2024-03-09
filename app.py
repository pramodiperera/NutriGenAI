import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import ImageChops

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))