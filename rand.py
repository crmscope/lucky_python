import random
a = 0 
b = 0 
i = 0
while i < 1000:
    a = a + random.randint(1,2) 
    b = b + random.randint(1,2)     
    i += 1

print("a: ", a)
print("b: ", b)