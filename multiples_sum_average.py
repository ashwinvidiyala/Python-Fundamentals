# Multiples

# Part 1: Print odd numbers from 1 to 1000
for x in range(1,1000):
    if x % 2 is not 0:
        print x

# Part 2: Print all multiples of 5 from 5 to 1,000,000
for x in range(5,1000000):
    if x % 5 is 0:
        print x

#Sum list & Average List
a = [1, 2, 5, 10, 255, 3]
sum = 0
for x in a:
    sum = sum + x
print sum
average = sum/(len(a))
print average
