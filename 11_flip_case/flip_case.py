from curses.ascii import islower


def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    output = ""
    for char in phrase:
        #to select which characters to switch
        if char.lower() == to_swap.lower():
            #from lower to upper case
            if char.islower(): 
                new_char = char.upper()
            #from upper to lower case 
            else:
                new_char = char.lower()
            #from upper to lower
            if char.isupper():
                new_char = char.lower()
            else:
                new_char = char.upper()
            output += new_char
        #rest of the characters
        if char.lower() != to_swap.lower():
            output += char   
    return output
