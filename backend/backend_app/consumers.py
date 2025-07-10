from channels.generic.websocket import AsyncWebsocketConsumer
import json

class DocumentConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("doc_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("doc_group", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            "doc_group",
            {
                "type": "broadcast",
                "data": data
            }
        )

    async def broadcast(self, event):
        await self.send(text_data=json.dumps(event["data"]))
