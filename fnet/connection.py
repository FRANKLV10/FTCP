import asyncio
import socket

from fnet.tcprequest import TcpRequest
from utils.logger import logger
from fnet.message import msg_handler, new_message


class Connection:
    def __init__(self, conn, connID, router):
        self.conn = conn
        self.connID = connID
        self.loop = asyncio.get_event_loop()
        self.router = router

    def start(self):
        pass

    def is_close(self) -> bool:
        """
        whether the connection is closed
        :return:
        """
        return getattr(self.conn, '_closed')

    def close(self):
        getattr(self.conn, '_closed')
        self.conn.close()

    async def start_receiver(self):
        """

        :param conn:
        :return:
        """
        data = b''
        logger.info(f"connID is {self.connID}")
        while True:
            # read msg head
            client_data = await self.loop.sock_recv(self.conn, msg_handler.headLen)
            logger.info(client_data)
            # data_len, msgId = data_pack.unpack_msg(client_data)
            data_len = 0
            msgId = 1
            if data_len > 0:
                data = await self.loop.sock_recv(self.conn, data_len)
                logger.info(data)
            msg = new_message(msgId, data)
            req = TcpRequest(self.conn, msg)

            #
            if self.router is not None:
                await self.router.pre_handle(req)
                await self.router.handle(req)
                await self.router.after_handle(req)

    async def send_msg(self, msgId, data):
        if self.close() is True:
            logger.exception("Connection closed when send msg")
            raise Exception("Connection closed when send msg")

        # msg_handler.pack_msg(msg)
        #
        # await self.loop.sock_sendall(msg)


if __name__ == '__main__':
    a, b = (1, 2)
    print(a, b)
