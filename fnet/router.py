import asyncio

from fnet.tcprequest import TcpRequest


class Router(object):
    """
    way to del with client connection
    """

    async def pre_handle(self, req: TcpRequest):
        pass

    async def handle(self, req: TcpRequest):
        pass

    async def after_handle(self, req: TcpRequest):
        pass
