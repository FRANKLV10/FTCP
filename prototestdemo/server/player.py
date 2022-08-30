from building import init_building


class Player:
    def __init__(self, player_id):
        self.player_id = player_id
        self.buildings = {}
        self.gold = 10000
        self.gems = 1000

    def is_currency_enough(self, currency_type, cost):
        if currency_type == 0:
            return self.gold >= cost
        elif currency_type == 1:
            return self.gems >= cost
        else:
            return "unknown costBy"

    def cost_currency(self, currency_type, cost):
        if self.is_currency_enough(currency_type, cost) is True:
            if currency_type == 0:
                self.gold -= cost
            if currency_type == 1:
                self.gems -= cost


Players = {}

player_ids = ["test001", "test002", "test003"]


def create_player():

    for i in player_ids:
        p = Player(i)
        Players[p.player_id] = p
        init_building(p.buildings)

    print(Players)
