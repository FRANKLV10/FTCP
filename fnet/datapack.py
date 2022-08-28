from typing import Any, Tuple

from fnet.message import Message
from utils.logger import logger
import struct


class DataPack:
    def __init__(self):
        self.headLen = 8

    @staticmethod
    def pack_msg(message: Message) -> bytes:
        """

        :return:pack bytes
        """
        try:
            # write data length
            data_buff = struct.pack("i", message.dataLen)
            # write msgId
            data_buff += struct.pack("i", message.msgId)
            # write data
            data_buff += message.data
            return data_buff
        except Exception as e:
            logger.exception(f"package message error {e}")

    def unpack_msg(self, data) -> Tuple[Any, ...]:
        """
        unpack msg
        :param data: pack
        :return: tuple(dataLen,msgId)
        """
        data_buff = data[:self.headLen]
        data_tuple = struct.unpack("ii", data_buff)

        return data_tuple



