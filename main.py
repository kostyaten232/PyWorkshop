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