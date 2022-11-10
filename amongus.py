'''
made by:  Aayush 9029
created at: April 3, 2020
turned sus by: Omicron166

A module that converts string to amongus code and vice versa

'''

codec = {
    # . -> amongus
    # - -> sus
    # ' ' -> sussy-baka
    "a": "amongus-sus",
    "b": "sus-amongus-amongus-amongus",
    "c": "sus-amongus-sus-amongus",
    "d": "sus-amongus-amongus",
    "e": "amongus",
    "f": "amongus-amongus-sus-amongus",
    "g": "sus-sus-amongus",
    "h": "amongus-amongus-amongus-amongus",
    "i": "amongus-amongus",
    "j": "amongus-sus-sus-sus",
    "k": "sus-amongus-sus",
    "l": "amongus-sus-amongus-amongus",
    "m": "sus-sus",
    "n": "sus-amongus",
    "o": "sus-sus-sus",
    "p": "amongus-sus-sus-amongus",
    "q": "sus-sus-amongus-sus",
    "r": "amongus-sus-amongus",
    "s": "amongus-amongus-amongus",
    "t": "sus",
    "u": "amongus-amongus-sus",
    "v": "amongus-amongus-amongus-sus",
    "w": "amongus-sus-sus",
    "x": "sus-amongus-amongus-sus",
    "y": "sus-amongus-sus-sus",
    "z": "sus-sus-amongus-amongus",
    "0": "sus-sus-sus-sus-sus",
    "1": "amongus-sus-sus-sus-sus",
    "2": "amongus-amongus-sus-sus-sus",
    "3": "amongus-amongus-amongus-sus-sus",
    "4": "amongus-amongus-amongus-amongus-sus",
    "5": "amongus-amongus-amongus-amongus-amongus",
    "6": "sus-amongus-amongus-amongus-amongus",
    "7": "sus-sus-amongus-amongus-amongus",
    "8": "sus-sus-sus-amongus-amongus",
    "9": "sus-sus-sus-sus-amongus",
    ".": "amongus-sus-amongus-sus-amongus-sus",
    ",": "sus-sus-amongus-amongus-sus-sus",
    "?": "amongus-amongus-sus-sus-amongus-amongus",
    "!": "sus-amongus-sus-amongus-sus-sus",
    "-": "sus-amongus-amongus-amongus-amongus-sus",
    "/": "sus-amongus-amongus-sus-amongus",
    "@": "amongus-sus-sus-amongus-sus-amongus",
    "(": "sus-amongus-sus-sus-amongus",
    ")": "sus-amongus-sus-sus-amongus-sus",
    " ": "sussy-baka"
}

def encode(input: str) -> str:
    '''
    returns amongus code variant of the string

    i am butterfly
    >>> amongus-amongus sussy-baka amongus-sus sus-sus sussy-baka sus-amongus-amongus-amongus amongus-amongus-sus sus sus amongus amongus-sus-amongus amongus-amongus-sus-amongus amongus-sus-amongus-amongus sus-amongus-sus-sus

    Cc Aa
    >>> sus-amongus-sus-amongus sus-amongus-sus-amongus sussy-baka amongus-sus amongus-sus
    '''

    letters = list(input)
    output = ""
    for letter in letters:
        if letter.lower() in codec:
            output += codec[letter.lower()] + " "
        else:
            return KeyError
    return output

def decode(input: str) -> str:
    '''
    returns the decoded string as amongus code

    amongus-sus amongus-sus-sus-amongus amongus-sus-sus-amongus amongus-sus-amongus-amongus amongus
    >>> apple

    amongus-amongus sussy-baka amongus-sus sus-sus sussy-baka amongus-sus sussy-baka sus-amongus-amongus amongus-amongus amongus-amongus-amongus sus-amongus-sus-amongus sus-sus-sus sussy-baka sus-amongus-amongus amongus-sus sus-amongus sus-amongus-sus-amongus amongus amongus-sus-amongus
    >>> i am a disco dancer
    '''
    
    words =  input.split("  ")
    output = ""
    
    for word in words:
        letters  = word.split()
        for letter in letters:
            for string, code in codec.items():  # for name, age in dictionary.iteritems():  (for Python 2.x)
                if letter == code:
                    output += string
        output += " "
    return output[:-1]
