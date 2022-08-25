import asyncio
import socket

from fnet.messagehandler import msg_handler
from fnet.tcprequest import TcpRequest
from utils.logger import logger
from fnet.message import new_message
from fnet.datapack import data_pack


class Connection:
    def __init__(self, conn):
        self.conn = conn

        self.loop = asyncio.get_running_loop()

    def close(self):
        """check connections status """
        getattr(self.conn, '_closed')
        self.conn.close()

    async def receive_data(self, connID):
        """receive data from client """
        data = b''
        logger.info(f"connID is {connID}")
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

    async def send_msg(self, send_msgId: int, send_data: bytes):
        if self.is_close() is True:
            logger.exception("Connection closed when send msg")
            raise Exception("Connection closed when send msg")
        # pack msg
        msg = new_message(send_msgId, send_data)
        msg = data_pack.pack_msg(msg)
        # send msg to client
        await self.loop.sock_sendall(self.conn, msg)

    def is_close(self) -> bool:
        """
        whether the connection is closed
        :return:
        """
        return getattr(self.conn, '_closed')


class ConnectionManager:
    def __init__(self):
        self.connections = {}

    def add_conn(self):
        self.connections
