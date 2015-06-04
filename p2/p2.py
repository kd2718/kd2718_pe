# p2 project euler
# filter(lambda x: x % 2 == 0, range(10))

fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)
limit = 40
print map(fib,range(limit))
print filter(lambda x: x % 2 == 0, map(fib,range(limit)))
print sum(filter(lambda x: x % 2 == 0 and x < 4000000, map(fib,range(limit))))
