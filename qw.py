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

]

x_list = [ 46, 28, 34, 27, 33, 43, 25, 36, 19, 39, 43, 37, 49]
y_list = [38, 44, 31, 33, 47, 49, 42, 39, 47, 45, 31, 34, 49]
z_list = [ 28, 28, 35, 42, 27, 41, 43, 39, 46, 37, 49,  34, 29]
res = list(map(lambda x, y, z: x + y + z, x_list, y_list, z_list))
print(res)

studens_list = ['Денис - 112', 'Дима - 100', 'Ваня - 100', 'Дима - 102', 'Дима - 107', 'Лёха - 133', 'Вова - 110', 'Вадим - 114', 'Богдан - 112', 'Юра - 121', 'Антон - 123', 'Артем - 105', 'Костя - 127']
print(studens_list)
]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]]\]\]\]\]\]\]\]\]\]\]\]]\]\]\


nums = [n for n in range(100)]

for n in nums:
  if n % 6 == 1 or n % 6 == 5:
    print(n, 'possible prime')
  else:
    print(n, 'not prime')

nums = [n for n in range(1000)]

for n in nums:
  i = 0
  if n % 6 == 1 or n % 6 == 5:
    print(n, 'possible prime')
    i += 1
print(i)
  # else:
  #   print(n, 'not prime')

]]\]\]\]\]\]]\]\]\]\]\]\]\]]\]\]\]\]\]\]\]]\]\]\

from time import perf_counter

nums = [n for n in range(10000)]
i = 0

start = perf_counter()
for n in nums:
  
  if n % 6 == 1 or n % 6 == 5:
    print(n, 'possible prime')
    i += 1
print(i)
print(perf_counter() - start, 'secs')
  # else:
  #   print(n, 'not prime')

]\]\]\]\]\]\\]]\\]]\]\]\]\]\]\]\]\]\]\]\


def binary(arr, low, high):
  i = 1
  while 55 < 66:
    if arr[low] < arr[high]:
      return arr[high], i
    mid = (low + high) // 2
    if arr[mid] > arr[mid + 1]:
      return arr[mid], i
    if arr[mid] > arr[high]:
      low = mid + 1
    elif arr[mid] < arr[high]:
      high = mid - 1
    i += 1
  return None

]\]\]\]\]\]\]\]\]\]\]\]\]]]]\]\]\]\]\

# Binary Search

from random import random as rr
from linear import linear
from binary import binary


n = 10_000
array = [n for n in range(n + 1)]


def rotate(array):
  for _ in range(rr(1, len(array))):
    array.append(array.pop(0))
    array.insert(0, array.pop())
  return array

array = rotate(array)


print(linear(array))
print(binary(array, 0, len(array) - 1))


\]\]\\]\]\]\]\]\]\]\]\]\]\]\]\]\]\
from wrapper import get_time


@get_time
def binary(arr, low, high):
  i = 1
  while 55 < 66:
    if arr[low] < arr[high]:
      return arr[high], i
    mid = (low + high) // 2
    if arr[mid] > arr[mid + 1]:
      return arr[mid], i
    if arr[mid] > arr[high]:
      low = mid + 1
    elif arr[mid] < arr[high]:
      high = mid - 1
    i += 1
  return None

\]\]\]]\\]\]]\]\]\]\]\\]\]\]\]\]\]\]\]\]\]\]\]\]\]\\]\]\]]\]\\]


from wrapper import get_time


@get_time
def linear(arr):
  i = 1
  for num in arr:
    i += 1
    if num > arr[arr.index(num) + 1]:
      return num, i
  return None


from time import perf_counter


def get_time(func):
  def wrapper(*args):
    start = perf_counter()
    res = func(*args)
    end = perf_counter()
    return res, '%.10f' % (end - start)
  return wrapper



\]\]\]\]]]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\\]\]\]\]\]]\]\]\


# DAY 5

# Chunks
# Custom Exceptions
# Wrappers
# Two Pointer method
# Domino Stage 3
# snake = [[2, 3], [3, 4], [5, 6], [7, 8]]
# print(list(map(str, snake[:2])))
# print(*snake, sep='...')


