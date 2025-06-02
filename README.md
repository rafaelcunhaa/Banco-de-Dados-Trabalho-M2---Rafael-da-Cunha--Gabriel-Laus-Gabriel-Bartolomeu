# Simulação de Transações Concorrentes com Detecção e Resolução de Deadlocks

## 📌 Disciplina
Banco de Dados II  
Universidade do Vale do Itajaí – UNIVALI  
Professor: Maurício Pasetto de Freitas, MSc.

## 🧠 Objetivo
Este projeto tem como objetivo simular transações concorrentes acessando recursos compartilhados, gerando situações de **deadlock**, e utilizando a técnica de **timestamp (wait-die ou wound-wait)** para resolução. A execução é feita com uso de **threads em Python**.

## ⚙️ Funcionalidades
- Simulação de múltiplas transações (threads) concorrendo por recursos `X` e `Y`
- Controle de acesso com bloqueios binários
- Detecção de deadlocks
- Resolução de deadlocks com algoritmo `wait-die` (ou `wound-wait`)
- Mensagens detalhadas no terminal sobre o estado de cada transação
