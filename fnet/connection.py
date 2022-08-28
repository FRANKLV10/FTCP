import asyncio
from typing import Dict

from utils.logger import logger
from fnet.message import new_message
from fnet.datapack import data_pack
from fnet.tcprequest import TcpRequest


class Connection:
    def __init__(self, server, conn, connID, client_addr):
        self.server = server  # type: Server :object
        self.conn = conn
        self.connID = connID
        self.client_addr = client_addr
        self.loop = asyncio.get_running_loop()

    def close(self):
        """check connections status """
        self.conn.close()

    async def receive_data(self, deal_conn):
        """receive data from client """
        data = None

        logger.info(f"connID is {self.connID}")
        while True:
            # read msg head
            try:
                head_data = await self.loop.sock_recv(self.conn, data_pack.headLen)
                # print(f"receive head data: {head_data}")
                data_len, msgId = self.server.packet.unpack_msg(head_data)

                if data_len > 0:
                    data = await self.loop.sock_recv(self.conn, data_len)
                    # print(f"receive data: {data}")
                msg = new_message(msgId, data)

                # get client request
                req = TcpRequest(deal_conn, msg)
                await self.server.msg_handler.process_messages_now(req)
            except ConnectionError as e:
                print(f"{e}client disconnect,client addr:{self.client_addr}")

                self.close()
                self.server.conn_manager.delete_conn(self.connID)

                break

    async def send_msg(self, send_msgId: int, send_data: bytes):
        if self.is_close() is True:
            logger.exception("Connection closed when send msg")
            raise Exception("Connection closed when send msg")
        # pack msg
        msg = new_message(send_msgId, send_data)
        msg = self.server.packet.pack_msg(msg)
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
        self.connections: Dict[int:Connection] = {}
        self.lock = asyncio.Lock

    def add_conn(self, c: Connection):
        self.connections[c.connID] = c

    def clear_conn(self):
        for _, c in self.connections:
            c.close()
        print("all connection is closed")

    def get_conn(self, connID: int):
        return self.connections[connID]

    def delete_conn(self, connID: int):
        del self.connections[connID]

    def get_conn_num(self) -> int:
        return len(self.connections)
