import threading

class Resource:
    def __init__(self, item_id):
        self.item_id = item_id
        self.lock = threading.Lock()
        self.locked_by = None
        self.waiting_queue = []  # usado futuramente se precisar
