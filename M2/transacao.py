import threading, time, random


class Resource:
    def __int__(self, item_id):
        self.item_id = item_id
        self.lock = threading.Lock()
        self.locked_by = None
        self.waiting_queue = []

class Transacao(threading.Thread):
    def __int__(self, tid, timestamp, resource_x, resource_y):
        super().__init__()
        self.tid = tid
        self.timestamp = timestamp
        self.resource_x = resource_x
        self.resource_y = resource_y
        self.aborted = False

    def run(self):
        print(f"[T{self.tip}] Iniciando execução (timestamp: {self.timestamp})")
        self.try_lock(self.resource_x)
        self.random_wait()
        self.try_lock(self.resource_y)
        self.random_wait()
        self.unlock(self.resource_x)
        self.random_wait()
        self.unlock(self.resource_y)
        self.random_wait()
        print(f"[T{self.tid}] Finalizando execução (timestamp: {self.timestamp})")

        def random_wait(self):
            wait_time = random.uniform(0.1, 0.5)

        def try_lock(self, resource):
            adquire = resource.lock.adquire(blocking=False)
            if adquire:
                resource.locked_by = self
                print(f"[T{self.tid}] Bloqueou recurso {resource.item_id} ")
            else:
                print(f"[T{self.tid}] Esperando recurso {resource.item_id}")

        def unlock(self, resource):
            if resource.locked_by == self:
                resource.lock.release()
                resource.locked_by = None
                print(f"[T{self.tid}] Liberou recurso {resource.item_id}")
