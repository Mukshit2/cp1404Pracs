class Place:
    def __init__(self, name: str, country: str, priority: int, visited: bool = False):
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited

    def __str__(self):
        return f"{self.name}, {self.country} - Priority: {self.priority} - Visited: {'Yes' if self.visited else 'No'}"


    def __repr__(self):
        return f"{self.name}, {self.country} - Priority: {self.priority} - Visited: {'Yes' if self.visited else 'No'}"
    def mark_visited(self):
        self.visited = True

    def mark_unvisited(self):
        self.visited = False

    def is_important(self) -> bool:
        return self.priority <= 2



