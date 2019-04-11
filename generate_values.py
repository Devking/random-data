import random

for x in range(888):
    rand = int(random.gauss(50, 20))
    if rand > 100: rand = 100
    if rand < 0: rand = 0
    randcat = random.randint(0, 4)
    target = 1 if rand >= 50 else 0
    print('{},{},{},{}'.format(x, rand, randcat, target))
