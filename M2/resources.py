import threading

class Resource:
    def __init__(self, item_id):
        self.item_id = item_id  # Nome do recurso (ex: "X" ou "Y")
        self.lock = threading.Lock()  # Lock associado ao recurso
        self.locked_by = None  # Indica qual transação está usando o recurso
        self.waiting_queue = []  # Lista de espera (não usada aqui, mas pode ser útil futuramente)
