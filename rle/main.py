def compress(text):
    if len(text) == 0:
        return ""

    # the output string
    string = ""

    # How many of the current character there are. Eg 'HHH' -> 3
    current_character_count = 0
    # Latest character being counted.
    latest_character = text[0]

    for c in text:
        # If we've seen the character before, increment the counter
        if latest_character == c:
            current_character_count += 1
        else:
            # Add the previous character and how many there were to the total string
            string += latest_character + ' ' + str(current_character_count) + ' '
            # Reset character count to 1
            current_character_count = 1
            # Update current character to the new one
            latest_character = c

    # add the last character type onto the end, since the loop would break before the else branch is hit
    # For example 'AAABB' would only return 'A 3' without this, since it loops over all of the 'B's without it changing.
    string += latest_character + ' ' + str(current_character_count) + ' '
    return string


print(compress("AAARRRRGGGHH"))
print(compress("A"))
print(compress("HELLO"))
