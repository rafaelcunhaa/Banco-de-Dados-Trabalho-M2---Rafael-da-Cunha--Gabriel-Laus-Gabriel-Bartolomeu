import threading
import time
import random
from deadlock_handler import try_lock_with_wait_die

class Transacao(threading.Thread):
    def __init__(self, tid, timestamp, resource_x, resource_y, manager):
        super().__init__()
        self.tid = tid  # ID da transação
        self.timestamp = timestamp  # Marca temporal (idade da transação)
        self.resource_x = resource_x
        self.resource_y = resource_y
        self.aborted = False  # Marca se a transação foi abortada

    def run(self):
        while not self.aborted:
            print(f"[T{self.tid}] Iniciando execução (timestamp: {self.timestamp})")
            self.random_wait()

            # Tenta bloquear o recurso X
            if not try_lock_with_wait_die(self, self.resource_x):
                self.restart()
                continue

            self.random_wait()

            # Tenta bloquear o recurso Y
            if not try_lock_with_wait_die(self, self.resource_y):
                # Libera X se falhar em Y para evitar deadlock
                self.resource_x.lock.release()
                self.resource_x.locked_by = None
                print(f"[T{self.tid}] Liberou recurso {self.resource_x.item_id}")
                self.restart()
                continue

            # Simula execução com os dois recursos bloqueados
            self.random_wait()

            # Libera recursos após a execução
            self.resource_x.lock.release()
            self.resource_x.locked_by = None
            print(f"[T{self.tid}] Liberou recurso {self.resource_x.item_id}")
            self.random_wait()

            self.resource_y.lock.release()
            self.resource_y.locked_by = None
            print(f"[T{self.tid}] Liberou recurso {self.resource_y.item_id}")
            self.random_wait()

            print(f"[T{self.tid}] Finalizou com sucesso")
            break  # Sai do loop se executou com sucesso

    def restart(self):
        # Em caso de aborto, espera um pouco e recomeça
        print(f"[T{self.tid}] Abortada por deadlock - Reiniciando...")
        self.random_wait()

    def random_wait(self):
        # Espera aleatória para simular tempo de execução e concorrência
        time.sleep(random.uniform(0.1, 0.5))
