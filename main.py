import random
# Создание списка чисел из заданного интервала с указанным количеством
deck = list(range(1000, 9999))
hand = random.sample(deck, k=100)
# Сумма чисел в списке
# hand_sum = sum(hand)
# print(hand)
# print(hand_sum)

# Открываем файлы для записи четных и нечетных чисел
with open("четные.txt", "w") as even_file, open("нечетные.txt", "w") as odd_file:
    # Перебираем числа в списке
    for number in hand:
        # Проверяем, является ли число четным
        if number % 2 == 0:
            # Если число четное, записываем его в файл для четных чисел
            even_file.write(str(number) + "\n")
        else:
            # Если число нечетное, записываем его в файл для нечетных чисел
            odd_file.write(str(number) + "\n")
