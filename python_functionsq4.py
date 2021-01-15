def is_even(num1):
    if num1 % 2  == 0:
       return True
    else: 
        return False
        
user_input = int(input("Please enter a number: "))

print("You're even number is:  " + str(is_even(user_input)) + "!") 



def is_odd(num2):
    if is_even(num2):
        return False
    else:
        return True


user_input2 = int(input("You're odd number is: "))
print("You're number is:  " + str(is_odd(user_input2)) + "!")

    

#def is_odd(num):
#    if is_even(num)
#
#output = is_odd()
#print(output)
