def try_lock_with_wait_die(transacao, resource):
    # Tenta adquirir o lock do recurso sem bloquear
    if resource.lock.acquire(blocking=False):
        resource.locked_by = transacao  # Registra quem está com o recurso
        print(f"[T{transacao.tid}] Bloqueou recurso {resource.item_id}")
        return True
    else:
        # Recurso já está sendo usado por outra transação
        other = resource.locked_by
        print(f"[T{transacao.tid}] Esperando recurso {resource.item_id} (em posse de T{other.tid})")

        # Se a transação for mais velha, ela pode esperar
        if transacao.timestamp < other.timestamp:
            print(f"[T{transacao.tid}] Espera permitida (mais velha que T{other.tid})")
            while resource.lock.locked():
                pass  # Espera ocupada (melhor usar Condition no futuro)
            return try_lock_with_wait_die(transacao, resource)  # Tenta novamente
        else:
            # Se for mais nova, aborta (wait-die)
            print(f"[T{transacao.tid}] Abortada (mais nova que T{other.tid}) - Wait-die")
            transacao.aborted = True
            return False
