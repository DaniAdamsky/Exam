def snake_to_camel(text: str) -> str:
    """gets a string in snake case and returns it in camel case"""
    rest = text.split("_")
    for word in rest[1:]:
        #loop starts at 1, makes every word besides the first a title
        word = word.title()
        return rest[0] + "".join(word)

print(snake_to_camel('hello_python'))