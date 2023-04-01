import os
import openai
import wandb

openai.api_key = "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"

run = wandb.init(project='Chat GPT Webcrawler')
prediction_table = wandb.Table(columns=["prompt", "completion"])

gpt_prompt = "When is spring break for USF?"

response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=gpt_prompt,
    temperature=0.5,
    max_tokens=256,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
)

print(response['choices'][0]['text'])

predication_table.add_data(gpt_prompt, response['choices'][0]['text'])
