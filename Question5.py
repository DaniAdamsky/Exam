def most_common_word(story: tuple[str, ...]) -> str:
    """function that gets a short story in a tuple and finds which word appears the most and prints a counter"""
    if story == ():
        #to check if the tuple is empty
        return "No story provided"
    word_count = {}
    for line in story:
        for word in line.split():
            word_count[word] = word_count.get(word, 0) + 1
    most_common = max(word_count, key=word_count.get)
    print(f"The word: {most_common}\nappears {word_count[most_common]} times.")
    return most_common

print(most_common_word(("hello world", "hello there- today is sunday", "weekend is fun", "yes it is")))