import json
import os
import requests
import re

def chatgpt(text, act):
  if not text == '':
     openai_api_key = "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" #It's free so there is no point in stealing it...
    
     if openai_api_key is None:
        raise ValueError("Missing API key")
    
     url = "https://api.openai.com/v1/chat/completions"
    
     headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}"
     }
    
     data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a " + str(act)
            },
            {
                "role": "user",
                "content": text
            }
        ]
    }
  
    
  response = requests.post(url, headers=headers, json=data)
  if response.status_code == 200:
      return(response.json()['choices'][0]['message']['content'])
      
  elif response.status_code == 429:
      return("Wait a minute, usage too much for API.")
  else:
    raise ValueError("Nothing was entered")
   
  
 

