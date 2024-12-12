class InMemoryDB:
    def __init__(self):
        self.database = {}
        self.transaction = None

    def get(self, key):
        if self.transaction and key in self.transaction:
            return self.transaction[key]
        return self.database.get(key)

    def put(self, key, val):
        if self.transaction is None:
            raise Exception("Transaction not in progress. Use begin_transaction() first.")
        self.transaction[key] = val

    def begin_transaction(self):
        if self.transaction is not None:
            raise Exception("A transaction is already in progress.")
        self.transaction = {}

    def commit(self):
        if self.transaction is None:
            raise Exception("No active transaction to commit.")
        self.database.update(self.transaction)
        self.transaction = None

    def rollback(self):
        if self.transaction is None:
            raise Exception("No active transaction to rollback.")
        self.transaction = None


if __name__ == "__main__":
    inmemoryDB = InMemoryDB()

    print(inmemoryDB.get("A"))

    try:
        inmemoryDB.put("A", 5)
    except Exception as e:
        print(e)

    inmemoryDB.begin_transaction()
    inmemoryDB.put("A", 5)
    print(inmemoryDB.get("A"))

    inmemoryDB.put("A", 6)
    inmemoryDB.commit()
    print(inmemoryDB.get("A"))

    try:
        inmemoryDB.commit()
    except Exception as e:
        print(e)

    try:
        inmemoryDB.rollback()
    except Exception as e:
        print(e)

    print(inmemoryDB.get("B"))
    inmemoryDB.begin_transaction()
    inmemoryDB.put("B", 10)
    inmemoryDB.rollback()
    print(inmemoryDB.get("B"))
