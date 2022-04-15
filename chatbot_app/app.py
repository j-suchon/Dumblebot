import os
from random import choice
import pandas as pd
from slack_bolt import App
from pymongo import MongoClient
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv

load_dotenv()
bot_token = os.getenv('SLACK_BOT_TOKEN')
app_token = os.getenv('SLACK_APP_TOKEN')

# Initialize a Slack App, connect to Postgres container
app = App(token=bot_token)

# Initiate MongoDB
client = MongoClient("mongodb://db:27017")
db = client['DumblebotDB']

# collection name
dialog = db["dialog"]
collection = dialog.find({})

if not list(collection):
    data = pd.read_csv('database/dumbledore_dialog.csv', index=False)
    for line in data['dialog'].to_dict().values():
        dialog.insert_one({'dialog': line})

# gathers all dialog into a list to chose from
collection = dialog.find({})
dialog_list = [obj['dialog'] for obj in collection]


@app.event('app_mention')
def mention_handler(body, say):
    say('Hello, Hogwarts Students!')


@app.event("message")
def handle_message_events(body, logger, say):
    logger.info(body)
    say(choice(dialog_list))


if __name__ == '__main__':
    handler = SocketModeHandler(app, app_token)
    handler.start()
