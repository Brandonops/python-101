def is_even(num):
    if num % 2  == 0:
       return True
    else: 
        return False

def only_evens(num):
    for i in num:
        count = 0
        if is_even(i):
            count += 1
            return i


print(only_evens([11, 20, 42, 97, 23, 10, 50, 10, 12402, 12, 1452]))