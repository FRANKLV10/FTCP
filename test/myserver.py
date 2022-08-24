from utils.parseconfig import get_config
from fnet.router import Router
from fnet.server import Server
from fnet.tcprequest import TcpRequest


class MyRouter(Router):
    async def pre_handle(self, req: TcpRequest):
        await req.loop.sock_sendall(req.conn, b"pre handle")

    async def handle(self, req: TcpRequest):
        await req.loop.sock_sendall(req.conn, b"handle")

    async def after_handle(self, req: TcpRequest):
        await req.loop.sock_sendall(req.conn, b"after handle")


if __name__ == '__main__':
    config = get_config("./config.json")
    r = MyRouter()
    s = Server(config)
    s.add_router(r)
    print(s.router)
    s.serve()
