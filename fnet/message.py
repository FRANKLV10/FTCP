import struct

from typing import Tuple, Any

from utils.logger import logger


class Message:
    def __init__(self):
        self._data = None
        self._msgId = None
        self._dataLen = None

    @property
    def msgId(self) -> int:
        return self._msgId

    @property
    def data(self) -> bytes:
        return self._data

    @property
    def dataLen(self) -> int:
        return self._dataLen

    @msgId.setter
    def msgId(self, value: int):
        self._msgId = value

    @data.setter
    def data(self, value: bytes):
        self._data = value
        self._dataLen = len(value)

    @dataLen.setter
    def dataLen(self, value):
        self._dataLen = value


class MessageHandler:
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


def new_message(msgId, data):
    msg = Message()
    msg.msgId = msgId
    msg.data = data
    return msg


msg_handler = MessageHandler()
