def process_input(input_arg):
    if isinstance(input_arg, dict):
        if len(input_arg) > 0:
            max_key = None
            max_value = float('-inf')
            for key, value in input_arg.items():
                if value > max_value:
                    max_key = key
                    max_value = value
            return f"Ключ с максимальным значением: {max_key}"
        else:
            return "Словарь пуст"
    elif isinstance(input_arg, list):
        count = 0
        for item in input_arg:
            if item < 0:
                break
            count += 1
        return f"Количество элементов до первого отрицательного: {count}"
    elif isinstance(input_arg, int):
        if input_arg < 2:
            return "Число не является простым"
        for i in range(2, int(input_arg**0.5) + 1):
            if input_arg % i == 0:
                return "Число не является простым"
        return "Число является простым"
    elif isinstance(input_arg, str):
        reversed_str = input_arg[::-1]
        digit_sum = sum(int(char) for char in input_arg if char.isdigit())
        return f"Строка в обратном порядке: {reversed_str}, Сумма цифр в строке: {digit_sum}"
    else:
        return "Неизвестный тип аргумента"

#Примеры использования:
input_arg_dict = {'a': 5, 'b': 10, 'c': 3}
print(process_input(input_arg_dict))

input_arg_list = [1, 2, 3, -1, 4, 5]
print(process_input(input_arg_list))

input_arg_int = 17
print(process_input(input_arg_int))

input_arg_str = "12345"
print(process_input(input_arg_str))