def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp


while True:
    try:
        type = int(input(
            "Welcome! Please enter the type of conversion:\n1. Fahrenheit to Celsius\n2. Celsius to Fahrenheit\n"))
        if type not in (1, 2):
            raise ValueError

        if type == 1:
            f_temp = float(input("Please enter the temperature in Fahrenheit: "))
            result = f_to_c(f_temp)
            print(f"The temperature in Celsius is: {result:.2f}")
        else:
            c_temp = float(input("Please enter the temperature in Celsius: "))
            result = c_to_f(c_temp)
            print(f"The temperature in Fahrenheit is: {result:.2f}")

        again = input("Would you like to convert another temperature? (Y/N): ").upper()
        if again != 'Y':
            break
    except ValueError:
        print("Invalid input. Please enter a valid option.")

print("Thank you for using the temperature converter!")
