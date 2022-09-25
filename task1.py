# Мимикрия. У вас есть код, который вы не можите менять:

# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformated_values = list(map(transformation, values))

# Единственный способ вашего взаимодействия с этим кодом - 
# посредством задания функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно 
# никак преобразоывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, 
# чтобы transformated_values получился копией values. 


transformation = lambda x: x
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformated_values = list(map(transformation, values))
if values == transformated_values:
    print('ok')
else:
    print('fail')
