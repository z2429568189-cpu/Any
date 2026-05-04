def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        print("Error: Cannot divide by zero!")
        return None
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

while True:
    op = input("input the operator (+, -, *, /, or quit): ").strip().lower()

    if op == "quit":
        print("Goodbye!")
        break

    if op not in operations:
        print("Error: Invalid operator!")
        continue

    try:
        s = float(input("input the first number: "))
        t = float(input("input the second number: "))
    except ValueError:
        print("Error: Please enter valid numbers!")
        continue

    result = operations[op](s, t)

    if result is not None:
        print("your numbers are: ", s, "and", t)
        print("result: ", result)
