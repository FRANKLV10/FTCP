import asyncio
import socket

from fnet.tcprequest import TcpRequest
from utils.logger import logger
from fnet.message import new_message
from fnet.datapack import data_pack


class Connection:
    def __init__(self, conn, connID, router):
        self.conn = conn
        self.connID = connID
        self.loop = asyncio.get_running_loop()
        self.router = router

    def start(self):
        pass

    def close(self):
        """check connections stauts """
        getattr(self.conn, '_closed')
        self.conn.close()

    async def receive_data(self):
        """

        :param conn:
        :return:
        """
        data = b''
        logger.info(f"connID is {self.connID}")
        while True:
            # read msg head
            head_data = await self.loop.sock_recv(self.conn, data_pack.headLen)
            print(f"receive head data: {head_data}")
            data_len, msgId = data_pack.unpack_msg(head_data)
            # data_len = 0
            # msgId = 1
            if data_len > 0:
                data = await self.loop.sock_recv(self.conn, data_len)
                print(f"receive data: {data}")
            msg = new_message(msgId, data)

            # get client request
            req = TcpRequest(self.conn, msg)

            #
            if self.router is not None:
                await self.router.pre_handle(req)
                await self.router.handle(req)
                await self.router.after_handle(req)




if __name__ == '__main__':
    a, b = (1, 2)
    print(a, b)
