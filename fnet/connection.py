import asyncio
import socket

from fnet.messagehandler import msg_handler
from fnet.tcprequest import TcpRequest
from utils.logger import logger
from fnet.message import new_message
from fnet.datapack import data_pack


class Connection:
    def __init__(self, conn, connID):
        self.conn = conn
        self.connID = connID
        self.loop = asyncio.get_running_loop()


    def start(self):
        pass

    def close(self):
        """check connections status """
        getattr(self.conn, '_closed')
        self.conn.close()

    async def receive_data(self):
        """receive data from client """
        data = b''
        logger.info(f"connID is {self.connID}")
        while True:
            # read msg head
            head_data = await self.loop.sock_recv(self.conn, data_pack.headLen)
            print(f"receive head data: {head_data}")
            data_len, msgId = data_pack.unpack_msg(head_data)

            if data_len > 0:
                data = await self.loop.sock_recv(self.conn, data_len)
                print(f"receive data: {data}")
            msg = new_message(msgId, data)

            # get client request
            req = TcpRequest(self.conn, msg)

            await msg_handler.process_messages_now(req)


if __name__ == '__main__':
    a, b = (1, 2)
    print(a, b)
