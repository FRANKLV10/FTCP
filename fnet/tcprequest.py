import asyncio

from fnet.message import Message


class TcpRequest:
    def __init__(self, conn, msg: Message):
        self.conn = conn
        self.msg = msg
        self.loop = asyncio.get_running_loop()

    @property
    def data(self) -> bytes:
        return self.msg.data

    @property
    def msgId(self) -> int:
        return self.msg.msgId




