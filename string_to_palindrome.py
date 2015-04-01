__author__ = 'sachs7'
"""
Given a string, convert it to Palindrome with minimum number of insertions.
"""


def s2p(text):
    lis = list(text)
    count = 0

    if lis[0:] == lis[::-1]:
        return "It is palindrome, No insertion was done."

    elif lis[0] != lis[-1]:
        lis.append(lis[0])

    for i in range(1, len(lis) - 1):

        if lis[i] == lis[-(i + 1)]:
            continue
        else:
            lis.insert(len(lis) - i, lis[i])
            count += 1
        print(lis)

    if lis[0:] == lis[::-1]:
        return "Given string was: ", text, " And number of insertions took was: ", count
    else:
        return "It is not"


# print(s2p("test"))
# print(s2p("python"))

inp = str(input("Enter the string: "))
print(s2p(inp))

Sample Output:
    ['t', 'e', 's', 'e', 't']
    ('Given string was: ', 'test', ' And number of insertions took was: ', 1)
  
    ['P', 'y', 't', 'h', 'o', 'n', 'y', 'P']
    ['P', 'y', 't', 'h', 'o', 'n', 't', 'y', 'P']
    ['P', 'y', 't', 'h', 'o', 'n', 'h', 't', 'y', 'P']
    ['P', 'y', 't', 'h', 'o', 'n', 'o', 'h', 't', 'y', 'P']
    ('Given string was: ', 'Python', ' And number of insertions took was: ', 4)

    Enter the string: 12345
    ['1', '2', '3', '4', '5', '2', '1']
    ['1', '2', '3', '4', '5', '3', '2', '1']
    ['1', '2', '3', '4', '5', '4', '3', '2', '1']
    ('Given string was: ', '12345', ' And number of insertions took was: ', 3)
    
    Enter the string: aba
    It is palindrome, No insertion was done.
