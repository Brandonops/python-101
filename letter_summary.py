print("Dictionary builder!")
user_input = input("Please enter a word, this program will tally your letters in the word: ")

dict = {}
for letter in user_input:
    if letter in dict:
        dict[letter] += 1
    else:
        dict[letter] = 1
print(dict)   
        


