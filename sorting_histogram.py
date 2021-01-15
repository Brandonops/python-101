print("This is a sorting histogram, this program will tally your words for each word in the sentence!")
user_input = input("Please enter a sentence: ")



def word_histogram(input):
    counts = dict() #empty dictionary
    words = str.split(input) #

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    sortedValues = sorted(counts, key=count.get)
    sortedCounts = {}

    for value in sortedValues:
        sortedCounts[value] = counts [value]
    return sortedCounts

print(word_histogram(user_input))
        