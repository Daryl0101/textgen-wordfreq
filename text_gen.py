import os
import dotenv
import requests

dotenv.load_dotenv()

TOKEN = os.getenv("HUGGINGFACE_TOKEN")

API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"
headers = {
    "Authorization": "Bearer " + TOKEN,
    "x-wait-for-model": "true"
    }

def query(content : str):
   payload={
      "inputs": content,
      "parameters": {
          "max_new_tokens": 50,
          "num_return_sequences": 1,
          "temperature": 0.8
      }
  }
   response = requests.post(API_URL, headers=headers, json=payload)
   return response.json()

input="Life is a box of"
output = query(input)
print(f"Input: {input}\nGenerated Text: {output[0]['generated_text']}")
