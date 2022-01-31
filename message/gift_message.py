class GiftMessage:
    def __init__(self, gift_name, num, uname, face, guard_level, uid, timestamp, gift_id,
                 gift_type, action, price, rnd, coin_type, total_coin):
        """
        :param gift_name: 礼物名
        :param num: 礼物数量
        :param uname: 用户名
        :param face: 用户头像URL
        :param guard_level: 舰队等级，0非舰队，1总督，2提督，3舰长
        :param uid: 用户ID
        :param timestamp: 时间戳
        :param gift_id: 礼物ID
        :param gift_type: 礼物类型（未知）
        :param action: 目前遇到的有'喂食'、'赠送'
        :param price: 礼物单价瓜子数
        :param rnd: 随机数
        :param coin_type: 瓜子类型，'silver'或'gold'
        :param total_coin: 总瓜子数
        """
        self.gift_name = gift_name
        self.num = num
        self.uname = uname
        self.face = face
        self.guard_level = guard_level
        self.uid = uid
        self.timestamp = timestamp
        self.gift_id = gift_id
        self.gift_type = gift_type
        self.action = action
        self.price = price
        self.rnd = rnd
        self.coin_type = coin_type
        self.total_coin = total_coin

    @classmethod
    def from_command(cls, data: dict):
        return cls(
            data['giftName'], data['num'], data['uname'], data['face'], data['guard_level'],
            data['uid'], data['timestamp'], data['giftId'], data['giftType'],
            data['action'], data['price'], data['rnd'], data['coin_type'], data['total_coin']
        )