
import random  # импортируем модуль random для генерации случайных чисел

# Функция генерирует nxm массив случайных чисел до max_value, у которого
# стандартное значение 20
def random_array(n, m, max_value=50):
    array = []  # инициализируем массив
    # Цикл for. Оператор range выдает диапазон чисел, в данном случае
    # от 0 до n-1
    for i in range(0, n):
        sub_array = []  # инициализируем подмассив
        # Если передать range один аргумент, то нижняя граница 0, в данном
        # случае диапазон чисел будет от 0 до m-1
        for j in range(m):
            # Генерируем слуйчаное число от 0 до 50 и добавляем его в подмассив
            number = random.randint(1, max_value)
            sub_array.append(number)
        # Добавляем полученный подмассив в основной массив
        array.append(sub_array)
    return array  # возвращаем массив из случайных чисел


def print_array(array):  # функция выводит массив в удобочитаемой форме
    print()  # переход на новую строку
    # Циклу for также можно давать массивы, тогда перебирается каждый элемент
    for i in array:
        # Так как массив состоит из подмассивов, тогда каждый элемент тоже
        # можно перебрать используя цикл for
        for j in i:
            print("%d\t" % j, end='')  # выводим каждое значение и табуляцию
        print()  # переход на новую строку


def main():
    array = random_array(4, 5)  # заполняем массив случайными числами
    print_array(array)  # выводим массив на экран
    # Бесконечный цикл while, который закончится только при помощи break

    while True:
        print  # переход на новую строку
        print("1. Заполнить массив случайными числами;")
        print("2. Выполнить задание;")
        print("3. Выход.")
        # Получаем ввод команды от пользователя
        key = input('Введите команду (1, 2 или 3): ')
        if key == '1':  # если команда 1, то заполняем массив заново
            array = random_array(4, 5)
            print_array(array)


            # После этого условия цикл начнется с начала
        elif key == '2':
            l = 0
            max  = array[0][0]
            min = array[0][0]
            sum = 0

            for col, r in enumerate(array): # перебираем каждую строку
                for row, ceil in enumerate(r):
                    print(ceil, end = ' ')
                    if(ceil > max):
                        max = ceil
                    if(ceil < min):
                        min = ceil
                    if (ceil > 0):
                        sum = sum + ceil
                print()

            if sum != 0:

                for i in range(len(array)):  # перебор каждую строку
                    while True:  # цикл нужен, так как макс/мин не одни в массиве
                        try:
                            index_max = array[i].index(max)
                            array[i][index_max] /= 2
                            round(index_max)
                        except ValueError:
                            break
                for i in range(len(array)):
                    while True:
                        try:
                            index_min = array[i].index(min)
                            array[i][index_min] /= 3
                            round(index_min)
                        except ValueError:
                            break
        elif key == '3':
            exit(0)


if __name__ == '__main__':
    main()