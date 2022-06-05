""" 
    Игра "Угадай число".
    Компьютер сам загадывает и сам угадывает число.
"""

import numpy as np

def random_predict(left_limit:int=1, right_limit:int=100, number:int=1)->int:
    """Функция для угадывания числа

    Args:
        left_limit (int, optional): левая граница диапазона поиска загаданного числа. Defaults to 1.
        right_limit (int, optional): правая граница диапазона поиска загаданного числа. Defaults to 100.
        number (int, optional): загаданное число. Defaults to 1.

    Returns:
        int: число попыток угадывания числа. Ноль (0), если число не угаданно.
    """
    
    # Количество попыток
    count = 0
    
    # Максимально допустимое число попыток
    max_count = right_limit - left_limit + 1
    
    # Цикл по угадыванию числа.
    # Цикл выполянется, пока не будет угадано число, либо пока не будет достигнуто максимальное число попыток.
    while True:
        count += 1
        # Выбираем новое число
        predict_number = np.random.randint(left_limit, right_limit + 1)
        # Если число меньше загаданного числа, смещаем левую границу поиска.
        if predict_number < number:
            left_limit = predict_number
        # Если число больше загаданного числа, смещаем правую границу поиска.
        elif predict_number > number:
            right_limit = predict_number
        # Угадали число. Выходим из цикла поиска.
        elif  predict_number == number:
            break
        # Защита от бесконечного цикла: перебрали все числа из допустимого диапазона, но не угадали число.
        if count >= max_count:
            return(0)
    
    return(count)

def score_game(random_predict)->int:
    """Функция вычисляет, за какое среднее число попыток функция random_predict угадывает число. Используется 1000 проходов.

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее число попыток угадывания числа. Ноль (0), если число не угаданно.
    """
    
    # Список для хранения результатов работы функции random_predict
    count_list = []
    
    #
    np.random.seed(1)
    
    # Левая граница диапазона загадывания числа.
    left_limit = 1
    
    # Правая граница диапазона загадывания числа.
    right_limit = 100
    
    # Заполняем массив загадываемых чисел рандомными числами. Разммер массива 1000 элементов.
    random_array = np.random.randint(left_limit, right_limit + 1, size=(1000))
    
    # Для каждого числа из массива рандомных чисел угадываем число и 
    #  добавляем результат в список.
    for number in random_array:
        count_list.append(random_predict(left_limit, right_limit, number))
    
    # Вычисляем среднее число попыток. Срднее число попыток - целое число.
    score = int(np.mean(count_list))
    
    # Выводим результаты работы функции.
    if score != 0:
        print(f"Ваш алгоритм угадывает числов среднем за {score} попыток")
        return(score)
    else:
        print("Ошибка! Не удалось угадать число:(")
        return(0)

# RUN
if __name__ == '__main__':
    score_game(random_predict)
