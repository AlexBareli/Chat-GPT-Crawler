import os
import openai
import wandb
from flask import Flask, request, render_template




app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/result", methods=['POST'])
def next_page():
    return render_template('mainint.html')

@app.route("/prompt", methods=['GET','POST'])
def question():
    return render_template('chatpage.html')

@app.route("/answer", methods=['GET', 'POST'])
def response():    
    openai.api_key = os.getenv("OPENAI_API_KEY")
    gpt_prompt = "Scrape https://www.usfca.edu/ for " + request.form['Question']
    
    response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=gpt_prompt,
    temperature=0,
    max_tokens=200,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None
        )
    
    return render_template('answer.html', response=response['choices'][0]['text'])

@app.route('/input/', methods=['POST', 'GET'])
def input():
    if request.method == 'POST':
        question = request.form['Question']
        return response()
    if request.method == 'GET':
        return f"Cannot get a valid input"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4999, debug=True)