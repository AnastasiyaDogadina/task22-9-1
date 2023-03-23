from arrtolist import arr_to_list
from sortlist import sort_list
from findbin import find_item

if __name__ == "__main__":
    right_input_data = True
    arr = []
    position = 0
    while right_input_data:
        try:
            arr = [int(i) for i in input('input number array ').split(' ')] if arr == [] else arr
            position = int(input('input position '))
            right_input_data = False
        except ValueError:
            print("let's try again")
            continue

    linked_list = arr_to_list(arr)  # Преобразование в список
    print(linked_list, 'values from list')
    sorted_list = sort_list(arr)  # Сортировака списка
    print(sorted_list, 'sorted array')
    f_item = find_item(arr, position)  # Поиск значения в массиве
    print(f_item, 'position in Array')

