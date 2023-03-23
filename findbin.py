def binary_search(array, element, left, right):
    if left > right:
        return right

    middle = (right + left) // 2
    if array[middle] < element <= array[middle + 1]:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


def find_item(arr, position):
    if arr[0] >= position:
        return None
    return binary_search(arr, position, 0, len(arr) - 1)
