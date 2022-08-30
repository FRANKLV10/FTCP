from socket import *
import struct
import building_pb2


class ProtoClient:
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)

    def connect(self, ip, port):
        """
        连接server
        :param
        :return:
        """
        ADDR = (ip, port)
        self.socket.connect(ADDR)

    def send(self, send_data):
        """

        :param send_data:
        :return:
        """
        self.socket.send(send_data)

    def receive(self):
        """

        :return:
        """
        while True:
            rev_data = self.socket.recv(1024)
            result = bytes()
            msg_len = len(rev_data)
            if msg_len != 0:
                result += rev_data
                self.socket.close()
                return result

    def transfer(self, ip, port, send_data):
        """


        :param ip:
        :param port:
        :param send_data:
        :return:
        """
        self.connect(ip, port)
        self.send(send_data)
        return self.receive()


def proto_request(IP, port, data):
    """
    proto api
    :param IP:
    :param port:
    :param data:
    :return:
    """

    rev_data = ProtoClient().transfer(IP, port, data)
    return rev_data


def pack_package(proto_data, msgId):
    head = struct.pack('ii', len(proto_data), msgId)
    send_data = head + proto_data
    return send_data


def unpack_package(rev_data):
    rev_proto = rev_data[8:]

    result = building_pb2.RspUpgradeBuilding()
    result.ParseFromString(rev_proto)
    print(type(result))
    print(result)


def building_proto(player_id: str, building_id: int, cost: str):
    building = building_pb2.ReqUpgradeBuilding()
    building.playerId = player_id
    if cost == "Gems":
        building.costBy = building_pb2.CostType.Gems
    elif cost == "Gold":
        building.costBy = building_pb2.CostType.Glod
    else:
        raise Exception("unknown type")
    building.buildingId = building_id
    print(building)

    data = building.SerializeToString()
    print(type(data))
    return data


if __name__ == '__main__':
    IP = "127.0.0.1"
    port = 8990
    data = building_proto("user1", 1001, "gold")
    data = pack_package(data, 10001)
    A = proto_request(IP, port, data)
    unpack_package(A)
