def print_upper_words(words, letters):
    """Print each word on separate line, uppercased, if starts with one of given letters in the set"""
    for word in words:
        if(word[0].lower() in letters):
            print(word.upper())


print_upper_words(["hello", "ey", "goodbye", "yo", "yes", "friend", "Eyvan"], letters={"h", "y", "e"})
