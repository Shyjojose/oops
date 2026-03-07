class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        else:
            print(f"Instance already exists: {cls._instances[cls]}")
        return cls._instances[cls]




class Database(metaclass=SingletonMeta):
    def __init__(self, url):
        self.url = url

db1 = Database("postgres://localhost")
db2 = Database("mysql://localhost")

print(db1 is db2)   # True — same object!
print(db1.url)      # postgres://localhost
print(db2.url)      # postgres://localhost — db2 is actually db1!