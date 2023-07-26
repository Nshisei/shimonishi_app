import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from connection.target import get_temp_from_server
from post_database.db_operation import *
from chatgpt.chat import *


load_dotenv()

# Install the Slack app and get xoxb- token in advance
app = App(token=os.environ["SLACK_BOT_TOKEN"])

# @app.event("app_mention")
@app.message('服装予報')
def _message_mention(message, say):
    text = message['text']
    if '服装予報' in text:
        f_message = False
        if '服装予報 with list' in text:
            name = text.replace('服装予報 with list', '').strip()  # 名前抽出
            f_message = True
        else:
            name = text.replace('服装予報', '').strip()  # 名前抽出
        print(name)
        temperature = get_temperature()  # get_温度
        gender = get_gender(name)
        clothes_list = get_info_from_db(name)
        text = make_text(temperature, clothes_list, gender)
        print(text)
        message = chatgpt(text)  # chatgptにメッセージを投げて、返してもらう
        print(message)
        if f_message:
            message = text + '\n\n' + message
    say(message)

@app.message('DB参照')
def _message_mention_db(message, say):
    text = message['text']
    if 'DB参照' in text:
        print(text)
        all_data = get_all_data()
        message = all_data
    say(message)

@app.message('insert clothes')
def _insert_clothes(message, say):
    text = message['text']
    if 'insert clothes' in text:
        print(text)
        value = text.replace('insert clothes', '').strip()  # 名前抽出
        value_list = value.split(',')
        text = insert_clothes(*value_list)
        if text != '':
            all_data = get_all_data()
            message = all_data
        else:
            message = text
    say(message)

@app.message('delete clothes')
def _delete_clothes(message, say):
    text = message['text']
    if 'delete clothes' in text:
        print(text)
        id = text.replace('delete clothes', '').strip()  # 名前抽出
        text = delete_clothes(id)
        if text != '':
            all_data = get_all_data()
            message = all_data
        else:
            message = text
    say(message)

    
@app.message('insert user')
def _insert_user(message, say):
    text = message['text']
    if 'insert user' in text:
        print(text)
        value = text.replace('insert user', '').strip()  # 名前抽出
        value_list = value.split(',')
        text = insert_user(*value_list)
        if text != '':
            all_data = get_all_data()
            message = all_data
        else:
            message = text
    say(message)


@app.message('delete user')
def _delete_user(message, say):
    text = message['text']
    if 'delete user' in text:
        print(text)
        id = text.replace('delete user', '').strip()  # 名前抽出
        text = delete_user(id)
        if text != '':
            all_data = get_all_data()
            message = all_data
        else:
            message = text
    say(message)

@app.event("message")
def handle_message_events(body, logger):
    logger.info(body)

if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()