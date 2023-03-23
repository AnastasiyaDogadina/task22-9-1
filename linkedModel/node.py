class Node:
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_

    def __str__(self):
        return "Node value = " + str(self.value)
