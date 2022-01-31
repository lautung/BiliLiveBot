from plugin import BotPlugin


class UserToastMsg(BotPlugin):

    async def on_command_received(self, cmd, data):
        if cmd != 'USER_TOAST_MSG':
            return
        await self.send_message(f'{data["data"]["toast_msg"]}')
        await self.send_message(f'感谢{data["data"]["username"]}续费的舰长，爱你哦！')
