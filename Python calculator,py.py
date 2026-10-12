def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def division(a, b):
    if b == 0:
        return "Error! Division by zero is not possible."
    return a / b


def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def percentage(number, total):
    if total == 0:
        return "Error! Total cannot be zero."
    return (number / total) * 100


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    while True:
        print("\n===== CALCULATOR =====")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Check Even/Odd")
        print("6. Calculate Percentage")
        print("7. Exit")

        operation = input("Enter your choice (1-7): ").strip()

        if operation == "1":
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            print("Result:", add(a, b))

        elif operation == "2":
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            print("Result:", subtract(a, b))

        elif operation == "3":
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            print("Result:", multiply(a, b))

        elif operation == "4":
            a = get_number("Enter the first number: ")
            b = get_number("Enter the second number: ")
            print("Result:", division(a, b))

        elif operation == "5":
            number = get_number("Enter a whole number: ")

            if number.is_integer():
                print(number, "is", check_even_odd(int(number)))
            else:
                print("Even/Odd checking requires a whole number.")

        elif operation == "6":
            a = get_number("Enter the number: ")
            b = get_number("Enter the total/reference number: ")

            result = percentage(a, b)

            if isinstance(result, str):
                print(result)
            else:
                print(f"{a} is {result:.2f}% of {b}")

        elif operation == "7":
            print("Thank you for using the calculator. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option from 1 to 7.")


if __name__ == "__main__":
    main()
