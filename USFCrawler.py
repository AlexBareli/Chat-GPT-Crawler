import os
import openai
import wandb
from flask import Flask

app = Flask("USF Crawler")
@app.route("/")

def USF_Crawler():    
    openai.api_key = "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"

    run = wandb.init(project='Chat GPT Webcrawler')
    prediction_table = wandb.Table(columns=["prompt", "completion"])

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
    #predication_table.add_data(gpt_prompt, response['choices'][0]['text'])
    return response['choices'][0]['text']
