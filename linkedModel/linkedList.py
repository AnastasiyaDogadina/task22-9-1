from linkedModel.node import Node


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def clear(self):
        self.__init__()

    def pushright(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

    def __str__(self):
        R = ''

        pointer = self.first
        while pointer is not None:
            R += str(pointer.value)
            pointer = pointer.next
            if pointer is not None:
                R += ' '
        return R
