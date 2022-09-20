def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # list1 = phrase.split(" ")
    output = []
    for item in phrase.split(" "):
        output.append(item[0].upper()+item[1:].lower())
    return " ".join(output)