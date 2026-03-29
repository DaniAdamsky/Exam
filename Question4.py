"""inputs strings from user until the user enters quit"""
list1 = []
while True:
    user_input = input("Enter string: ")
    if user_input == 'quit':
        break
    list1.append(user_input)
set_list = set(list1)
if len(list1) != len(set_list):
    print("Duplicate string found")
else:
    print("No duplicate strings found")