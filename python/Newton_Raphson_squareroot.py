#!/usr/bin/env python3

epsilon = 0.01         # Desired accuracy
y = 24                 # Number to find the square root of
guess = y / 2.0        # Initial guess
num_guesses = 0

while abs(guess ** 2 - y) >= epsilon:
    num_guesses += 1
    guess = guess - (((guess ** 2) - y) / (2 * guess))

print("Number of guesses:", num_guesses)
print("Square root of", y, "is approximately", guess)
