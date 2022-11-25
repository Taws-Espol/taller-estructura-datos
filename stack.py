from structures.Stack import Stack

# Ej 1
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]


class ModifiedQueue:

    def __init__(self, limit) -> None:
        self.pila1 = Stack(limit)
        self.pila2 = Stack(limit)

    def push(self, elemento):
        size = self.pila1.size()
        for i in range(size - 1):
            tmp = self.pila1.pop()
            self.pila2.push(tmp)
        self.pila1.push(elemento)
        for i in range(size - 1):
            tmp = self.pila2.pop()
            self.pila1.push(tmp)

    def pop(self):
        if not self.pila1.isEmpty():
            return self.pila1.pop()
        return -1

# Ej 2
# Input: s = "()[]{}"
# Output: true


def ejercicio2(texto):
    size = len(texto)
    pila = Stack(size)

    push_items = ["(", "[", "{"]

    for letra in texto:
        if letra in push_items:
            pila.push(letra)

        elif letra == ")":
            if pila.pop() != "(":
                return False

        elif letra == "]":
            if pila.pop() != "[":
                return False

        elif letra == "}":
            if pila.pop() != "{":
                return False

    return pila.isEmpty()
