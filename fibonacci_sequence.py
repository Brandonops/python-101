def fib(n):
    n = []
    fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    count = 0
    for i in fibonacci:
        i = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(i)
    return 
        




user_input = int(input("Please enter a number: "))
print(fib(user_input))



#"0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368,
