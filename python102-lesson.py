#todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]

#index = 2
#while index < len(todos):
#    todo = todos[index]
#    print ("%d: %s" %(index +1, todo))
#    index += 1

#count = 1
#for todo in todos:
#    print("%d: %s" % (count, todo))
#    count += 1

#todos.append("binge watch a show")
#todos.append("go to sleep")

#count = 1
#for todo in todos:
#    print("%d: %s" %(count,todo))
#    count += 1


#todos = todos + ["binge watch a show", "go to sleep"]

#count = 1
#for todo in todos:
#    print("%d: %s" % (count, todo))
#    count += 1


todos = []

user_input = input("Please enter a new to-do task:")

while len(user_input) > 0:
    todos.append(user_input)

    print("To do: ")
    print("================")
    count = 1
    for todo in todos:
        print("%d: %s" % (count, todo))
        count += 1
    print("\n")
    user_input = input("what do we need to do? ")
elif 

print("Have a nice day!")





#todos = ["pet the cat", "go to work", "shop for groceries", "go home", "feed the cat"]
#del todos[0]
#print(todos)

#del todos[1:3]
print(todos)
