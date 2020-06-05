import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# convert all whitespace characters to a space
characters_whitespace = '\n \t \r'.split(" ")

for whitespace in characters_whitespace:
    words = words.replace(whitespace, " ")

# remove consecutive spaces
words = words.replace("  ", " ")

# analyze which words can follow other words
following_words = dict()

# create additional dictionaries to categorize words as start/end words
start_words = dict()
end_words = dict()

ending_punctuation = [".", "?", "!"]

words_array = words.split(" ")

for word_id in range(len(words_array)):

    word = words_array[word_id]

    # skip the last word
    if word_id == len(words_array) - 2:
        break

    # if there is a next word, add it
    if word_id + 1 < len(words_array):

        next_word = words_array[word_id + 1]

        # start a new set for words to follow if the set doesn't exist yet
        if word not in following_words:
            following_words[word] = []

        # add the next word to the set
        following_words[word].append(next_word)

        # if the word is a start word, add it to the start_words dictionary
        # start word criteria: starts with a capital letter OR starts with a quote and 
        is_start_word = (word[0].isalpha() and word[0] == word[0].upper()) or (len(word) > 1 and word[0] == '"' and word[1].isalpha() and word[1] == word[1].upper())

        if is_start_word and word not in start_words:
            start_words[word] = 1

        # if the word is an end word, add it to the end_words dictionary
        is_end_word = (word[-1] in ending_punctuation) or (len(word) > 1 and word[-1] == '"' and word[-2:-1] in ending_punctuation)

        if is_end_word and word not in end_words:
            end_words[word] = 1

# for data in following_words:
#     print(data, following_words[data])

# for data in start_words:
    # print(data, start_words[data])

# for data in end_words:
#     print(data, end_words[data])

start_words_array = list(start_words)

# construct 5 random sentences
for sentence_id in range(5):

    # keep track of whether a closing double quote is needed
    need_closing_double_quote = False

    # start sentence with a random word from start_words_array
    next_word = random.choice(start_words_array)
    sentence = next_word
        
    # keep track of whether to look for a word with a double-closing quote (if the current word doesn't already have both)
    if next_word[0] == '"' and next_word[-1] != '"':
        need_closing_double_quote = True

    # continue picking words until an end word is encountered
    while True:

        # can end sentence if any opening double quotes have been matched
        if next_word in end_words and not need_closing_double_quote:
            break

        # choose a next word and determine if update double quote count
        next_word = random.choice(following_words[next_word])
                
        if need_closing_double_quote:
            
            # do not allow nesting of double quotes. Next word must not begin with a double quote.
            if next_word[0] == '"':
                continue

            # next word has a closing double quote; update count
            elif next_word[-1] == '"':
                need_closing_double_quote = False
         
        else:

            # do not allow a word with a closing double quote if there was no double opening quote before it
            if next_word[-1] == '"':
                continue

            # next word has an opening double quote; update count (but only if it doesn't end with a double quote)
            elif next_word[0] == '"' and next_word[-1] != '"':
                need_closing_double_quote = True

        sentence += " " + next_word

    print(sentence, "\n")