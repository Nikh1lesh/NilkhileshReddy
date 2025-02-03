from abc import ABC, abstractmethod
class IDatabaseOperations(ABC):
    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass
class SQLDatabase(IDatabaseOperations):
    def insert(self):
        print('SQL insert')

    def update(self):
        print('SQL update')

    def delete(self):
        print('SQL delete')
class NoSQLDatabase(IDatabaseOperations):
    def insert(self):
        print('NoSQL insert')

    def update(self):
        print('NoSQL update')

    def delete(self):
        print('NoSQL delete')
def main():
    s = SQLDatabase()
    s.insert()
    s.update()
    s.delete()
    n = NoSQLDatabase()
    n.insert()
    n.update()
    n.delete()
main()