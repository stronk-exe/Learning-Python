import random

cards = ["Club", "Diamond", "Heart", "Spade"]
num = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

print(random.choice(num), end = ' ')
print('of', end = ' ')
print(random.choice(cards))
