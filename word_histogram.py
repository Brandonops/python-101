print("This is a Word Histogram, this program will tally your words for each word in the sentence!")
user_input = input("Please enter a sentence: ")



def word_histogram(input):
    counts = dict()
    words = str.split(input)

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(word_histogram(user_input))
        