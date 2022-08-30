from utils.parseconfig import get_config
from fnet.server import Server
from fnet.router import Router
from fnet.tcprequest import TcpRequest

from pb import building_pb2
from player import Players, create_player

error_id = {
    201: "currency not enough",
    202: ""
}

config = get_config("./config.json")
demo = Server(config)


@demo.router(10001)
class BuildingUpdate(Router):
    @staticmethod
    def res_msg(player, building):
        if building.error != "":
            error = True
        else:
            error = False

        res_msg = building_pb2.RspUpgradeBuilding()
        res_msg.buildingId = building.id
        res_msg.buildingLevelNow = building.level
        res_msg.playerGemNow = player.gems
        res_msg.playerGoldNow = player.gold
        res_msg.isSuccess = error
        res_msg.errorMsg = building.error
        res = res_msg.SerializeToString()
        return res

    async def handle(self, req: TcpRequest):
        msg = building_pb2.ReqUpgradeBuilding()
        msg.ParseFromString(req.data)

        player = Players[msg.playerId]
        building = player.buildings[msg.buildingId]
        is_enough = player.is_currency_enough(msg.costBy, building.cost[msg.costBy])
        if is_enough is True:

            building.upgrade_building(player)
            if building.error == "":
                print(building.error)
                player.cost_currency(msg.costBy, building.cost[msg.costBy])
        elif is_enough is False:
            building.error = f"currency not enough"
        else:
            building.error = is_enough
        res_msg = self.res_msg(player, building)
        await req.connection.send_msg(10001, res_msg)


if __name__ == '__main__':
    create_player()
    demo.serve()
