words = "It's thanksgiving day. It's my birthday,too!"
print "The position of the first occurence of 'day' is position #", words.find("day")

x = [2,54,-2,7,12,98]
print "The minimum value is", min(x)
print "The maximum value is", max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print "First value is", y[0]
print "Last value is", y[-1]

array1 = [19,2,54,-2,7,12,98,32,10,-3,6]
array1.sort()
array2 = array1[:len(array1)/2]
array3 = array1[len(array1)/2:]
array3.insert(0, array2)

print "The final list is", array3
