def fizzbuzzhehe(num):
        if num % 5 == 0 and num % 3 == 0:
            return ("fizzbuzz")
        elif num % 5 == 0:
            return ("buzz")
        elif num % 3 == 0:
            return ("fizz")
        return(user_input)

user_input = int(input("Please enter a number!: "))

print(fizzbuzzhehe(user_input))