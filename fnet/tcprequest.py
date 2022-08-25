import asyncio

from fnet.datapack import data_pack
from fnet.message import Message
from utils.logger import logger


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

    def is_close(self) -> bool:
        """
        whether the connection is closed
        :return:
        """
        return getattr(self.conn, '_closed')

    async def send_msg(self, send_msgId, send_data):
        if self.is_close() is True:
            logger.exception("Connection closed when send msg")
            raise Exception("Connection closed when send msg")

        msg = data_pack.pack_msg(send_msgId, send_data)

        await self.loop.sock_sendall(self.conn, msg)
