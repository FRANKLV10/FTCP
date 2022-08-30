

from socket import *
import config
import struct
import building_pb2


def building_proto():
    building = building_pb2.ReqUpgradeBuilding()
    building.playerId = 'test002'
    building.costBy = building_pb2.CostType.Gems
    building.buildingId = 1001
    print(building)

    data = building.SerializeToString()
    print(type(data))
    return data


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

        :param send_data: 数据包
        :return:
        """
        self.socket.send(send_data)

    def receive(self):
        """
        接受数据
        :return: 服务器回包
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
        建立连接，发送协议，接受协议

        :param ip:
        :param port:
        :param send_data:数据包
        :return: 服务器回包
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
    :return: 服务器回包
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


if __name__ == '__main__':
    data = building_proto()
    data = pack_package(data, 10001)
    A = proto_request(config.Server.IP, config.Server.port, data)
    unpack_package(A)
