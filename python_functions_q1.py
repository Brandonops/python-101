def madlib(name1 = "Jenn", subject1 = "science"):
    return (f"{name1}'s favorite subject is {subject1}.")

user_name = input("Please Enter a name: ")
user_subject = input("Please enter a subject: ")

result = madlib(user_name, user_subject)

print(result)


