from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class AbstractProductA(ABC):
    @abstractmethod
    def useful_function_a(self):
        pass


class AbstractProductB(ABC):
    @abstractmethod
    def useful_function_b(self):
        pass

    @abstractmethod
    def another_useful_function_b(self):
        pass

class ConcreteProductA(AbstractProductA):
    def useful_function_a(self):
        return "This is concrete product A"


class ConcreteProductB(AbstractProductB):
    def useful_function_b(self):
        return "This is concrete product B"

    def another_useful_function_b(self):
        return "This is concrete product B another function"


class ConcreteFactoryA(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA()

    def create_product_b(self):
        return ConcreteProductB()


class ConcreteFactoryB(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA()

    def create_product_b(self):
        return ConcreteProductB()


def client_code(factory):
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()
    print(f"Client: product_a: {product_a.useful_function_a()}")
    print(f"Client: product_b: {product_b.another_useful_function_b()}")


print("Client: testing client code, first factory")
client_code(ConcreteFactoryA())

