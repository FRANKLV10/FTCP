from building import init_building


class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.buildings = {}
        self.gold = 10000
        self.gems = 1000

    def is_currency_enough(self, currency_type, cost):
        if currency_type == 0:
            return self.gems >= cost
        elif currency_type == 1:
            return self.gold >= cost
        else:
            return "unknown costBy"

    def cost_currency(self, currency_type, cost):
        if self.is_currency_enough(currency_type, cost) is True:
            if currency_type == 0:
                self.gems -= cost
            if currency_type == 1:
                self.gold -= cost


Players = {}

player_ids = ["user1", "user2", "user3"]


def create_player():

    for i in player_ids:
        p = Player(i)
        Players[p.player_id] = p
        init_building(p.buildings)

    print(Players)
