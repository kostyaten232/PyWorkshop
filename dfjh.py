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