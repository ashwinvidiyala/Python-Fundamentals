list1 = ['magical unicorns',19,'hello',98.98,'world']
list2 = [2,3,1,7,4,12]
list3 = ['magical','unicorns']

def typeList(list):
    string = ""
    sum = 0
    for value in list:
        if isinstance(value, int) or isinstance(value, float):
            sum = sum + value
        if isinstance(value, str):
            string = string + " " + value
    if sum > 0 and len(string) == 0:
        print "The list you entered is of integer type."
        print "Sum:", sum
    elif sum == 0 and len(string) >= 0:
        print "The list you entered is of string type."
        print "String:", string
    else:
        print "The list you entered is of mixed type."
        print "String:", string
        print "Sum:", sum
    return

typeList(list1)
