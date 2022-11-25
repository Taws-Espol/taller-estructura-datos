from structures.SinglyLinkedList import LinkedList, Node

# Ej 1
# Input: list1 = [1,2,4], list2 = [1,3,4]
#Output: [1,1,2,3,4,4]


def ejercicio1(l1, l2):
    if (l1 == None and l2 == None):
        return None

    if l1 == None:
        return l2
    if l2 == None:
        return l1

    if l1.data < l2.data:
        lista = l1
        l1 = l1.next
    else:
        lista = l2
        l2 = l2.next

    head = lista

    while (l1 != None and l2 != None):
        if l1.data < l2.data:
            lista.next = l1
            l1 = l1.next
        else:
            lista.next = l2
            l2 = l2.next
        lista = lista.next

    if l1 == None:
        lista.next = l2
    else:
        lista.next = l1

    return head

# Ej 2
#Input: head = [1,1,2,3,3]
#Output: [1,2,3]


def ejercicio2(head):
    lista = []
    iterador = head
    prev = head

    while iterador != None:
        if iterador.data not in lista:
            lista.append(iterador.data)
            prev = iterador

        else:
            prev.next = iterador.next

        iterador = iterador.next

    return head

# Ej 3
# Input: head = [3,2,0,-4], pos = 1
#Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).


def ejercicio3(head):
    iterador_lento = head
    iterador_rapido = head

    if head == None or head.next == None:
        return False

    while (iterador_rapido.next != None and iterador_rapido.next.next != None):
        iterador_lento = iterador_lento.next
        iterador_rapido = iterador_rapido.next.next

        if iterador_lento == iterador_rapido:
            return True

    return False

# Ej 4
# Input: head = [1,2,6,3,4,5,6], val = 6
#Output: [1,2,3,4,5]


def ejercicio4(head, target):
    lista_enlazada = Node(0)
    prev = lista_enlazada

    while head != None:
        if head.data != target:
            lista_enlazada.next = Node(head.data)
            lista_enlazada = lista_enlazada.next
        head.next

    return prev.next
