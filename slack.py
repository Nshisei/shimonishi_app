import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from connection.target import get_temp_from_server
from post_database.db_operation import get_info_from_db
from chatgpt.chat import *


load_dotenv()

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

# @app.event("app_mention")
@app.message('服装予報')
def message_mention(message, say):
    name = message['text'].replace('服装予報', '').strip()  # 名前抽出
    print(name)
    temperature = get_temperature()  # get_温度
    clothes_list = get_info_from_db(name)
    text = make_text(temperature, clothes_list)
    print(text)
    advice = chatgpt(text)  # chatgptにメッセージを投げて、返してもらう
    print(advice)
    say(advice)

@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()