#!/usr/bin/env python3
low = 0
high = 100
print("Please think of a number between 0 and 100!")

while True:
    guess = (low + high) // 2
    print("Is your secret number", guess, "?")
    print("Enter 'h' if the guess is too high, 'l' if too low, 'c' if correct.")

    user_input = input("Your response: ")

    if user_input == 'h':
        high = guess
    elif user_input == 'l':
        low = guess
    elif user_input == 'c':
        print("Game over. Your secret number was:", guess)
        break
    else:
        print("Sorry, I did not understand your input.")