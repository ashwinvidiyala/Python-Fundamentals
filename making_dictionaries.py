name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dictionary(list1, list2):
    if len(list1) == len(list2) or len(list1) > len(list2):
        new_dictionary = zip(list1, list2)
    elif len(list1) < len(list2):
        new_dictionary = zip(list2, list1)
    return new_dictionary

print make_dictionary(name, favorite_animal)
