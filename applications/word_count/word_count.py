def word_count(s):
    table = str.maketrans(dict.fromkeys('":;,.-+=/\\|[]{}()*^&'))

    strings = s.translate(table).split()

    count = {}

    for w in [word.lower() for word in strings]:
        if w not in count:
            count[w] = 0
        
        count[w] += 1
    
    return count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))