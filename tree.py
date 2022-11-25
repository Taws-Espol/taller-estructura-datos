from structures.Tree import Node
from structures.Stack import Stack

# Ej 1
# Input: root = [1,null,2,3]
# Output: [1,3,2]


def ejercicio1_v1(root):
    if root != None:
        ejercicio1_v1(root.left)
        print(root.data)
        ejercicio1_v1(root.right)


def ejercicio1_v2(root):
    pila = Stack(100)
    pila.push(root)
    while not pila.isEmpty():
        x = pila.peek()
        while x != None:
            pila.push(x.left)
            x = pila.peek()
        pila.pop()
        if not pila.isEmpty():
            x = pila.pop()
            print(x.data)
            pila.push(x.right)

# Ej 2
# Input: p = [1,2,3], q = [1,2,3]
# Output: true


def ejercicio2(tree1, tree2):
    if (tree1 == None and tree2 == None):
        return True
    if (tree1 == None or tree2 == None):
        return False

    if (tree1.data != tree2.data):
        return False
    return ejercicio2(tree1.left, tree2.left) and ejercicio2(tree1.right, tree2.right)
