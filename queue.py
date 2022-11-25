from structures.Queue import Queue

# Ej 1
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]


class ModifiedStack:

    def __init__(self, limit) -> None:
        self.cola1 = Queue(limit)
        self.cola2 = Queue(limit)
        self.primario = True

    def push(self, elemento):
        if self.primario:
            self.cola1.enqueue(elemento)
        else:
            self.cola2.enqueue(elemento)

    def pop(self):
        if self.primario:
            size = self.cola1.getSize()
            for i in range(size - 1):
                elemento = self.cola1.dequeue()
                self.cola2.enqueue(elemento)
            elemento = self.cola1.dequeue()
            self.primario = not self.primario
            return elemento

        else:
            size = self.cola2.getSize()
            for i in range(size - 1):
                elemento = self.cola2.dequeue()
                self.cola1.enqueue(elemento)
            elemento = self.cola2.dequeue()
            self.primario = not self.primario
            return elemento
