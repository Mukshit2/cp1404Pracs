'''
Name: Mukshit
student id - jc955870
GITHUB URL - https://github.com/Mukshit2/cp1404Pracs
'''

import csv
import random
from place import Place
# Constants
FILENAME = "places.csv"
HEADER = ["Name", "Country", "Priority", "Visited"]
UNVISITED_MARK = "*"


# Main program


def main():
    places = load_places()
    print(places)
    print("Travel Tracker 1.0 - by Mukshit")
    print(f"{len(places)} places loaded from {FILENAME}")


    while True:
        places = sorted(places, key=lambda place: (place.visited, int(place.priority)))
        print("Menu:")
        print("L - List places")
        print("A - Add new place")
        print("M - Mark a place as visited")
        print("R - Recommend a place to visit")
        print("Q - Quit\n")
        choice = input(">>> ").upper()
        if choice == "L":
            display_places(places)
        elif choice == "A":
            add_place(places)
        elif choice == "M":
            mark_visited(places)
        elif choice == "R":
            recommend_place(places)
        elif choice == "Q":
            save_places(places)
            print("Goodbye!")
            break
        else:
            print("Invalid menu choice!")


# Functions
def load_places():
    """
    Load places from a CSV file and return a list of Place objects
    """
    places = []
    with open(FILENAME, newline="") as file:
        reader = csv.reader(file)
        next(reader)  # skip the header row
        for row in reader:
            name = row[0]
            country = row[1]
            priority = int(row[2])
            visited = True if row[3] == 'v' else False
            place = Place(name, country, priority, visited)
            places.append(place)
    return places



def save_places(places):
    """
    Save places to a CSV file
    """
    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(HEADER)
        for place in places:
            writer.writerow(place)


def display_places(places):
    """
    Display a neatly formatted list of all places with details and number of unvisited places
    """
    print(f"Places to Visit: ")
    unvisited_count = 0
    for i, place in enumerate(places, 1):
        visited_mark = UNVISITED_MARK if not place.visited else " "
        print(f"{visited_mark}{i}. {place}")
        if not place.visited:
            unvisited_count += 1
    if unvisited_count == 0:
        print(f"All {len(places)} places have been visited!")
    else:
        print(f"There are {unvisited_count} unvisited places out of {len(places)}.")


def get_valid_input(prompt):
    """
    Get a valid input from the user
    """
    variable = input(prompt)
    while variable == "":
        print("input cannot be blank .")
        variable = input(prompt)
    return variable


def add_place(places):
    """
    Add a new place to the list
    """
    name = input("Name: ")
    while not name:
        print("Input can not be blank")
        name = input("Name: ")
    country = input("Country: ")
    while not country:
        print("Input can not be blank")
        country = input("Country: ")
    priority = input("Priority: ")
    while not priority.isnumeric():
        print("Priority must be number")
        priority = input("Priority: ")
    priority = int(priority)
    place = Place(name, country, priority)
    places.append(place)
    print(f"{place.name} in {place.country} (priority {place.priority}) added to Travel Tracker")



def mark_visited(places):
    unvisited_places = [place for place in places if not place.visited]
    if not unvisited_places:
        print("No unvisited places")
        return

    # print the list of places
    display_places(places)

    # get user input for place to mark as visited
    while True:
        try:
            choice = int(input("Enter the number of a place to mark as visited: "))
            if choice < 1 or choice > len(places):
                raise ValueError
            elif places[choice - 1].visited:
                print("That place has already been visited.")
            else:
                places[choice - 1].mark_visited()
                print(f"{places[choice - 1].name} in {places[choice - 1].country} marked as visited.")
                break
        except ValueError:
            print(f"Please enter a number between 1 and {len(places)}")


def recommend_place(places):
    """
    Recommend a random unvisited place
    """
    unvisited_places = [place for place in places if not place.visited]
    if unvisited_places:
        place = random.choice(unvisited_places)
        print(f"\nNot sure where to visit next? \nHow about... {place.name} in {place.country}?\n")
    else:
        print("\nNo places left to visit!\n")



main()
