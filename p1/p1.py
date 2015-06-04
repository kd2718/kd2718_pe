# problem 1 project euler
k = []
# (k.append(x) for x in range(1000) if x % 3 == 0 or x % 5 == 0)
for x in range(1000):
    if x % 3 == 0 or x % 5 == 0:
        k.append(x)
print k
print sum(k)
