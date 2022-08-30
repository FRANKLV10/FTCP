import asyncio
import socket
from fnet.datapack import DataPack
from fnet.messagehandler import MessageHandler
from fnet.router import Router
from utils.logger import logger
from fnet.connection import Connection, ConnectionManager


class Server:
    def __init__(self, config, packet=None):
        self.name = config.get("name")
        self.ip = config.get("ip")
        self.port = config.get("port")
        self.max_conn = config.get("maxcoon")
        self.AF_INET = (self.ip, self.port)
        self.log = logger
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.msg_handler = MessageHandler()
        self.loop = asyncio.new_event_loop()
        self.conn_manager = ConnectionManager()
        self.packet = DataPack() if packet is None else packet

    async def start(self):
        """
        start accept client connection
        :return:
        """
        self.log.info(f"[{self.name}] start success")
        conn_id = 0
        while True:
            conn, client_addr = await self.loop.sock_accept(self.socket)
            # determinate max connection
            if self.conn_manager.get_conn_num() >= self.max_conn:
                conn.close()
            else:
                # receive message from client
                self.log.info(f'a client connect to server ======> client_addr:{client_addr}')
                deal_conn = Connection(self, conn, conn_id, client_addr)
                self.conn_manager.add_conn(deal_conn)
                self.loop.create_task(deal_conn.receive_data(deal_conn))
                conn_id += 1


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
