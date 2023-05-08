"""Project class with less than function"""

from datetime import datetime


class Project:
    """Represents information about a project."""
    def __init__(self, name, start_date, priority, estimate, completion):
        """Construct a project from the given values."""
        self.name = name
        self.start_date = datetime.strptime(start_date, '%d/%m/%Y').date()
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __repr__(self):
        """ Return a string representation of a project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, priority {self.priority}, estimate: ${self.estimate:.2f}, completion: {self.completion}%"

    def __lt__(self, other):
        """Sort the project on the basis of priority."""
        return self.priority < other.priority


