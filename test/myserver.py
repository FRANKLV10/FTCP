from utils.parseconfig import get_config
from fnet.router import Router
from fnet.server import Server
from fnet.tcprequest import TcpRequest


class MyRouter1(Router):
    async def pre_handle(self, req: TcpRequest):
        if req.msgId == 1:
            await req.loop.sock_sendall(req.conn, b"pre handle")


class MyRouter2(Router):
    async def handle(self, req: TcpRequest):
        if req.msgId == 2:
            await req.loop.sock_sendall(req.conn, b"handle")


class MyRouter3(Router):
    async def after_handle(self, req: TcpRequest):
        if req.msgId == 3:
            await req.loop.sock_sendall(req.conn, b"after handle")


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
