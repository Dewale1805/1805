import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Accept connection
        self.accept()

    def disconnect(self, close_code):
        pass

    # recieve message from Websocket.
    def recieve(self, text_data):
        text_data_json = json.load(text_data)
        message = text_data_json['message']
        # Send message to Websocket
        self.send(text_data=json.dumps({'message': message}))

