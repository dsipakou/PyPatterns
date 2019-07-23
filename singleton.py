from typing import Optional


class SingletonMeta(type):
    _instance = None

    def __call__(self):
        print(self._instance)
        if self._instance is None:
            print('new instance')
            self._instance = super().__call__()
        else:
            print('old instance')
            return self._instance


class Singleton(metaclass=SingletonMeta):
    def hello(self):
        print("Hello world")


if __name__ == '__main__':
    a = Singleton()
    b = Singleton()
    a.hello()
    b.hello()
    print(id(a) == id(b))
    print(id(a))
    print(id(b))
