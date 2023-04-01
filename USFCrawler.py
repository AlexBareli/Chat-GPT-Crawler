import os
import openai
import wandb
from flask import Flask, request, render_template

app = Flask("USF Crawler")

@app.route("/")
def homepage():
    return render_template('USFCrawler.html')

@app.route("/response", methods=['POST'])
def response():    
    openai.api_key = os.getenv("OPENAI_API_KEY")
    gpt_prompt = request.form['Question']

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

@app.route('/input/', methods=['POST', 'GET'])
def input():
    if request.method == 'POST':
        question = request.form['Question']
        return response()
    if request.method == 'GET':
        return f"Cannot get a valid input"

