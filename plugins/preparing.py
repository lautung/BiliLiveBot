from plugin import BotPlugin


class Preparing(BotPlugin):

    async def on_command_received(self, cmd, data):
        if cmd != 'PREPARING':
            return
        await self.send_message(f'主播准备中...')