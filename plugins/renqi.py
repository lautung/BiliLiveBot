from plugin import BotPlugin


class Renqi(BotPlugin):

    def __init__(self) -> None:
        super().__init__()
        self.currentPopularity = 0

    async def on_receive_popularity(self, popularity: int):
        print(f"之前人气:{self.currentPopularity},最新人气{popularity}。")

        if self.currentPopularity == 0:
            self.currentPopularity = popularity
            return

        if abs(popularity - self.currentPopularity) > 10000:
            self.currentPopularity = popularity
            await self.send_message(f'当前人气：{popularity}')
