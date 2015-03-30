__author__ = 'sachs7'

"""
Given a text file, read the contents of file line by line.
Search for a pattern, eg., "test" and print the number of line and the number of times
the pattern appears in a line.

e.g., input : "This is test. And test is easy.
               This is cool! test is really easy."
      output:  Line 1: 2
               Line 2: 1
"""

counter = 0
line_num = 1

with open('G:/Pycharm/c.txt') as f:
    for line in f:
        counter += line.count("test")  # we are looking for 'test' word.
        # print("Number of times 'test' appears in line #" + str(line_num) + " ---> " + str(counter))
        print("Number of times 'test' appears in line # {0}  -->  {1}".format(str(line_num), str(counter)))
        line_num += 1
        counter = 0

Sample Output:
  Number of times 'test' appears in line # 1  -->  1
  Number of times 'test' appears in line # 2  -->  0
  Number of times 'test' appears in line # 3  -->  1
  Number of times 'test' appears in line # 4  -->  0
  Number of times 'test' appears in line # 5  -->  3
  Number of times 'test' appears in line # 6  -->  0
  Number of times 'test' appears in line # 7  -->  1
