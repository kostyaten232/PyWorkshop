a = 'Fight Club'
b = 'David Fincher'           
с = '1999'
print(f' {a}')
print(f'  {b}')
print(f'  {с}')
print('{2} {1} {0}'.format('1999', 'David Fincher', 'Fight Club'))





a = 'serendipity'
print(f' {a}')
b = 'serendipity has 11 letters'
print(f' {b}')



nums = [n * 2 for n in range(1, 21)]
print(nums)
print(nums[2:7])

str1 = 'Python is not just a mere snake'
print(str1[10:18])

print(str1[::-1])
print(str1[7::])

new_str = str1[:]
print(new_str)

my_list = ['Java', 'Python', 'Kotlin']
print(my_list[:2])
print(my_list[:99999999])





# !!NEVER DO THIS
def my_func(a, lst=[]):
  pass

# +DO THIS
def my_func(a):
  lst = []
  



stock = []
for i in range(7):
  for j in range(i, 7):
    stock.append([i, j])



stock = [[i, j] for i in range(7) for j in range(i, 7)]




from random import randint
lst = [randint(0, 10) for _ in range(10)]
lst.sort()
print(lst)
mx = 0
for n in lst:
  if n > mx:
    mx = n

print(mx)




from random import randint
lst = [randint(0, 10) for _ in range(10)]
lst.sort()
print(lst)
mx = 0
for n in lst:
  if n > mx:
    mx = n

print(mx)




from random import randint
lst = [randint(0, 10) for _ in range(10)]
lst.reverse()
print(lst)
mn = 0
for n in lst:
  if n < mn:
    mn = n

print(mn)



hard




no




1)We look for the middle in the array 
2)Take any number and add 1 to it. 
2.1)If the number turns out to be less than or equal to any number, then this is not the maximum number.
2.2)If there is no number <= number +1, then this is the maximum number.


1. creating an array with random numbers;
2. Sorting the numbers;
3.Creating a condition






# map

  

nums = [n for n in range(10)]
# double_n = [n * 2 for n in nums]
print(nums)
# print(double_n)

def doubler(x):
  return x * 2

double_numbers = list(map(doubler, nums))
print(double_numbers)

a, b = map(int, (input(), input()))
print(a, b)





nums = [n for n in range(10)]
# # double_n = [n * 2 for n in nums]
# print(nums)
# # print(double_n)

# def doubler(x):
#   return x * 2

# double_numbers = list(map(doubler, nums))
# print(double_numbers)

# a, b = map(int, (input(), input()))
# print(a, b)


double_numbers = list(map(lambda x: x * 2, nums))

print(double_numbers)






double_numbers = list(map(lambda x: x * 2, nums))

print(double_numbers)


x_list = [1, 2, 4]
y_list = [4, 6, 8]
z_list = [9, 10, 10]

res = list(map(lambda x, y, z: x + y + z, x_list, y_list, z_list))
print(res)






#filter

odd_numbers = list(filter(lambda x: x % 2, nums))
print(odd_numbers)




# map / takes a func





# -----------
nums = [n for n in range(10)]
double_nums = [n * 2 for n in nums]
print(nums)
print(double_nums)

# -----------
def doubler(x):
  return x * 2

double_numbers = list(map(doubler, nums))
print(double_numbers)

# -----------
a, b = map(int, (input(), input()))
print(a, type(a), b, type(b))

# -----------
double_numbers = list(map(lambda x: x * 2, nums))
print(double_numbers)

# -----------
x_list = [1, 2, 4]
y_list = [4, 6, 8]
z_list = [9, 10, 10]

res = list(map(lambda x, y, z: x + y + z, x_list, y_list, z_list))
print(res)


#filter / takes a Boolean func (True or False)
odd_numbers = [n for n in nums if n % 2]
print(odd_numbers)

# -----------
odd_numbers = list(filter(lambda x: x % 2, nums))
print(odd_numbers)

#--------------------------------------------------
# map and filter can be replaced with list comprehention
# which is more PYTHONIC yet
# map and filter are generally more efficient and faster







from string import ascii_uppercase

print(ascii_uppercase)






word2 = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'l', 'a', 'n', 'g', "u", "a", "g", "e"]
print(word2[2])
print(word2[5])
print(word2[8])
print(word2[15])
print(word2[16])
print(word2[18])






# iterators

# iterators use dunders __iter()__ & __next()__

my_list = [1, 2, 3]
my_iter = iter(my_list)  # turn list to generator
print(my_iter)
print(next(my_iter))  # get intance in generator
print(next(my_iter))  # get next intance in generator till error

for a in my_list:  # same concept
  print(a)


# zip

names = ['Mary', 'Ann']
surnames = ['Smith', 'Boul']
for name, surname in zip(names, surnames):
  print(name, surname)

names = ['Mary', 'Ann', 'Bob']
surnames = ['Smith', 'Boul']
for name, surname in zip(names, surnames):  # stops at shortest
  print(name, surname)

# from python 3.10 you can make sure lists are identical in length
names = ['Mary', 'Ann', 'Bob']
surnames = ['Smith', 'Boul']
for name, surname in zip(names, surnames, strict=True):  # throws error
  print(name, surname)
  
# enumerate
  
names = ['Mary', 'Ann', 'Bob']

i = 1
for name in names:
  print(i, name)

for i, name in enumerate(names):
  print(i + 1, name)
# or
for i, name in enumerate(names, start=1):
  print(i, name)










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





import sys

a = 5
b = 2

try:
  resalt = a / b
except Exciption as err:
  type, obj, tr = sys.exc_info()
  line = tr.tb_lineno
  print('Error', err.__class__.__name__, line)
else:
  print('The result is ', resalt)
finally:
  print("Thank you for using the service")