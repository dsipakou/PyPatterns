class Target:
    def request(self) -> str:
        return "Default behavior"


class Adaptee:
    def specific_request(self) -> str:
        return "dlrow olleH"


class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee

    def request(self) -> str:
        return f"Adapted text: {self.adaptee.specific_request()[::-1]}"


def client_code(target: Target) -> None:
    print(target.request())


if __name__ == "__main__":
    print("Start here")
    target = Target()
    client_code(target)

    adaptee = Adaptee()
    print(adaptee.specific_request())

    adapter = Adapter(adaptee)
    client_code(adapter)
