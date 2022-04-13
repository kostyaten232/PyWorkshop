# % foramatting
print('%.3f' % (11 /  3))
name = 'Mary'; age = 15
print('Hi %s you are %d' % (name, age))

# .format()
print('{} {} {}'.format('Me', 'and', 'You'))
print('{who} {} {}'.format('Me', 'and', who='You'))
print('{who} {} {}'.format('Me', 'and', who='You'))
print('{2} {1} {0}'.format('Me', 'and', 'You'))

# f'{var]'
a = 5
print(f'%.{a}f' % (11 /  3))
name = 'Jonny Cage'
print(f'This is the end of you, {name}')



x_list = [ 46, 28, 34, 27, 33, 43, 25, 36, 19, 39, 43, 37, 49]
y_list = [38, 44, 31, 33, 47, 49, 42, 39, 47, 45, 31, 34, 49]
z_list = [ 28, 28, 35, 42, 27, 41, 43, 39, 46, 37, 49,  34, 29]
res = list(map(lambda x, y, z: x + y + z, x_list, y_list, z_list))
print(res)

studens_list = ['Денис - 112', 'Дима - 100', 'Ваня - 100', 'Дима - 102', 'Дима - 107', 'Лёха - 133', 'Вова - 110', 'Вадим - 114', 'Богдан - 112', 'Юра - 121', 'Антон - 123', 'Артем - 105', 'Костя - 127']
print(studens_list)