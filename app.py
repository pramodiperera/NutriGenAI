import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

input_prompt="""
    You are an expert in nutrition where you need to analyze food items from the image and provide comprehensive details. Please list the foods identified in the image along with their respective calorie counts. Additionally, provide a summary of the food and the suitable age range for consumption for the entire selection.

    Example:
    1. Food Item - Calories
    2. Food Item - Calories
    3. Food Item - Calories
    ...
    Total Calories: [total calories]

    Summary:
    [Summary of the food items]

    Suitable Age Range:
    [Age range for consumption of the food items]


"""

def get_model_response(input, image):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0]])

    return response.text

def get_processed_image(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue() # read the file into bytes

        # image format required for gemini model
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("File was not uploaded !")
    

# streamlit application
st.set_page_config("Nutrition Advisor")
st.markdown("<h2 style='text-align: center; color: Black;'>AI powered Nutrition Advisor</h2>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Choose an image : ", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, width=350, caption="Uploaded image")

submit = st.button("Analyze")



if submit:
    image = get_processed_image(uploaded_file)
    response = get_model_response(input_prompt, image)
    st.subheader("Nutrition Analysis : ")
    st.write(response)