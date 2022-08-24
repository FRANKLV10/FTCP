import asyncio
import socket

from fnet.router import Router
from utils.logger import logger
from fnet.connection import Connection


class Server:
    def __init__(self, config):
        self.name = config.name
        self.ip = config.ip
        self.port = config.port
        self.AF_INET = (self.ip, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.loop = asyncio.get_event_loop()
        self.router = None

    async def start(self):
        """
        start accept client connection
        :return:
        """
        logger.info("fnet start success", self.router)
        conn_id = 0
        while True:
            conn, client_addr = await self.loop.sock_accept(self.socket)
            logger.info(f'a client connect to server ======> client_addr:{client_addr}')
            deal_conn = Connection(conn, conn_id, self.router)
            self.loop.create_task(deal_conn.start_reader())
            conn_id += 1

    def stop(self):
        self.socket.close()

    def serve(self):
        self.socket.bind((self.ip, self.port))
        self.socket.listen(10)
        self.loop.run_until_complete(self.start())

    def add_router(self, router: Router):
        self.router = router


if __name__ == '__main__':
    server = Server()
    server.serve()
