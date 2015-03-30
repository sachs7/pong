__author__ = 'sachs7

"""
Given a Morse Code, decode it and print in human readable format
"""

morse_table = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
    ".": "E", "..-.": "F", "--.": "G", "....": "H",
    "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P",
    "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z", " ": ""
}


def decode_morse(morseCode):
    result = []
    lis1 = morseCode.split("   ")
    # print("after split at 3 spaces", lis1)
    for i in range(len(lis1)):
        # print("print list after 3 spaces",lis1[i])
        # if " " in lis1[i]:
        b = lis1[i].split()
        # print("if there is 1 space",b)
        for j in b:
            result.append(morse_table[j])
        result.append(" ")

    # return "".join(result)
    res = "".join(result)
    r = res.rstrip()
    fin = r.lstrip()
    return fin


print(decode_morse(".... . -.--   .--- ..- -.. ."))
print(decode_morse(".... . -.--     .... --- .--     -.-- --- ..-     -.. --- .. -. --."))

Sample Output:
  HEY JUDE
  HEY HOW YOU DOING
