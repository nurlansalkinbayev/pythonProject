# Теплоемкость

# C - Это удельная телоемкость материала (Вода)
C_WATER = 4.186
E_PRICE = 8.9
# Начальная температура воды t1
t1 = int(input('Начальная температура воды: '))
# Конечная температура воды t2
t2 = int(input('Конечная температура воды: '))
# Масса воды в граммах
m = int(input('Масса воды в граммах: '))
# Вычисляем количество энергии q
q = (m * C_WATER * (t2 - t1)) / 1000
print(f'Количество энергии равно {q} кДж.')
# Перевод 1 кДж в 1 кВт 1kJ = 0.000277kWh
q_kWh = q * 0.0000277
# Расчет в центах 1 кВт = 8.9 центов
cost = q_kWh * E_PRICE
# Вывод результата
print(f'Стоимость нагрева составляет {cost}.')
