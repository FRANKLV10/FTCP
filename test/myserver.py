from fnet.connection import Connection
from utils.parseconfig import get_config
from fnet.router import Router
from fnet.server import Server
from fnet.tcprequest import TcpRequest

config = get_config("./config.json")
server = Server(config)


@server.router(1)
class MyRouter1(Router):
    async def pre_handle(self, req: TcpRequest):
        if req.msgId == 1:
            await req.connection.send_msg(1, b"234234f")


@server.router(2)
class MyRouter2(Router):
    async def handle(self, req: TcpRequest):
        if req.msgId == 2:
            await req.connection.send_msg(2, b"freererfe")


@server.router(3)
class MyRouter3(Router):
    async def after_handle(self, req: TcpRequest):
        if req.msgId == 3:
            await req.connection.send_msg(3, b"freffdfdfrfe")


if __name__ == '__main__':

    server.serve()
