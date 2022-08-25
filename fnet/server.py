import asyncio
import socket

from fnet.messagehandler import msg_handler
from fnet.router import Router
from utils.logger import logger
from fnet.connection import Connection


class Server:
    def __init__(self, config):
        self.name = config.get("name")
        self.ip = config.get("ip")
        self.port = config.get("port")
        self.max_conn = config.get("maxcoon")
        self.AF_INET = (self.ip, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.loop = asyncio.new_event_loop()

    async def start(self):
        """
        start accept client connection
        :return:
        """
        logger.info(f"[{self.name}] start success")
        conn_id = 0
        while True:
            conn, client_addr = await self.loop.sock_accept(self.socket)
            logger.info(f'a client connect to server ======> client_addr:{client_addr}')
            deal_conn = Connection(conn, conn_id)
            self.loop.create_task(deal_conn.receive_data(deal_conn))
            conn_id += 1

    def stop(self):
        self.socket.close()

    def serve(self):
        self.socket.bind((self.ip, self.port))
        self.socket.listen(self.max_conn)
        self.loop.run_until_complete(self.start())

    @staticmethod
    def add_router(msgId: int, router: Router):
        msg_handler.add_router(msgId, router)
