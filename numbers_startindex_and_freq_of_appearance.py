__author__ = 'sachs7'

"""
Given a sorted array with duplicates and a number, find the range in the
form of (startIndex, endIndex) of that number. For example,

find_range({0 2 3 3 3 10 10}, 3) should return (2,4).
find_range({0 2 3 3 3 10 10}, 6) should return (-1,-1). -----> As of now, not printing this.
The array and the number of duplicates can be large.
"""


def find_range(a, b):
    counter = [i for i in range(len(a)) if a[i] == b]
    start_index = counter[0]
    end_index = counter[-1]
    total = len(counter)

    print("start index of " + str(b) + " --> " + str(start_index) + "; end index --> " + str(end_index) + ".")
    return "start index of " + str(b) + " is " + str(start_index) + " and appears " + str(total) + " times."


result = find_range([1, 2, 2, 1, 1, 1, 4], 1)
print(result)

Sample Output:
  start index of 1 --> 0; end index --> 5.
  start index of 1 is 0 and appears 4 times.
  
  if searching 4 in above list:
  start index of 4 --> 6; end index --> 6.
  start index of 4 is 6 and appears 1 times.
