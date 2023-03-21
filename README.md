# russian-multiplication
An implementation of Russian and (limited) Egyptian multiplication, as seen in [this video](https://www.youtube.com/watch?v=HJ_PP5rqLg0). 
It includes a function that converts decimal numbers to binary. 
```
def decimalToBinary(n):
    digits = []
    while n >= 1:
        digits.append(n % 2)
        if n % 2 == 1:
            n = int((n - 1) / 2)
        elif n % 2 == 0:
            n = int(n / 2)
    return digits
```