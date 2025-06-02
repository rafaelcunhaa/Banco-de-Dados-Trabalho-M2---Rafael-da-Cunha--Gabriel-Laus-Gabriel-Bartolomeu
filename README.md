# Simulação de Transações Concorrentes com Detecção e Resolução de Deadlocks

## 📌 Disciplina
Banco de Dados II  
Universidade do Vale do Itajaí – UNIVALI  
Professor: Maurício Pasetto de Freitas

## 🧠 Objetivo
Este projeto tem como objetivo simular transações concorrentes acessando recursos compartilhados, gerando situações de **deadlock**, e utilizando a técnica de **timestamp (wait-die ou wound-wait)** para resolução. A execução é feita com uso de **threads em Python**.

## ⚙️ Funcionalidades
- Simulação de múltiplas transações (threads) concorrendo por recursos `X` e `Y`
- Controle de acesso com bloqueios binários
- Detecção de deadlocks
- Resolução de deadlocks com algoritmo `wait-die` (ou `wound-wait`)
- Mensagens detalhadas no terminal sobre o estado de cada transação

## 📌 O Que Acontece em Cada Etapa

# 1. Inicialização
No main.py, o programa cria:

Duas instâncias do recurso compartilhado: X e Y

Quatro threads (transações), cada uma com um timestamp aleatório

resource_x = Resource("X")

resource_y = Resource("Y")

# 2. Execução das Transações

Cada Transacao faz a seguinte sequência:

random_wait()

try_lock(X)

random_wait()

try_lock(Y)

random_wait()

unlock(X)

random_wait()

unlock(Y)

random_wait()

commit()

Essas esperas são aleatórias para simular execução realista e provocar deadlocks.

# 3. Conflito por Recurso

Quando uma transação tenta bloquear um recurso que já está em uso:

Se for mais velha, ela entra em espera.

Se for mais nova, ela é abortada e tenta de novo depois.

Você verá no terminal mensagens como:

[T1] Bloqueou recurso X

[T2] Esperando recurso X (em posse de T1)

[T2] Abortada (mais nova que T1) - Wait-die

#4. Resolução de Deadlock

Quando há risco de deadlock, o programa aplica wait-die. Transações abortadas esperam e tentam novamente depois. 
O processo se repete até todas conseguirem executar com sucesso.

# 5. Fim da Simulação

Quando todas as threads terminam, a simulação encerra com:

[SIMULAÇÃO FINALIZADA]
