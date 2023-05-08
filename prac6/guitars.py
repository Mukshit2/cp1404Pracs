from guitar import Guitar

print("My guitars!")
guitars = []
while True:
    name = input("Name: ")
    if name == "":
        break
    
    while True:
        try:
            year = int(input("Year: "))
            if year < 0:
                raise ValueError("Year must be a positive integer.")
            break
        except ValueError as e:
            print(f"Invalid input: try again: ")
    
    while True:
        try:
            cost = float(input("Cost: $"))
            if cost < 0:
                raise ValueError("Cost must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input, Try again: ")
    
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    print(f"{str(guitar)} added.\n")

print("\nThese are my guitars:")
for i, guitar in enumerate(guitars, start=1):
    vintage_string = " (vintage)" if guitar.is_vintage() else ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
