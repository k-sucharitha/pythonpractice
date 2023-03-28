import random

# input() always returns string datatype "10"
top_of_range = input("Type a number:")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a large number than 0 next time.")
        quit()
else:
    print("Please type a number next time.")
    quit()


random_number = random.randint(0, top_of_range)
# print(f"Random number from the given number {top_of_range} is: {random_number}")
guess_count = 0

while True:
    guess_count += 1
    user_guess = input("Make a guess.")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a large number than next time.")
        continue

    if user_guess == random_number:
        print("you got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")


print(f"You guessed the number correctly in {guess_count} chances.")
