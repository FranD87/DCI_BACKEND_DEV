Python basics: Exceptions IV
Coin-toss Debugging
The following program is meant to be a simple coin toss guessing game. The player gets two guesses (it’s an easy game). However, the program has several bugs in it. Run through the program a few times to find the bugs that keep the program from working correctly.

This is a bit different. It's not a program that can be considered "complete", so feel free to change the code for the coin toss game to work to work correctly (meaning that the program should ask for the correct input twice and return the correct answers).

import random
guess = ''
while guess not in ('heads', 'tails'):
print('Guess the coin toss! Enter heads or tails:')
guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
print('You got it!')
else:
print('Nope! Guess again!')
guesss = input()
if toss == guess:
print('You got it!')
else:
print('Nope. You are really bad at this game.')