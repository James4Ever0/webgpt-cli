import openai
import sys

prompt = sys.argv[1]
openai.api_key = "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"
r = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0.8, max_tokens=800)
response = r.choices[0]['text']

print('\n'+response.strip("\n")+'\n')