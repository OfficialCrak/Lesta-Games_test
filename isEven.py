from decorator import time_it


@time_it
def isEven(value):
    return value % 2 == 0


"""
Прироста к скорости такой метод ничего не даст, станеть чуть медленнее из-за дополнительного запуска isinstance, но код
с типизацией легче читать и понимать (что приходит на вход, что получаем), также проверка на тип повышает надежность функции
от поломки при получении недопустимого типа
"""
@time_it
def isEven_upgrade(value: int) -> bool:
    if not isinstance(value, int):
        raise TypeError(f"Ошибка типа входного числа, полученный тип: {type(value).__name__}")
    return value % 2 == 0
