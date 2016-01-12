import math
M = float(input())
T = int(input())
X = int(input())
tip = (M * T)/100
tax = (M * X)/100
final = int(round(M + tip + tax))
print("The final price of the meal is $" + str(final) + ".")
