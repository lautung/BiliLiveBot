from plugin import BotPlugin


class Live(BotPlugin):

    async def on_command_received(self, cmd, data):
        if cmd != 'LIVE':
            return
        await self.send_message(f'欢迎主播回家！')