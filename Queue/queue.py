class QueueUnderflow(Exception):
    def __init__(self,info):
        self.info = info

class Queue():
    def __init__(self):
        self.elems = []



