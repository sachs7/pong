__author__ = 'Sachi'


def sop(array_of_numbers, summed_value):
    diction = {}

    for i in array_of_numbers:
        if summed_value - i not in diction:
            diction[i] = 'True'
        elif summed_value - i in diction:
            return [summed_value - i, i]
        else:
            return None

print(sop([1, -2, 3, 0, -6, 1], -6))
print(sop([10, 5, 2, 3, 7, 5], 10))
print(sop([5, 9, 13, -3], 10))


Results: 
        [0, -6]
        [3, 7]
        [13, -3]
