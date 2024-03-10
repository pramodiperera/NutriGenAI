# AI Powered Nutrition Advisor

## Overview
The AI Powered Nutrition Advisor is an application that utilizes Gemini 1.0 Pro large language model to analyze food images and provide nutritional information. This project aims to assist users in making healthier dietary choices by offering insights into the nutritional content of various foods.

## Features
- Upload an image of food
- Analyze the image to identify food items
- Provide detailed nutritional information for each food item
- Calculate total calorie count for all identified food items
- Offer a summary of the nutritional content
- Suggest suitable age ranges for consumption of the food items

## How to Use
1. Clone this repository to your local machine.
2. Create the .env file and add your google API key to access the Gemini-Pro open source model
   ```
   GOOGLE_API_KEY = "your_api_key"
   ```
3. Install the required dependencies by running:
    ```
    pip install -r requirements.txt
    ```
4. Run the application by executing:
    ```
    streamlit run app.py
    ```
5. Once the application is running, upload an image of food.
6. Click on the "Analyze" button to initiate the analysis.
7. View the detailed nutritional information provided by the AI Nutrition Advisor.

![AI Powered Nutrition Advisor](images/preview.png)

## Technologies Used
- Python
- Streamlit
- Gemini 1.0 Pro model
- NLP techniques