# def example_exceptions_1(x, y):
#   if y == 0:
#     raise ZeroDivisionError('the dem is 0')
#   elif y < 0:
#     raise Exception('the dom is neg')
#   else:
#     print(x / y)

# example_exceptions_1(10, 5)

class NegativeResultException(Exception):
  pass
  


def example_exceptions_2(a, b):
  try:
    c = a / b
    if c < 0:
      raise NegativeResultException
    else:
      print(c)
  except NegativeResultException:
    print('there is a neg result')

example_exceptions_2(10, 5)
raise NegativeResultException






]\]\]\]\]\]\]\]\]\]\]\]\]\]\]]\]\]\]\]\]\]\]\]\]\]\]\]





# DAY 5

# Chunks
# Custom Exceptions
# Wrappers
# Two Pointer method
# Domino Stage 3
# snake = [[2, 3], [3, 4], [5, 6], [7, 8]]
# print(list(map(str, snake[:2])))
# print(*snake, sep='...')

# def example_exceptions_1(x, y):
#   if y == 0:
#     raise ZeroDivisionError('the dem is 0')
#   elif y < 0:
#     raise Exception('the dom is neg')
#   else:
#     print(x / y)

# example_exceptions_1(10, 5)


class OutOfBoundsException(Exception):
    d


class LessthanOneException(Exception):
    pass


def example_exceptions_3(x):
    try:
        if 3 < x < 30:
            raise OutOfBoundsException
        elif x < 1:
            raise LessthanOneException
        else:
            print(x)
    except OutOfBoundsException:
        print('x should not be from 3 to 30')
    except LessthanOneException:
        print('x should not be less than 1')


example_exceptions_3(50)


]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]\]]\]\]\]\


# DAY 5

# Chunks
# Custom Exceptions
# Wrappers
# Two Pointer method
# Domino Stage 3
# snake = [[2, 3], [3, 4], [5, 6], [7, 8]]
# print(list(map(str, snake[:2])))
# print(*snake, sep='...')

# def example_exceptions_1(x, y):
#   if y == 0:
#     raise ZeroDivisionError('the dem is 0')
#   elif y < 0:
#     raise Exception('the dom is neg')
#   else:
#     print(x / y)

# example_exceptions_1(10, 5)


class OutOfBoundsException(Exception):
    def __init__(self, x):
      self.message = f'{x} can not be processed'
      super().__init__(self.message)


def example_exceptions_4(x):
    try:
        if 3 < x < 30:
            raise OutOfBoundsException(x)
        else:
            print(x)
    except OutOfBoundsException as err:
        print(err)



example_exceptions_4(10)



\]]\]\]\]\]\]\]\]\]]\]]]\]]\]\]\]\\]]]\]]\]\]\]\]\\]\]\\]]\]]\]\]\]\]\]\]\]\]\]\
# Custom Exceptions

# specifying message in arg
def example_exceptions_1(x, y):
  if y == 0:
    raise ZeroDivisionError('the dem is 0')
  elif y < 0:
    raise Exception('the dom is neg')
  else:
    print(x / y)

example_exceptions_1(10, 0)
example_exceptions_1(10, -1)


# raising with try/except
class NegativeResultException(Exception):
  pass
  
def example_exceptions_2(x, y):
  try:
    z = x / y
    if z < 0:
      raise NegativeResultException
    else:
      print(z)
  except NegativeResultException:
      print('res is negative')

example_exceptions_2(10, -1)

# raising several exceptions
class NegativeResultException(Exception):
  pass

class DenomOutOfBoundsException(Exception):
  pass
  
def example_exceptions_3(x, y):
  try:
    z = x / y
    if z < 0:
      raise NegativeResultException
    elif 1 < y < 10:
      raise DenomOutOfBoundsException
    else:
      print(z)
  except NegativeResultException:
      print('res is negative')
  except DenomOutOfBoundsException:
      print('denom can not be = from 2 to 9')

example_exceptions_3(10, -1)
example_exceptions_3(10, 4)

# by __str__ dunder
class OutOfBoundsException(Exception):
    def __str__(self):
      self.message = f'x can not be processed'
  

def example_exceptions_4(x):
