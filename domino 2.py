from random import randint, shuffle

stock = [[i, j] for i in range(7) for j in range(i, 7)]
doubles = stock[:-4:-2]
on_hands = 7

while not any([double in stock[:on_hands * 2] for double in doubles]):
    shuffle(stock)

for double in doubles:
    if double in stock[:on_hands * 2]:
        snake = stock.pop(stock.index(double))
        break

computer, player = stock[on_hands - 1], stock[on_hands - 1:on_hands * 2 - 1]
if randint(1, 2) == 2:
    player, computer = computer, player

stock = stock[on_hands * 2 - 1:]

print('=' * ord ('F'))
print('Stock size: %s\nComputer pieces: %s\n\n%s\n' % (len(stock), len(computer), snake))
print('Your pieces:\n{}'.format('\n'.join(list(f'{i + 1}:{e}' for i, e \
                                               in enumerate (list (map (str, ([pcs for pcs in player]))))))))
print(''.join(chr(n) for n in [83, 116, 97, 116, 117, 115, 58]), end=' ')
print('Computer is about to make a move. Press enter to continue...' if
     len(computer) > len(player) else \
     'It\'s your turn to make a move. Enter your command.')



