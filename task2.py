# Самая далекая планета. Планеты вращаются вокруг звезд по эллептическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию, find_farthest_orbit(list_of_orbits), которая среди списка
# орбит планет найдет ту, по которой вращается самая далекая планета.
# Круговые орбиты не учитывайте. Результатом функции должен быть кортеж,
# содержащий длины полуосей эллипса орбиты самой далекой планеты.

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]


# def find_farthest_orbit(orbits):
#     return [i for i in orbits if i[0] * i[1] == max(map(lambda x: (x[0] != x[1]) * x[0] * x[1], orbits))]


# print(*find_farthest_orbit(orbits))


print(*max(orbits, key=lambda x: (x[0] != x[1]) * x[0] * x[1]))