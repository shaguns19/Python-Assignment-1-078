a = int(input("Enter dividend: "))
b = int(input("Enter divisor: "))
if b != 0:
    print("Quotient =", a // b)
    print("Remainder =", a % b)
else:
    print("Division by zero is not allowed.")
