import openai
import sys

openai.api_key = "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"
temp = sys.argv[1]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "気温が{}度の時の服を60文字で".format(temp)},
    ]   
)

print(response['choices'][0]['message']['content'])
