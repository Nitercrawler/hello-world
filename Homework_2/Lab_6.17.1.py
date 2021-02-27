pass_word = input('')  # taking the simple password as input

pass_word = list(pass_word)  # converting string to list

for i in range(0, len(pass_word)):  # iterating for changing characters
    if pass_word[i] == 'i':
        pass_word[i] = '!'
    elif pass_word[i] == 'a':
        pass_word[i] = '@'
    elif pass_word[i] == 'm':
        pass_word[i] = 'M'
    elif pass_word[i] == 'B':
        pass_word[i] = '8'
    elif pass_word[i] == 'o':
        pass_word[i] = '.'
    # elif pass_word[i] == 's':
     # pass_word[i] = '$'
strong_password = ""
strong_password = strong_password.join(pass_word)  # converting list to string
strong_password = strong_password+"q*s"  # appending "rdq" at end
print(strong_password)  # printing new password
