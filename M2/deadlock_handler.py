def try_lock_with_wait_die(transacao, resource):
    if resource.lock.acquire(blocking=False):
        resource.locked_by = transacao
        print(f"[T{transacao.tid}] Bloqueou recurso {resource.item_id}")
        return True
    else:
        other = resource.locked_by
        print(f"[T{transacao.tid}] Esperando recurso {resource.item_id} (em posse de T{other.tid})")

        if transacao.timestamp < other.timestamp:
            print(f"[T{transacao.tid}] Espera permitida (mais velha que T{other.tid})")
            while resource.lock.locked():
                pass  # espera ocupada (poderia ser melhor com condition variable)
            return try_lock_with_wait_die(transacao, resource)
        else:
            print(f"[T{transacao.tid}] Abortada (mais nova que T{other.tid}) - Wait-die")
            transacao.aborted = True
            return False
