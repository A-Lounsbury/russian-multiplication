import math
# multiplies two numbers
def russian_multiply(x, y):
    # filling the two lists
    xNumbers = [x]
    yNumbers = [y]
    while x > 1:
        x = xNumbers[len(xNumbers) - 1] / 2
        if math.floor(x) >= 1:
            xNumbers.append(math.floor(x))
    for n in range(len(xNumbers) - 1):
        y = 2 * y
        yNumbers.append(y)

    # removing the numbers we don't need
    i = 0
    while i < len(xNumbers) - 1:
        if xNumbers[i] % 2 == 0:
            xNumbers.remove(xNumbers[i])
            yNumbers.remove(yNumbers[i])
            i -= 1
        i += 1
    sum = 0
    for n in yNumbers:
        sum += n
        
    return sum

print(russian_multiply(9, 13))
if 9 * 13 == russian_multiply(9, 13):
    print("equal")

print(russian_multiply(13, 9))
if 13 * 9 == russian_multiply(13, 9):
    print("equal")

print(russian_multiply(121, 398))
if 121 * 398 == russian_multiply(121, 398):
    print("equal")

# converts a decimal number to a list of binary digits
def decimalToBinary(n):
    digits = []
    while n >= 1:
        digits.append(n % 2)
        if n % 2 == 1:
            n = int((n - 1) / 2)
        elif n % 2 == 0:
            n = int(n / 2)
    return digits

print()
# multiplies two numbers
def egyptian_multiply(x, y):
    # filling the two lists
    xNumbers = []
    yNumbers = []
    n = 0.5
    while n * 2 < x:
        xNumbers.append(int(n * 2))
        n = n * 2
    for n in xNumbers:
        yNumbers.append(n * y)
    
    # finding the two numbers that sum to x
    digits = decimalToBinary(x)
    sum = 0
    for i, d in enumerate(digits):
        if d == 1:
            sum += yNumbers[i]
    
    return sum

print(egyptian_multiply(9, 13))
if 9 * 13 == egyptian_multiply(9, 13):
    print("equal")

print(egyptian_multiply(10, 13))
if 10 * 13 == egyptian_multiply(10, 13):
    print("equal")
    
print(egyptian_multiply(65, 93))
if 65 * 93 == egyptian_multiply(65, 93):
    print("equal")

print(egyptian_multiply(93, 65))
if 93 * 65 == egyptian_multiply(93, 65):
    print("equal")
    
print(egyptian_multiply(4368764, 32019))
if 4368764 * 32019 == egyptian_multiply(4368764, 32019):
    print("equal")