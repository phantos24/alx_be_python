FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32



while (True):
    global degree
    try:
        degree = float(input("Enter the temperature to convert: "))
        break
    except:
         print("Invalid temperature. Please enter a numeric value.")

       

while (True):
    temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
    match (temp):
        case "c":
            converted = convert_to_fahrenheit(degree)
            print(f"{degree}°C is {converted}°F")
            break
        case "f":
            converted = convert_to_celsius(degree)
            print(f"{degree}°F is {converted}°C")
            break
        case _:
            print("Please enter a vaild temprature.")
