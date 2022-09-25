# Все равны, как на подбор. 
# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики,
# и возвращает True, если это так. Если значение характеристики для
# разных объектов отличается – то False. Для пустого набора объектов,
# функция должна возвращать True. Аргумент characteristic – это функция,
# которая принимает объект и вычисляет его характеристику.


def same_by(characteristic, objects):
    try:
        return len(set(map(characteristic, objects))) == 1 if objects else True
    except:
        print('Некорректный ввод')


objects = [2, 4, 6, 8]

print(same_by(lambda x: x % 2, objects))
