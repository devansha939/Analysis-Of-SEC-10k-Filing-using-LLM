"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""
import os
import re
import string
import nltk
from nltk.corpus import stopwords
import requests
import google.generativeai as genai

genai.configure(api_key="AIzaSyDXm87eHQIBRuQY_bSD5a5B6hjoIqdB4fM")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

convo = model.start_chat(history=[
])

# Download the required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def load_and_preprocess(file_dir):
    preprocessed_filings = []
    stop_words = set(stopwords.words('english'))

    # Iterate over all files in the directory
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)

                # Load the file
                with open(file_path, 'r', encoding='utf-8') as f:
                    text = f.read()

                # Remove HTML tags
                text = re.sub(r'<[^>]+>', '', text)

                # Convert to lowercase
                text = text.lower()

                # Remove punctuation
                text = text.translate(str.maketrans('', '', string.punctuation))

                # Tokenize the text
                tokens = nltk.word_tokenize(text)

                # Remove stop words
                tokens = [token for token in tokens if token not in stop_words]

                # Join the tokens back into a string
                preprocessed_text = ' '.join(tokens)

                preprocessed_filings.append(preprocessed_text)

    print(f"Number of preprocessed filings: {len(preprocessed_filings)}")
    return preprocessed_filings

file_dir = 'sec-edgar-filings'
# Check if the directory exists
if not os.path.exists(file_dir):
    print("Directory '{file_dir}' does not exist. Please create it and add your 10-K filing text files.")
else:
    # List the contents of the directory
    dir_contents = os.listdir(file_dir)
    print(f"Contents of '{file_dir}' directory: {dir_contents}")

    # If the directory is empty, print a message
    if not dir_contents:
        print(f"The '{file_dir}' directory is empty. Please add your 10-K filing text files.")
    else:
        preprocessed_filings = load_and_preprocess(file_dir)

        for idx, filing in enumerate(preprocessed_filings):
            prompt = f"Analyze the following 10-K filing text and provide insights on the company's financial performance like revenue, shares profitability,loss , handling cost, research cost: {filing}"
            convo.send_message(prompt)
            # Print or store the generated insight
            print(f"Insight for filing {idx}:")
            print(convo.last.text)
            print("-" * 50)
