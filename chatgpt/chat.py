import openai
import os
from dotenv import load_dotenv

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


def get_temperature():
    temp = "20"
    return temp

def chatgpt(temperature):
    openai.api_key = os.environ["API_KEY"]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # engine="davinci",
        # prompt="気温が{}度の時の服を60文字で".format(temperature)
        messages=[
            {"role": "user", "content": "気温が{}度の時の服を60文字で".format(temperature)},
        ]   
    )

    return response['choices'][0]['message']['content']


load_dotenv()

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

# @app.event("app_mention")
@app.message('服装予報')
def message_mention(message, say):
    name = message['text'].replace('服装予報', '')
    # temperature = get_temperature()
    # advice = chatgpt(temperature)
    # say(advice)

@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()



