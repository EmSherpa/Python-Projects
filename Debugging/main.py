import math

def calculate():
    # 1. Map symbols directly to functions or lambdas
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b if b != 0 else math.inf,
        "log": lambda a, _: math.log10(a) if a > 0 else math.nan
    }

    print("Enter: '5 + 3' or 'log 100' (or 'exit')")

    while True:
        user_input = input('> ').strip().lower()
        if user_input == "exit":
            break

        parts = user_input.split()
        
        try:
            # 2. Handle 'log' separately as it only takes one number
            if parts[0] == "log":
                op, a, b = "log", float(parts[1]), 0
            else:
                a, op, b = float(parts[0]), parts[1], float(parts[2])

            # 3. Look up the math operation and run it
            if op in operations:
                result = operations[op](a, b)
                print(f"Result: {result}")
            else:
                print(f"Unknown operator: {op}")

        except (ValueError, IndexError):
            print("Error: Please use format 'num op num' or 'log num'")

if __name__ == "__main__":
    calculate()