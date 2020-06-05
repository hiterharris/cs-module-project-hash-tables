# Your code here

# allow sorting by multiple criteria
from operator import itemgetter

# copy of word_count function
def word_count(s):

    words = s.lower()

    # convert all whitespace characters to a space
    characters_whitespace = '\n \t \r'.split(" ")
    
    for whitespace in characters_whitespace:
        words = words.replace(whitespace, " ")

    # remove characters to be ignored
    characters_to_ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split(" ")

    for character in characters_to_ignore:
        words = words.replace(character, "")

    # turn string into an array of individual words        
    words = words.split(" ")

    words_already_seen = dict()

    for word in words:

        # skip empty strings
        if word == "":
            continue

        if word in words_already_seen:
            words_already_seen[word] += 1
        else:
            words_already_seen[word] = 1

    return words_already_seen

# make histogram
def make_histogram(file_path):

    with open(file_path) as file:
        text = file.read()

    # create a dictionary using the word_count function to store word frequencies
    frequencies = word_count(text)

    # turn the dictionary into an array and sort by number of occurrences, descending
    frequencies_array = frequencies.items()
    frequencies_array = sorted(frequencies_array, key=itemgetter(1, 0), reverse=True)

    # find length of longest word
    longest_word_length = len(frequencies_array[0][0])

    for word_data in frequencies_array:
        if len(word_data[0]) > longest_word_length:
            longest_word_length = len(word_data[0])

    # output words and their occurences. Output one "#" for each occurence
    for word_data in frequencies_array:

        word_formatted = word_data[0] + (longest_word_length - len(word_data[0])) * " "
        histogram_bar = "#" * word_data[1]

        histogram_row = word_formatted + "  " + histogram_bar

        print(histogram_row)
    
make_histogram("robin.txt")