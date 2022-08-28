import asyncio
import socket
import time

from fnet.datapack import DataPack
from fnet.message import new_message
from fnet.messagehandler import MessageHandler
from fnet.router import Router
from utils.logger import logger
from fnet.connection import Connection, ConnectionManager


class Server:
    def __init__(self, config):
        self.name = config.get("name")
        self.ip = config.get("ip")
        self.port = config.get("port")
        self.max_conn = config.get("maxcoon")
        self.AF_INET = (self.ip, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.msg_handler = MessageHandler()
        self.loop = asyncio.new_event_loop()
        self.conn_manager = ConnectionManager()
        self.packet = DataPack()

    async def start(self):
        """
        start accept client connection
        :return:
        """
        logger.info(f"[{self.name}] start success")
        conn_id = 0
        while True:
            conn, client_addr = await self.loop.sock_accept(self.socket)

            if self.conn_manager.get_conn_num() >= self.max_conn:
                conn.close()
            else:
                logger.info(f'a client connect to server ======> client_addr:{client_addr}')
                deal_conn = Connection(self, conn, conn_id, client_addr)
                self.conn_manager.add_conn(deal_conn)
                self.loop.create_task(deal_conn.receive_data(deal_conn))
                conn_id += 1
            print(self.conn_manager.get_conn_num())

    def router(self, msg_id: int):
        def wrapper(router: Router):
            self.add_router(msg_id, router())

        return wrapper

    def stop(self):
        self.socket.close()

    def serve(self):
        self.socket.bind((self.ip, self.port))
        self.socket.listen(self.max_conn)
        self.loop.run_until_complete(self.start())

    def add_router(self, msgId: int, router: Router):
        self.msg_handler.add_router(msgId, router)
