class Building:
    def __init__(self, config: dict):
        self._level = 1
        self.id = config.get("id")
        self.max_level = config.get("max_level")
        self.pre_building = config.get("pre_building")
        self.gold_cost = config.get("gold_cost")
        self.gem_cost = config.get("gem_cost")
        self.cost = [config.get("gem_cost") ,config.get("gold_cost")]
        self.error = ""

    def upgrade_building(self, player):
        if self.pre_building is not None:
            if player.buildings[self.pre_building].level > self.level:
                self.level_up()

            else:
                self.error = "need upgrade_level"
        if self.pre_building is None:
            self.level_up()

    def level_up(self):
        if self.level >= self.max_level:
            self.error = "already max level"
        else:
            self._level += 1
            self.error = ""

    @property
    def level(self):
        return self._level

    def building_info(self):
        return


building_info = [
    {"id": 1001, "max_level": 10, "pre_building": None, "gold_cost": 1000, "gem_cost": 50},
    {"id": 1002, "max_level": 10, "pre_building": 1001, "gold_cost": 1500, "gem_cost": 100},
    {"id": 1003, "max_level": 10, "pre_building": 1002, "gold_cost": 2000, "gem_cost": 150}
]


def init_building(buildings):
    for i in building_info:
        buildings[i["id"]] = Building(i)
