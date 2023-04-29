"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __int__(self):
        self.top = None
        self._size = 0

    def push(self, elem):
        node = Node(elem)
        node.next = self.top
        self.top = node
        self._size = self._size + 1
        pass

    def pop(self):
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return node
        pass
    """

n = list(str(input()))
lista = ''
lista = list(lista)
for c in n:
    if c == '(':
        lista.insert(,c)
    elif c == ')':
        pilha.pop()
if pilha._size > 0:
    print("incorrect")
elif pilha._size == 0:
    print("correct")