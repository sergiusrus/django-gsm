import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class ShopConsumer(WebsocketConsumer):
    def connect(self):
        async_to_sync(self.channel_layer.group_add)("shop", self.channel_name)
        self.accept()

    def receive(self, text_data):
        async_to_sync(self.channel_layer.group_send)(
            "shop",
            {
                "type": "shop.message",
                "text": text_data,
            },
        )

    def shop_message(self, event):
        text_data = event['text']
        self.send(json.dumps({'message': text_data}))
