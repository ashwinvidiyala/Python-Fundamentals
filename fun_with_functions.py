# Odd_Even Function
def odd_even(end):
    odd_or_even = ""
    for x in range(1,end+1):
        if x % 2 == 0:
            odd_or_even = 'even'
            print "Number is {}. This is an {} number.".format(x, odd_or_even)
        else:
            odd_or_even = 'odd'
            print "Number is {}. This is an {} number.".format(x, odd_or_even)

odd_even(2)

# Multiply Function
def multiply(list, value):
    for x in range(len(list)):
        list[x] = value * list[x]
    return list

a = [2,4,10,16]
print multiply(a, 5)

# Hacker challenge: Layered Multiples Function
def layered_multiples(array):
    new_array = []
    new_sub_array = []
    for x in array:
        new_sub_array = x * [1]
        new_array.append(new_sub_array)
    return new_array

print layered_multiples(multiply([1,2,3], 5))
