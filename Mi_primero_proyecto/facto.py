"""
def fact(num):
    if num == 1:
        return 1
    else:
        return num * fact(num -1)
num = int(input('proporcionar #'))
print(fact(num))
"""

while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")