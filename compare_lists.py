list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
list_three = [1,2,5,6,5]
list_four = [1,2,5,6,5,3]
list_five = [1,2,5,6,5,16]
list_six = [1,2,5,6,5]
list_seven = ['celery','carrots','bread','milk']
list_eight = ['celery','carrots','bread','cream']

def compareLists(list_one, list_two):
    list_one.sort()
    list_two.sort()

    if list_one == list_two:
        print "The lists are the same"
    else:
        print "The lists are not the same"
    return

compareLists(list_one, list_two)
compareLists(list_three, list_four)
compareLists(list_five, list_six)
compareLists(list_seven, list_eight)
