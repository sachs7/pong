"""
This code will take any sentence and convert it into Morse Code.
Note: Not all characters are supported. Other characters can be added by updating the dictionary table, "morse_table".
"""

morse_table = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
    "E": ".", "F": "..-.", "G": "--.", "H": "....",
    "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.",
    "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", ".": ".-.-.-", ",": "--..--",
    ":": "---...", "?": "..--..", "-": "-....-", "/": "-..-.",
    "@": ".--.-."
}


def morse_encoder(got):
    lis = list(got.upper())
    result = []
    # print(lis)
    for i in lis:
        if i == " ":
            result.append("   ")
        else:
            result.append(morse_table[i] + " ")
    return "".join(result)


print(morse_encoder("hey jude"))
print(morse_encoder("This is cool- You are awesome"))
print("printing email id: \n", morse_encoder("abc@gmail.com"))
