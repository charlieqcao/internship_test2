from numpy.random import randint


your_value = randint(0,10,1)
enemy_value  = randint (0,10,1)

if your_value >= enemy_value:
    print("you win")
else:
    print("you lost")