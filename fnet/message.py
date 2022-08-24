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


def new_message(msgId: int, data: bytes):
    msg = Message()
    msg.msgId = msgId
    msg.data = data
    return msg
