import time

from plugin import BotPlugin
import json

class Welcome(BotPlugin):

    async def on_command_received(self, cmd, data):
        if cmd != 'INTERACT_WORD':
            return
        # time.sleep(10)
        # await self.send_message(f'欢迎{data["data"]["uname"]}加入房间!')
