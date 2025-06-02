from transacao import Transacao
from resources import Resource
import random

if __name__ == "__main__":
    NUM_THREADS = 4
    # Criando recursos
    resource_x = Resource("X")
    resource_y = Resource("Y")

    timestamps = list(range(1, NUM_THREADS + 1))
    random.shuffle(timestamps)

    threads = []
    for i in range(NUM_THREADS):
        t = Transacao(tid=i+1, timestamp=timestamps[i], resource_x=resource_x, resource_y=resource_y)
        threads.append(t)

        for t in threads:
            t.start()
        
        for t in threads:
            t.join()

        print("\n[Simulação concluída]")

