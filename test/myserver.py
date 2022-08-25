from fnet.connection import Connection
from utils.parseconfig import get_config
from fnet.router import Router
from fnet.server import Server
from fnet.tcprequest import TcpRequest


class MyRouter1(Router):
    async def pre_handle(self, req: TcpRequest):
        if req.msgId == 1:
            await req.send_msg(1, b"dsdsdsdsd")


class MyRouter2(Router):
    async def handle(self, req: TcpRequest):
        if req.msgId == 2:
            await req.send_buff(data=b"434343")


class MyRouter3(Router):
    async def after_handle(self, req: TcpRequest):
        if req.msgId == 3:
            await req.send_msg(2, b"dsdsdsdsd")


if __name__ == '__main__':
    config = get_config("./config.json")
    r1 = MyRouter1()
    r2 = MyRouter2()
    r3 = MyRouter3()
    s = Server(config)
    s.add_router(1, r1)
    s.add_router(2, r2)
    s.add_router(3, r3)
    s.serve()
