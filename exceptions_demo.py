"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
ans- a valueerror will occur when a user inputs a non numeric value 
2. When will a ZeroDivisionError occur?
ans - when the user inputs a value that is 0 
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
ans - no, the code will never run if the user inputs a value that is 0 
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Cannot divide by zero")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
   print("Cannot divide by zero!")
print("Finished.")

