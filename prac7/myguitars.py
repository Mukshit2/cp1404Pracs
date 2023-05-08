class Guitar:
    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name}, {self.year}, ${self.cost:.2f}"

    def __lt__(self, other):
        return self.year < other.year


# read the existing guitars from the file
guitars = []
with open("guitars.csv", "r") as file:
    for line in file:
        name, year, cost = line.strip().split(",")
        guitars.append(Guitar(name, int(year), float(cost)))

# ask the user to enter new guitars

while True:
    name = input("Enter guitar name (or 'quit' to exit): ")
    if name == "quit":
        break
    while True:
        if not name:
            print("Error: Name cannot be empty")
            name = input("Enter guitar name (or 'quit' to exit): ")
        else:
            break
    while True:
        try:
            year = int(input("Enter year: "))
            if year <= 0:
                raise ValueError("Year must be a positive integer")
            break
        except ValueError as e:
            print(f"Error: {e}")
    while True:
        try:
            cost = float(input("Enter cost: "))
            if cost <= 0:
                raise ValueError("Cost must be a positive number")
            break
        except ValueError as e:
            print(f"Error: {e}")
    guitars.append(Guitar(name, year, cost))

# write all guitars to the file
with open("guitars.csv", "w") as file:
    for guitar in guitars:
        file.write(f"{guitar.name},{guitar.year},{guitar.cost:.2f}\n")

# display the sorted guitars
guitars.sort()
for guitar in guitars:
    print(guitar)
