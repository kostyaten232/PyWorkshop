student1 = ['Денис - 46', 'Дима - 28', 'Ваня - 34', 'Дима - 27', 'Дима - 33', 'Лёха - 43', 'Вова - 25', 'Вадим - 36', 'Богдан - 19', 'Юра - 39', 'Антон - 43', 'Артем - 37', 'Костя - 49']



student2 = ['Денис - 38', 'Дима - 44', 'Ваня - 27', 'Дима - 33', 'Дима - 47', 'Лёха - 49', 'Вова - 42', 'Вадим - 39', 'Богдан - 47', 'Юра - 45', 'Антон - 31', 'Артем - 34', 'Костя - 49']



student3 = ['28', '28', 'Ваня - 35', 'Дима - 42', 'Дима - 27', 'Лёха - 41', 'Вова - 43', 'Вадим - 39', 'Богдан - 46', 'Юра - 37', 'Антон - 49', 'Артем - 34', 'Костя - 29']

from random import randint
lst = [randint(0, 100) for _ in range(100)]
lst.sort()
if lst/5 or lst


Денис - 1
Дима - 2
Ваня - 3
Дима - 4
Дима - 5
Лёха  - 6
Вова - 7
Вадим - 8
Богдан  - 9
Юра - 10
Антон - 11
Артем - 12
Костя - 13




# Default Dict and Counter

text = '''I've become so numb
I can't feel you there
Become so tired
So much more aware
I'm becoming this
All I want to do
Is be more like me
And be less like you
And I know
I may end up failing too
But I know
You were just like me with someone disappointed in you'''

text_list = text.split()

# setdefault
freq_dict = {}
for word in text_list:
  freq_dict.setdefault(word, 0)
  freq_dict[word] += 1

print(freq_dict)
print(freq_dict['AAAAAAAAA'])  # KeyError / Not Added

index_dict = {}
for index, word in enumerate(text_list):
  index_dict.setdefault(word, []).append(index)

print(index_dict)

# default dict
from collections import defaultdict

freq_ddict = defaultdict(int)

for word in text_list:
  freq_ddict[word] += 1

print(freq_ddict)
print(freq_ddict['AAAAAAAAA'])  # No Error / Missing value is added
print(freq_ddict)  # See it added to Dict
  
freq_dict = defaultdict(list)

# Counter
from collections import Counter

freq_counter = Counter(text_list)

print(freq_counter)  # use it like normal dict
print(freq_counter.most_common)
print(freq_counter.most_common(2))



my_dict = {
  1: 'low',
  5: 'high'
}

print(my_dict.items())

rev_dict = {v: k for k, v in my_dict.items()}

print(rev_dict)


stock = [[2, 1], [2, 3]]

weights = {
  0: 7,
  1: 8
}

max_value = max(weights.values())
print(max_value)

rev_weights = {v: k for k, v in weights.items()}

max_key = stock[rev_weights[max_value]]
print(max_key)











stock = ()
stock = [[0, 6], [3, 4], [1, 4], [4, 5], [3, 5], [1, 2], [1, 3], [0, 1], [5, 6], [6, 6], [0, 4], [1, 1], [2, 3], [0, 3], [3, 3], [2, 4], [1, 5], [2, 6], [3, 6], [0, 2], [4, 4]]

count = 0

weights = {
  0: (count == sum(map(lambda item: item == 0, stock))
        print('0:', count)),
  1: 7,
  2: 5,
  3: 8,
  4: 7,
  5: 4,
  6: 6
}

max_value = max(weights.values())
print(max_value)

rev_weights = {v: k for k, v in weights.items()}

max_key = stock[rev_weights[max_value]]
print(max_key)





'hello'.encode()
data = data.decode()

import socket


with socket.socket() as client_socket:

  hostname = '127.0.0.1'
  port = 5000
  
  client_socket.connect((hostname, port))
  
  data = 'Wake up Neo'
  
  client_socket.send(data.encode())
  
  buffer = 1024
  response = client_socket.recv(buffer)
  response = response.decode()
  
  print(response)




from functools import reduce
from collections import Counter


stock = [[0, 6], [3, 4], [1, 4], [4, 5], [3, 5], [1, 2], [1, 3], [0, 1], [5, 6], [6, 6], [0, 4], [1, 1], [2, 3], [0, 3], [3, 3], [2, 4], [1, 5], [2, 6], [3, 6], [0, 2], [4, 4]]


new_stock = reduce(lambda x, y: x + y, stock)
print(new_stock)


new_new_stock = [item for sublist in stock for item in sublist]
print(new_new_stock)





from functools import reduce
from collections import Counter


stock = [[0, 6], [3, 4], [1, 4], [4, 5], [3, 5], [1, 2], [1, 3], [0, 1], [5, 6], [6, 6], [0, 4], [1, 1], [2, 3], [0, 3], [3, 3], [2, 4], [1, 5], [2, 6], [3, 6], [0, 2], [4, 4]]


new_stock = reduce(lambda x, y: x + y, stock)
print(new_stock)

counter = Counter(new_stock)
print(counter[0])

print('Count:'
    
    '0:'print(counter[0])
    '1:'
  print(counter[1)]
    '2:'
    '3:'
    '4:'
    '5:'
    '6:'
)




pcs = [2, 4]

summ = 0
for e in pcs:
  summ += counter[e]

print(summ)
