import random

def scores_and_grades(number):
    scores_and_grades = {}
    while len(scores_and_grades) < number:
        score = int(random.random()*100)
        if score in range(60,70):
            scores_and_grades[score] = 'D'
        if score in range(70,80):
            scores_and_grades[score]  = 'C'
        if score in range(80,90):
            scores_and_grades[score]  = 'B'
        if score in range(90,100):
            scores_and_grades[score]  = 'A'

    for key,value in scores_and_grades.iteritems():
        print 'Score: {}; Your grade is {}'.format(key,value)

scores_and_grades(10)
