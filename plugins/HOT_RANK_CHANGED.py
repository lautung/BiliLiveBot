from plugin import BotPlugin


class HotRankChanged(BotPlugin):

    async def on_command_received(self, cmd, data):
        if cmd != 'HOT_RANK_CHANGED':
            return
        if 0 < data["data"]["rank"] < 10:
            await self.send_message(f'当前{data["data"]["area_name"]}排名{data["data"]["rank"]}')
