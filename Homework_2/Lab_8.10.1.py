user_input = input()
wo_spaces = ''
for x in user_input:
    if x != ' ':
        wo_spaces += x
space_reverse = ''
for x in wo_spaces:
    space_reverse = x+space_reverse
if wo_spaces == space_reverse:
    print(user_input + " is a palindrome")
else:
    print(user_input + " is not a palindrome")