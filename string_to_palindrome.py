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
        print(lis)

    for i in range(1, len(lis) - 1):
        print(lis[i])
        print(lis[-(i + 1)])

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


print(s2p("test"))
print(s2p("python"))

Sample Output:
  ['t', 'e', 's', 'e', 't']
  ('Given string was: ', 'test', ' And number of insertions took was: ', 1)
  
  ['P', 'y', 't', 'h', 'o', 'n', 'o', 'h', 't', 'y', 'P']
  ('Given string was: ', 'Python', ' And number of insertions took was: ', 4)
