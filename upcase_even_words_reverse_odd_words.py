__author__ = 'sachs7'

"""
Write a program to modify the string in following pattern,
Change odd words to uppercase and Reverse the even words.
Make sure that the spaces (multiple) between the words remains as it is.
E.g.:
Input : "This is a test String!!"
Output: "THIS si A tset STRING!!"
"""


def sentence(test):
    word_lis = test.split(" ")
    output = []
    for _ in word_lis:
        if len(_) % 2 == 0:
            output.append(_.upper())
        else:
            x = ""
            for i in range(len(_) - 1, -1, -1):
                x += _[i]
            output.append(x)

    print(" ".join(output))

user_input = input("Enter the sentence: ")
sentence(user_input)

Sample Output:
  Enter the sentence: This is a test string! Hope you guys enjoy.
  THIS IS a TEST !gnirts HOPE uoy GUYS ENJOY.
