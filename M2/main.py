from transacao import Transacao
from resources import Resource
import random

if __name__ == "__main__":
    NUM_THREADS = 4  # Define o número de transações

    # Cria os dois recursos compartilhados
    resource_x = Resource("X")
    resource_y = Resource("Y")

    # Atribui timestamps aleatórios para simular "idade"
    timestamps = list(range(1, NUM_THREADS + 1))
    random.shuffle(timestamps)

    threads = []
    for i in range(NUM_THREADS):
        # Cria cada transação com seus atributos e os recursos compartilhados
        t = Transacao(tid=i+1, timestamp=timestamps[i], resource_x=resource_x, resource_y=resource_y, manager=None)
        threads.append(t)

    # Inicia todas as transações
    for t in threads:
        t.start()

    # Aguarda todas finalizarem
    for t in threads:
        t.join()

    print("\n[SIMULAÇÃO FINALIZADA]")
