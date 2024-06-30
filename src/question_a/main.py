#add import
from src.question_a.question_a import test_config
from src.question_a.question_a import is_prime

def is_prime():
    while True:
        user_input = input("Enter a number or type 'quit' to exit:")

        if user_input.lower() == 'quit':
            print("Exiting the program.")
            break

        try:
            number = float(user_input)
            result = number ** 2
            print(f"The square of {number} is {result}.")
        except ValueError:
            print("Please enter a valid number.")



