x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(array):
    for value in array:
        if type(value) == int:
            print '*' * value
        elif type(value) == str:
            print value[0].lower() * len(value)

draw_stars(x)
