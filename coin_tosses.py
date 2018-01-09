import random

def coin_toss(limit):
    heads = 0
    tails = 0
    counter = 0
    print "Starting the program..."
    while counter < limit:
        toss = random.randint(0, 1)
        if toss is 1:
            heads += 1
            counter += 1
            print "Attempt #{}: Throwing a coin... It's a head! ...Got {} head(s) so far and {} tail(s) so far".format(counter, heads, tails)
        if toss is 0:
            tails += 1
            counter += 1
            print "Attempt #{}: Throwing a coin... It's a tail! ...Got {} head(s) so far and {} tail(s) so far".format(counter, heads, tails)
    print "Ending the program. Thank you."

coin_toss(5001)
