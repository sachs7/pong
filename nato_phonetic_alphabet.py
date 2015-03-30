__author__ = 'sachs7'
"""
In this, we're going to create the function nato that takes
a word and returns a string spells the word using the NATO phonetic alphabet.
There should be a space between each word in the returned string,
and the first letter of each word should be capitalized.
For those of you that don't want your fingers to bleed,
this kata already has a dictionary typed out for you.

nato("Banana") # == "Bravo Alpha November Alpha November Alpha"
"""
letters = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie",
    "D": "Delta", "E": "Echo", "F": "Foxtrot",
    "G": "Golf", "H": "Hotel", "I": "India",
    "J": "Juliett", "K": "Kilo", "L": "Lima",
    "M": "Mike", "N": "November", "O": "Oscar",
    "P": "Papa", "Q": "Quebec", "R": "Romeo",
    "S": "Sierra", "T": "Tango", "U": "Uniform",
    "V": "Victor", "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee", "Z": "Zulu", " ": "$"
}

out = []


def nato(word):
    for i in word:
        a = i.upper()
        out.append(letters[a])
    return " ".join(out)

wor = input("Enter the word: ")
print(nato(wor))

Sample Output:
  Enter the word: cisco network associate
  Charlie India Sierra Charlie Oscar $ November Echo Tango Whiskey Oscar Romeo Kilo $ Alpha Sierra Sierra Oscar Charlie India Alpha Tango Echo
