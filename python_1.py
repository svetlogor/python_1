def sum_of_neighbors(numbers):
    """
    Withdraw the sum of its two neighbors.
    :param numbers: list, int, str
    :return: str
    """
    # Приобразовываем в список
    numbers_splited = []
    for value in numbers.split(' '):
        try:
            numbers_splited.append(int(value))
        except ValueError:
            pass

    # Складываем соседей
    max_index = len(numbers_splited) - 1
    min_index = 0
    numbers_new = []
    for i, e in enumerate(numbers_splited):
        if i == min_index:
            numbers_new.append(numbers_splited[i + 1])
        elif i == max_index:
            numbers_new.append(numbers_splited[i - 1])
        else:
            numbers_new.append(numbers_splited[i - 1] + numbers_splited[i + 1])
    # Преобразовываем в нужный формат
    numbers_new_str = ''
    for i in numbers_new:
        numbers_new_str += str(i) + ';'
    return numbers_new_str


if __name__ == '__main__':
    print(sum_of_neighbors(input('Введите числа: ')))




