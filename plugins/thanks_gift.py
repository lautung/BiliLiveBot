from plugin import BotPlugin
from message.gift_message import GiftMessage
import json


class ThanksGift(BotPlugin):

    async def on_command_received(self, cmd, data):
        if cmd != 'SEND_GIFT':
            return
        # print(json.dumps(data))

        # gift = GiftMessage.from_command(data['data'])
        # await self.send_message(f'感谢{gift.uname}送出的{gift.gift_name}x{gift.num}')