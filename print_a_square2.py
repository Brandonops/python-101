try:
    user_input = int(input("How big is the square?"))
    count = 0
    star = "*"
    while (count <= user_input) :
            print(star * user_input)
            count += 1
except ValueError:
    print("Please run the program again and enter a number!")