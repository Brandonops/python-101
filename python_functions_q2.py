print("This Program converts degrees in Celsius to Fahrenheit!")

def calculate_temp_fahrenheit(temp):
    return (temp * 9/5) + 32

user_temp = float(input("Please enter a temperature: "))

result_farenheit = calculate_temp_fahrenheit(user_temp)

print(str(result_farenheit) + "F")
