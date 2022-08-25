import socket
import time
from fnet.message import new_message
from fnet.datapack import data_pack


def client():
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(("127.0.0.1", 8990))
    msg1 = new_message(1, b"hello")
    msg2 = new_message(2, b"test")
    msg3 = new_message(3, b"bye")
    msg_list = [msg1,msg3, msg2]
    while True:
        for m in msg_list:
            msg = data_pack.pack_msg(m)
            c.send(msg)
            time.sleep(1)
            data = c.recv(1024)
            print(data)


if __name__ == '__main__':
    # expect print after handle,pre handle,handle
    client()

