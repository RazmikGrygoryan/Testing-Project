sequence = input("Введите последовательность чисел через пробел: ")
number = input("Введите любое число: ")

try:
    sequence_list = [int(x) for x in sequence.split()]
    number = int(number)

    def sort_list(lst):
        for i in range(len(lst)):
            for j in range(len(lst)-1-i):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
        return lst

    sorted_list = sort_list(sequence_list)

    for i in range(len(sorted_list)):
        if sorted_list[i] < number and sorted_list[i+1] >= number:
            position = i+1
            break

    print("Отсортированный список:", sorted_list)
    print("Позиция элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу:", position)

except ValueError:
    print("Ошибка ввода данных. Пожалуйста, введите только числа.")