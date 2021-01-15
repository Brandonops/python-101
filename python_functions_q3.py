print("This Program converts degrees in Fahrenheit to Celsius!")

def calculate_temp_celsius(temp):
    return (temp - 32) * 5/9

user_temp = float(input("Please enter a temperature: "))

result_farenheit = calculate_temp_celsius(user_temp)

print(str(result_farenheit) + " C")
