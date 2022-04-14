'''Python Workshop DAY 3
1 Project Stage 2 (enumerate!!)
2 Binary Search!!!
3 Primes - new (folder 06)
4 Exceptions and Handlers- Theory and Practice
'''



print('Hello')
print(10 / 0)  # code goes till first exception

# typical

# NameError
a = 5; print(a + b)  # b is not defined before call

# TypeError
print('15' + 2)  # operation or func is applied to OBJ of wrong type

# ValueError
print(int('five'))  # OBJ type is ok but value inappropriate

# PYTHON exception tree
# BaseException
#  +-- SystemExit
#  +-- KeyboardInterrupt
#  +-- GeneratorExit
#  +-- Exception
#       +-- StopIteration
#       +-- StopAsyncIteration
#       +-- ArithmeticError
#       |    +-- FloatingPointError
#       |    +-- OverflowError
#       |    +-- ZeroDivisionError
#       +-- AssertionError
#       +-- AttributeError
#       +-- BufferError
#       +-- EOFError
#       +-- ImportError
#       |    +-- ModuleNotFoundError
#       +-- LookupError
#       |    +-- IndexError
#       |    +-- KeyError
#       +-- MemoryError
#       +-- NameError
#       |    +-- UnboundLocalError
#       +-- OSError
#       |    +-- BlockingIOError
#       |    +-- ChildProcessError
#       |    +-- ConnectionError
#       |    |    +-- BrokenPipeError
#       |    |    +-- ConnectionAbortedError
#       |    |    +-- ConnectionRefusedError
#       |    |    +-- ConnectionResetError
#       |    +-- FileExistsError
#       |    +-- FileNotFoundError
#       |    +-- InterruptedError
#       |    +-- IsADirectoryError
#       |    +-- NotADirectoryError
#       |    +-- PermissionError
#       |    +-- ProcessLookupError
#       |    +-- TimeoutError
#       +-- ReferenceError
#       +-- RuntimeError
#       |    +-- NotImplementedError
#       |    +-- RecursionError
#       +-- SyntaxError
#       |    +-- IndentationError
#       |         +-- TabError
#       +-- SystemError
#       +-- TypeError
#       +-- ValueError
#       |    +-- UnicodeError
#       |         +-- UnicodeDecodeError
#       |         +-- UnicodeEncodeError
#       |         +-- UnicodeTranslateError
#       +-- Warning
#            +-- DeprecationWarning
#            +-- PendingDeprecationWarning
#            +-- RuntimeWarning
#            +-- SyntaxWarning
#            +-- UserWarning
#            +-- FutureWarning
#            +-- ImportWarning
#            +-- UnicodeWarning
#            +-- BytesWarning
#            +-- EncodingWarning
#            +-- ResourceWarning

#NOTE!!

# if using parent name it will cover ALL exception in it
# so 
# RuntimeError will include both exceptions in it
# Handling Exceptions

# list
# https://docs.python.org/3/library/exceptions.html

a = 5
b = 2


try:
  result = a / b
except ZeroDivisionError:
  print('Error')
else:
  print('The result is ', result)
finally:
  print("Thank you for using the service")




# Handling Exceptions

# list
# https://docs.python.org/3/library/exceptions.html

# Handling Exceptions

# list
# https://docs.python.org/3/library/exceptions.html
import sys


a = 5
b = 0


try:
  result = a / b
except Exception as err:
  print('Error', err.__class__.__name__)
else:
  print('The result is ', result)
finally:
  print("Thank you for using the service")









# Handling Exceptions

# list
# https://docs.python.org/3/library/exceptions.html
import sys


a = 5
b = 0


try:
  result = a / b
except Exception as err:
  type, obj, tr = sys.exc_info()
  line = tr.tb_lineno
  print('Error', err.__class__.__name__, line)
else:
  print('The result is ', result)
finally:
  print("Thank you for using the service")







# Handling Exceptions

# list
# https://docs.python.org/3/library/exceptions.html

a = 5
b = 2

print(a / b)  # work as expected


a = 5
b = 0

print(a / b)  # ZeroDivision

# solution
try:
  result = a / b
except ZeroDivisionError as err:
  print('0 Error', err)  # err is exception description
else:
  print('The result is ', result)
finally:
  print("Thank you for using the service")

  
a = 5
b = 'five'

print(a / b)  # TypeError

# solution
try:
  result = a / b
except ZeroDivisionError as err:
  print('0 Error', err)  # err is exception description
except TypeError as err:
  print('T Error', err)  # err is exception description
else:
  print('The result is ', result)
finally:
  print("Thank you for using the service")

# line num of exception
import sys 
e_type, e_object, e_traceback = sys.exc_info()
e_line = e_traceback.tb_lineno


# exception name
# use __class__.__name__ called on err object

# multiple exceptions
# except (ZeroDivisionError, TypeError) as err:




# Binary Search

from random import randint as rr

n = 20
array = [n for n in range(n + 1)]

print(array)

def rotate(array):
  for _ in range(rr(1, len(array))):
    # array.append(array.pop(0))
    array.insert(0, array.pop())
  return array

array = rotate(array)

print(array)