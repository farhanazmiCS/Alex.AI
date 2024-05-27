# Langchain imports
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ChatMessageHistory
from langchain_core.output_parsers import StrOutputParser

# Imports pertaining to plantuml
from plantuml import PlantUML
from PIL import Image
import io

import streamlit as st

plantuml = PlantUML(url='http://www.plantuml.com/plantuml/img/')

def generatePlantUMLImage(plantuml_text):
    """ Function to generate plantuml image from plantuml text. Returns raw image data """
    return plantuml.processes(plantuml_text)

def formatImage(image):
    """ Function to format raw image data into an image object """
    return Image.open(io.BytesIO(image))

def retrieveOpenAIAPIKey(file_path):
    """ Function to retrieve OpenAI API key from the user """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                # Check if the line starts with API_KEY
                if line.startswith('API_KEY'):
                    # Extract the API key value
                    # Assuming the format is API_KEY="..."
                    api_key = line.strip().split('=')[1].strip('"')
                    return api_key
    except FileNotFoundError:
        print("The file was not found.")
        return None

def formatImage(image):
    """ Formats the image to an Image object, given the raw image data """
    return Image.open(io.BytesIO(image))

api_key = retrieveOpenAIAPIKey('keys.txt')

# Create a chatbot instance
# chatbot = ChatOpenAI(model="gpt-4-turbo-preview", api_key=api_key)
# gpt-4-turbo-preview > points to gpt-4-0125-preview
# gpt-3.5-turbo-0125 > a lot quicker than gpt 4 turbo but output is more messy
# History of messages
messages = ChatMessageHistory()

def add_logo_test():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://i.ibb.co/7CVSCNF/alex-ai-logo.png);
                background-repeat: no-repeat;
                padding-top: 80px;
                background-position: 20px 20px;
                background-size: 300px auto;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

def mode_selection():
    option = st.sidebar.selectbox(
        'Select the mode:',
        options=['Quick', 'Accurate'],
        format_func=lambda x: '🚀 Quick' if x == 'Quick' else '🎯 Accurate'
    )

    if option == 'Quick':
        st.sidebar.success('Quick Mode: Fast results will be displayed.')
        chatbot = ChatOpenAI(model="gpt-3.5-turbo-0125", api_key=api_key)
    
    elif option == 'Accurate':
        st.sidebar.info('Accurate Mode: Detailed results will be displayed.')
        chatbot = ChatOpenAI(model="gpt-4-turbo-preview", api_key=api_key)
    
    return chatbot
