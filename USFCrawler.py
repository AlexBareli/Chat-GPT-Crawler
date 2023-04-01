import os
import openai
import wandb
from flask import Flask

app = Flask("USF Crawler")
@app.route("/")

def USF_Crawler():    
    openai.api_key = os.getenv("OPENAI_API_KEY")

    gpt_prompt = "How many people live on planet earth?"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=gpt_prompt,
        temperature=0.5,
        max_tokens=256,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
    )
    return response['choices'][0]['text']
