import random

low = 1
high = 100
guesses = 0
number = random.randint(low, high)

while True:
    guess = int(input(f" Enter a number between({low} - {high})"))
    guesses +=1

    if guess < number:
        print(f"{guess} too low")

    elif guess > number:
        print(f'{guess} too high!')

    else:
        print("Correct!!")
        break


print(f"took {guesses} guesses")

