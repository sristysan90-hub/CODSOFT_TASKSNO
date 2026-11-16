"""CodSoft Task 2 - Simple Calculator."""


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def calculate(a, b, op):
    if op == "+":
        return a + b
    if op == "-":
        return a - b
    if op == "*":
        return a * b
    if op == "/":
        if b == 0:
            return "Error: cannot divide by zero"
        return a / b
    if op == "%":
        if b == 0:
            return "Error: cannot divide by zero"
        return a % b
    if op == "**":
        return a ** b
    return "Error: invalid operation"


def main():
    print("=== SIMPLE CALCULATOR ===")
    while True:
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")
        print("Operations:  +  -  *  /  %  **")
        op = input("Choose an operation: ").strip()

        result = calculate(num1, num2, op)
        print(f"Result: {num1} {op} {num2} = {result}")

        again = input("\nCalculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
