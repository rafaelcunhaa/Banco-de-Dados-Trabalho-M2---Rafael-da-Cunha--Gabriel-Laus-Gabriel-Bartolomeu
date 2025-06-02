from transacao import Transacao
from resources import Resource
import random

if __name__ == "__main__":
    NUM_THREADS = 4  # número de transações

    # criando os dois recursos compartilhados
    resource_x = Resource("X")
    resource_y = Resource("Y")

    # cada transação recebe um timestamp aleatório
    timestamps = list(range(1, NUM_THREADS + 1))
    random.shuffle(timestamps)

    threads = []
    for i in range(NUM_THREADS):
        t = Transacao(tid=i+1, timestamp=timestamps[i], resource_x=resource_x, resource_y=resource_y, manager=None)
        threads.append(t)

    # inicia as transações
    for t in threads:
        t.start()

    # espera todas terminarem
    for t in threads:
        t.join()

    print("\n[SIMULAÇÃO FINALIZADA]")
