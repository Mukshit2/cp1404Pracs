from place import Place
import csv


class PlaceCollection:
    def __init__(self):
        self.places = []

    def load_places(self, file_path):
        with open(file_path, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                name = row[0]
                country = row[1]
                priority = int(row[2])
                visited = True if row[3] == 'v' else False
                place = Place(name,country,priority,visited)
                self.places.append(place)

    def save_places(self, file_path):
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            for place in self.places:
                writer.writerow(place.to_csv_row())

    def add_place(self, place):
        self.places.append(place)

    def get_num_unvisited_places(self):
        return len([place for place in self.places if not place.visited])

    def sort(self, key):
        self.places.sort(key=lambda place: (getattr(place, key), place.priority))

    def __iter__(self):
        return iter(self.places)