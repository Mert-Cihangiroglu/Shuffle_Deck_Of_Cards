import itertools
import random

deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
random.shuffle(deck)
number=int(input('Enter the Number of Cards you want :'))
print("You got this: ")
for i in range(number):
    print(deck[i][0],"of",deck[i][1])