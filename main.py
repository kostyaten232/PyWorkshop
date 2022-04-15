N = int (input ('Введите число: '))
 
for d in range (1, N // 2 + 1) :
  if N % d == 0 :
    print (d, ' ', sep = '', end = '')
print (N)