""" A PROJECT MANAGEMENT SOFTWARE
Allow users to load, save, display, filter, add, and update projects.
"""

from project import Project
from datetime import datetime

MENU = "(L)oad projects\n" \
       "(S)ave projects\n" \
       "(D)isplay projects\n" \
       "(F)ilter projects by date\n" \
       "(A)dd new project\n" \
       "(U)pdate project\n" \
       "(Q)uit"

FILENAME = 'project.txt'


def main():
    """Display a menu of options and call the appropriate function for the user's choice"""
    projects = load_projects(FILENAME)
    print(MENU)
    choice = input(">>>").lower()
    while choice != "q":
        if choice == "l":
            print("Successfully loaded")
        elif choice == "s":
            print("Successfully Saved")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_project_by_date(projects)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("invalid choice")
        print(MENU)
        choice = input(">>>").lower()
    print("Thank you for using custom-built project management software.")
    save_projects(projects, FILENAME)


def load_projects(filename):
    """Loads project data from a file and returns a list of Project objects."""
    with open(filename, 'r') as in_file:
        in_file.readline()
        projects = [Project(*line.strip().split('\t')[0:5]) for line in in_file]
    return projects


def display_projects(projects):
    """Prints a list of incomplete and completed projects sorted by priority."""
    incomplete_projects = sorted([p for p in projects if int(p.completion) < 100])

    completed_projects = sorted([p for p in projects if p.completion == 100])

    print("Incomplete projects:")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects:")
    for project in completed_projects:
        print(f"  {project}")


def save_projects(projects, filename):
    """Writes project data to a file in tab-separated format."""
    with open(filename, 'w') as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(
                f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.estimate}\t{project.completion}",
                file=out_file)


def filter_project_by_date(projects):
    """Ask the user for a start date and prints a list of projects that start on or after that date"""
    start_date = input("Show projects that start after date(dd/mm/yyyy): ")
    start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
    filtered_projects = sorted([project for project in projects if project.start_date >= start_date])

    for project in filtered_projects:
        print(project)


def add_new_project(projects):
    """Prompts the user for project details and adds a new Project object to the projects list."""
    print("Let's add a new project")
    name = input("Name: ").title()
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: "))
    completion = int(input("Completion percentage: "))
    project = Project(name, start_date, priority, cost_estimate, completion)
    projects.append(project)


def update_project(projects):
    """Prompts the user to choose a project to update, then prompts for new data values and updates it into selected project.
"""
    for i, project in enumerate(projects):
        print(f"{i}. {project}")
    update_choice = int(input("Project choice: "))
    print(projects[update_choice])
    new_percentage = int(input("New Percentage: "))
    while new_percentage < 0 or new_percentage > 100:
        print("Invalid percentage")
        new_percentage = int(input("New Percentage: "))
    projects[update_choice].completion = new_percentage
    try:
        new_priority = int(input("New Priority: "))
    except ValueError:
        new_priority = projects[update_choice].priority
    projects[update_choice].priority = new_priority


main()
