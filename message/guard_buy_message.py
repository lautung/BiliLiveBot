class GuardBuyMessage:
    def __init__(self, uid, username, guard_level, num, price, gift_id, gift_name,
                 start_time, end_time):
        """
        :param uid: 用户ID
        :param username: 用户名
        :param guard_level: 舰队等级，0非舰队，1总督，2提督，3舰长
        :param num: 数量
        :param price: 单价金瓜子数
        :param gift_id: 礼物ID
        :param gift_name: 礼物名
        :param start_time: 开始时间戳？
        :param end_time: 结束时间戳？
        """
        self.uid = uid
        self.username = username
        self.guard_level = guard_level
        self.num = num
        self.price = price
        self.gift_id = gift_id
        self.gift_name = gift_name
        self.start_time = start_time
        self.end_time = end_time

    @classmethod
    def from_command(cls, data: dict):
        return cls(
            data['uid'], data['username'], data['guard_level'], data['num'], data['price'],
            data['gift_id'], data['gift_name'], data['start_time'], data['end_time']
        )