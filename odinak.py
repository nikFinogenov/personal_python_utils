class Single(type):
    _instances = {}

    def __call__(cls):
        if cls not in cls._instances:
            instance = super().__call__()
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=Single):
    def some_business_logic(self):
        print('some_business_logic')


if __name__ == "__main__":

    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print("Одинак робить, усе однакове")
    else:
        print("Одинак не робить.")