import random
a = 0 
b = 0 
c = 0 
i = 0
while i < 10000:
    a = a + random.randint(1,3) 
    b = b + random.randint(1,3) 
    c = c + random.randint(1,3)
    i += 1

print("a: ", a)
print("b: ", b)
print("c: ", c)
