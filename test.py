def Plus():
    total = 0
    print("\n[+] Addition Mode: Enter numbers to add. Type 'result' to see the final result.")
    while True:
        user_input = input("Enter a number (or 'result'): ").strip()
        if user_input.lower() == "result":
            print(f"Final Addition Result: {total}")
            break
        try:
            num = float(user_input)
            total += num
            print(f"Current Total: {total}")
        except ValueError:
            print("Invalid input. Enter a number or 'result'.")

def Minus():
    total = None
    print("\n[-] Subtraction Mode: Enter numbers to subtract. Type 'result' to see the final result.")
    while True:
        user_input = input("Enter a number (or 'result'): ").strip()
        if user_input.lower() == "result":
            if total is not None:
                print(f"Final Subtraction Result: {total}")
            else:
                print("No values entered.")
            break
        try:
            num = float(user_input)
            if total is None:
                total = num
            else:
                total -= num
            print(f"Current Total: {total}")
        except ValueError:
            print("Invalid input. Enter a number or 'result'.")

def Into():
    total = None
    print("\n[*] Multiplication Mode: Enter numbers to multiply. Type 'result' to see the final result.")
    while True:
        user_input = input("Enter a number (or 'result'): ").strip()
        if user_input.lower() == "result":
            if total is not None:
                print(f"Final Multiplication Result: {total}")
            else:
                print("No values entered.")
            break
        try:
            num = float(user_input)
            if total is None:
                total = num
            else:
                total *= num
            print(f"Current Total: {total}")
        except ValueError:
            print("Invalid input. Enter a number or 'result'.")

def Divide():
    total = None
    print("\n[/] Division Mode: Enter numbers to divide. Type 'result' to see the final result.")
    while True:
        user_input = input("Enter a number (or 'result'): ").strip()
        if user_input.lower() == "result":
            if total is not None:
                print(f"Final Division Result: {total}")
            else:
                print("No values entered.")
            break
        try:
            num = float(user_input)
            if total is None:
                total = num
            else:
                if num == 0:
                    print("Cannot divide by zero.")
                    continue
                total /= num
            print(f"Current Total: {total}")
        except ValueError:
            print("Invalid input. Enter a number or 'result'.")

if __name__ == "__main__":
    print("Simple Interactive Calculator")
    print("Available operations: plus, minus, into, divide")
    op = input("Choose operation: ").strip().lower()

    if op == "plus":
        Plus()
    elif op == "minus":
        Minus()
    elif op == "into":
        Into()
    elif op == "divide":
        Divide()
    else:
        print("Invalid operation selected.")