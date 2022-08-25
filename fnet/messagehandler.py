from fnet.tcprequest import TcpRequest


class MessageHandler:
    def __init__(self):
        self.apis = {}  # key msgId, value router
        self.worker_num = None
        self.queue = None

    async def process_messages_now(self, req: TcpRequest):
        router = self.apis.get(req.msgId)  # get router
        if router is not None:
            await router.pre_handle(req)
            await router.handle(req)
            await router.after_handle(req)
        else:
            print(f"msgId:{req.msgId} is not found")

    def add_router(self, msgId, router):
        self.apis[msgId] = router
        print(f"add router success,msgId is {msgId}")


msg_handler = MessageHandler()
