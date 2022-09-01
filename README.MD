TCP SERVER Framework
    

Server Example
    
    config = get_config("./config.json")
    server = Server(config)

    from FTCP.utils.parseconfig import get_config
    from FTCP.fnet.server import Router
    from FTCP.fnet.server import Server
    from FTCP.fnet.tcprequest import TcpRequest

    @server.router(1)
    class MyRouter3(Router):
        async def after_handle(self, req: TcpRequest):
            if req.msgId == 3:
                await req.connection.send_msg(3, b"hello client")



    server.serve()

Client Example
     
     import socket
     from FTCP.fnet.message import new_message
     from FTCP.fnet.datapack import DataPack
     c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     c.connect(("127.0.0.1", 8990))
     data_pack = DataPack()
     msg1 = new_message(1, b"hello")
     while True:
            c.send(msg)
            time.sleep(1)
            head = c.recv(8)
            data_len, id = data_pack.unpack_msg(head)

            data = c.recv(data_len)

            print(id, data.decode())
