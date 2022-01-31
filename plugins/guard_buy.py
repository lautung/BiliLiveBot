from plugin import BotPlugin


class GuardBuy(BotPlugin):

    async def on_command_received(self, cmd, data):
        if cmd != 'GUARD_BUY':
            return
        await self.send_message(f'感谢{data["data"]["username"]}的舰长。')
        await self.send_message(f'老板大气!!!')

