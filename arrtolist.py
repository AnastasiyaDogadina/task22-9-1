from linkedModel.linkedList import LinkedList


def arr_to_list(arr):
    linked_list = LinkedList()
    for i in arr:
        linked_list.pushright(i)
    return linked_list
