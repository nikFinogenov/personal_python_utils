class Target:
    def request(self):
        return "Ціль: поведінка цілі за умовчанням."

class Adaptee:
    def specific_request(self):
        return ".огонавотпадА акнідевоп авилбосО"

class Adapter(Target, Adaptee):
    def request(self):
        return f"Адаптер: (ПЕРЕКЛАД) {self.specific_request()[::-1]}"

def client_code(target: "Target"):
    print(target.request(), end="")

if __name__ == "__main__":
    print("Клієнт: Я можу чудово працювати з цільовими об’єктами:")
    target = Target()
    client_code(target)
    print("\n")

    adaptee = Adaptee()
    print("Клієнт: клас Adaptee має дивний інтерфейс. \n «Бачиш, я не розумію:")
    print(f"Адаптований: {adaptee.specific_request()}", end="\n\n")

    print("Клієнт: Але я можу працювати з ним через адаптер:")
    adapter = Adapter()
    client_code(adapter)