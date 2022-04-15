def get_prime_divs(n):
  res = []
  for i in range(2, int(n ** 0.5) + 1):
    while not n % i:
      if not i in res:
        res.append(i)
      n //= i
    if n < i:
      break
  if n > 1:
     res.append(n)
  return res

n = 999_999_937
start = perf_counter()
print(get_prime_divs(n))
print(perf_counter() - start)





# from time import perf_counter

# def get_primes(n):
#   primes = [2, 3]
#   for i in range(5, n + 1):
#     if i % 6 in (1, 5):
#       prime = True
#       for j in range(2, int(i ** 0.5) + 1):
#         if not i % j:
#           prime = False
#           break
#       if prime:
#         primes.append(i)
#   return primes


# n = 100_000
# start = perf_counter()
# primes = get_primes(n)
# print(perf_counter() - start)
# print(primes)


