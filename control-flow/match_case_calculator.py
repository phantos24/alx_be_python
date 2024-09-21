number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")
result = 0

match operation:
    case "+":
        result = number1 + number2
    case "-":
        result = number1 - number2
    case "*":
        result = number1 * number2
    case "/":
        if number2 != 0:
            result = number1 + number2
        else:
            print("can't divid by zero.")
print(f"The result is {result}.")
