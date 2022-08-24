from fnet.tcprequest import TcpRequest


class Router:
    """
    way to del with client connection
    """
    async def pre_handle(self, req: TcpRequest):
        raise NotImplementedError

    async def handle(self, req: TcpRequest):
        raise NotImplementedError

    async def after_handle(self, req: TcpRequest):
        raise NotImplementedError
