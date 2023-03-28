1.
name = input("What is your name? ")

file = open("name.txt", "w")
file.write(name)
file.close()

2.
file = open("name.txt", "r")
name = file.read()
print("Your name is", name)
file.close()

3.
file = open("numbers.txt", "r")
num1 = int(file.readline())
num2 = int(file.readline())
file.close()

print(num1 + num2) # prints 59

4.
file = open("numbers.txt", "r")
total = 0

for line in file:
    total += int(line)

file.close()

print(total)
