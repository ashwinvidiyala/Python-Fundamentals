dict = {'name': 'Anna',
        'age': 101, 
        'country of birth': 'The United States',
        'favorite language': 'Python'}

def print_dict(dict):
    for key, value in dict.iteritems():
        print "My {} is {}".format(key, value)

print_dict(dict)
