secret_number = 42
guess = 0

while guess != secret_number:
    guess = eval(input("What is the secret number? "))
    if guess < secret_number:
        print("This is way too low.Please try agin ")
    elif guess > secret_number:
        print("This is much too high.Please try again ")
print("Congratulations,you have guessed the secret number!")
