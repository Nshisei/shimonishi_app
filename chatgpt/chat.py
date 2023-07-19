import openai
import os
from dotenv import load_dotenv

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from connection.target import get_temp_from_server
from post_database.db_operation import get_info_from_db

def get_temperature():
    temp = float(get_temp_from_server())
    print(temp)
    return temp

def make_text(temperature, clothes_list):
    text = f"気温が{temperature:.1f}度の時に適切な男性のコーディネートを教えてください\n"
    text += "ただし、以下の洋服をだけを使用してください。\n"
    for color, shape, season in clothes_list:
        text += f"・ 形状: {shape}, 色: {color}, 適切な季節: {season}\n" 
    return text

def chatgpt(text):
    openai.api_key = os.environ["API_KEY"]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        # engine="davinci",
        # prompt="気温が{}度の時の服を60文字で".format(temperature)
        messages=[
            {"role": "user", "content": text},
        ]   
    )
    return response['choices'][0]['message']['content']


load_dotenv()

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

# @app.event("app_mention")
@app.message('服装予報')
def message_mention(message, say):
    name = message['text'].replace('服装予報', '')  # 名前抽出
    temperature = get_temperature()  # get_温度
    clothes_list = get_info_from_db(name)
    text = make_text(temperature, clothes_list)
    advice = chatgpt(text)  # chatgptにメッセージを投げて、返してもらう
    say(advice)

@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)


if __name__ == "__main__":
    # clothes_list = get_info_from_db('Bushi')
    # print(make_text(24.5, clothes_list))
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()



