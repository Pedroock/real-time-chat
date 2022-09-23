import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        user = self.scope['user'].username

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'welcomer',
                'message': user,
            }
        )

    async def disconnect(self, close_code):
        user = self.scope['user'].username
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'leaver',
                'message': user,
            }
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = text_data_json['author']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'author': user,
                'message': message,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['author']

        await self.send(text_data=json.dumps({
            'author': user,
            'message': message
        }))
    
    async def welcomer(self, event):
        message = event['message']
        typex = event['type']

        await self.send(text_data=json.dumps({
            'typex': typex,
            'message': message
        }))

    async def leaver(self, event):
        message = event['message']
        typex = event['type']

        await self.send(text_data=json.dumps({
            'typex': typex,
            'message': message
        }))