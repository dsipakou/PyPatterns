def singleton(clazz):
    instances = {}
    def get_instance(*args, **kwargs):
        if clazz not in instances:
            instances[clazz] = clazz(*args, **kwargs)
        return instances[clazz]
    return get_instance

@singleton
class Foo:
    def __init__(self, num):
        self.num = num
    def hello(self):
        print(f"hello there: {self.num}")

a = Foo(1)
a.hello()
b = Foo(2)
b.hello()
a.hello()
print(a == b)
print(id(a))
print(id(b))

