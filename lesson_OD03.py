# Сортировка пузырьком
bubble_array = [12, 15, 10, 9, 18, 7]
bubble_length = 6
for bubble_pass in range(bubble_length - 1):
    for bubble_index in range(bubble_length - 1 - bubble_pass):
        if bubble_array[bubble_index] > bubble_array[bubble_index + 1]:
            bubble_array[bubble_index], bubble_array[bubble_index + 1] = bubble_array[bubble_index + 1], bubble_array[bubble_index]
print(bubble_array)

# Быстрая сортировка
def fast_sort(quick_list):
    if len(quick_list) <= 1:
        return quick_list

    pivot = quick_list[0]
    lesser = list(filter(lambda el: el < pivot, quick_list))
    equal = [el for el in quick_list if el == pivot]
    greater = list(filter(lambda el: el > pivot, quick_list))

    return fast_sort(lesser) + equal + fast_sort(greater)

print(fast_sort([12, 7, 19, 3, 4, 12, 9]))

# Сортировка выбором
selection_array = [-9, 12, 3, -15, 4, 20]

def select_sort(select_list):
    for select_index in range(len(select_list)):
        min_position = select_index
        for select_j in range(select_index + 1, len(select_list)):
            if select_list[min_position] > select_list[select_j]:
                min_position = select_j
        select_list[select_index], select_list[min_position] = select_list[min_position], select_list[select_index]

select_sort(selection_array)
print(selection_array)

# Сортировка вставками
insertion_array = [-3, 5, 0, -8, 1, 10]

def insertion_sort(ins_list):
    for ins_index in range(1, len(ins_list)):
        current_value = ins_list[ins_index]
        ins_j = ins_index - 1
        while ins_j >= 0 and current_value < ins_list[ins_j]:
            ins_list[ins_j + 1] = ins_list[ins_j]
            ins_j -= 1
        ins_list[ins_j + 1] = current_value

insertion_sort(insertion_array)
print(insertion_array)