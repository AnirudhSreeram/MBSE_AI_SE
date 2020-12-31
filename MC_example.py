import random

# function to take different random step at each node


def random_walk(n):
    x, y = 0, 0
    for i in range(n):
        # NEWS direction addition
        (dx, dy) = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx  # increment x co-ordinates
        y += dy  # increment y co-ordinates
    return (x, y)

# for i in range(25):
#    walk = random_walk(10)
#    print(walk, 'distance from home = ', abs(walk[0])+abs(walk[1]))


no_walks = 20000  # number of trials for MC computations
for i in range(1, 31):
    no_trans = 0  # counter for no. of walks without cab
    for j in range(no_walks):
        (x, y) = random_walk(i)  # get a random walk for each iter
        dist = abs(x) + abs(y)  # compute distance from home
        if dist <= 4:  # distance greater than 4 take a cab else don't
            no_trans += 1  # inc counter
    res = abs(no_trans)/no_walks  # calc % of walks without cab
    print("walk size = ", i, "transport % = ", res*100)
