from abc import ABC, abstractmethod


class Database(ABC):
    @abstractmethod
    def query(self, sql: str) -> None:
        pass


class RealDatabase(Database):
    def query(self, sql: str) -> None:
        print(f"Executing query: {sql}")


class DatabaseProxy(Database):
    def __init__(self, has_access: bool):
        self._has_access = has_access
        self._real_db = RealDatabase()

    def query(self, sql: str) -> None:
        if not self._has_access:
            print("Access denied. Query cannot be executed.")
            return
        self._real_db.query(sql)


if __name__ == "__main__":
    user_db = DatabaseProxy(False)
    admin_db = DatabaseProxy(True)

    user_db.query("SELECT * FROM users")
    admin_db.query("SELECT * FROM users")
