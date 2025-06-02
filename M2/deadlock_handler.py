def try_lock_with_wait_die(transaction, resource):
    """
    Tenta adquirir o bloqueio do recurso. Se não conseguir, verifica se deve abortar a transação.
    """
    if resource.lock.acquire(blocking=False):
        resource.locked_by = transaction.tid
        print(f"[T{transaction.tid}] Adquiriu recurso {resource.item_id}")
        return True
    else:
        other = resource
        print(f"[T{transaction.tid}] Esperando recurso {resource.item_id} bloqueado por T{other.locked_by}. Abortando transação.")

       if transaction.timestamp < other.locked_by.timestamp:
            print(f"[T{transaction.tid}] Espera permitida (mais velha que T{other.tip})")
            while resource.lock.locked():
                pass
            return try_lock_with_wait_die(transaction, resource)
        else:
         print(f"[T{transacao.tid}] Abortada (nais nova que T{other.locked_by})")
        transaction.abort() = True
        return False
