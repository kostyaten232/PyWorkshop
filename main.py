P = int (input ('Введите число: '))
 
for d in range (1, P // 2 + 1) :
  if P % d == 0 :
    print (d, ' ', sep = '', end = '')
print (P)