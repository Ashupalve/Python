# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the ‘ZeroDivisionErrorʼ .

try:
    a = int (input("Enter numerator:"))
    b = int (input("Enter denominator:"))
    print(a/b)

except ZeroDivisionError as v :
    print("Denominator is zero")

