# Create your main program in this file, using the TravelTrackerApp class


from kivy import Config
from kivy.app import App

from kivy.uix.button import Button

from kivy.lang import Builder
# constants
from kivy.properties import StringProperty, ListProperty

from placecollection import PlaceCollection
from place import Place

TITLE = "Travel Tracker"
KV_FILE = "app.kv"
FILE_NAME = "places.csv"


class TravelTrackerApp(App):
    """..."""

    # class variables here ....
    SORT_KEY_TO_VALUE = {
        'is_visited': 'Visited',
        'priority': 'Priority',
        'name': 'Name',
        'country': 'Country'
    }

    # define properties here ...
    current_sort_key = StringProperty('priority')
    top_status_label = StringProperty()  # empty string
    bottom_status_label = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.place_collection = PlaceCollection()
        self.place_collection.load_places(FILE_NAME)

    def build(self):
        self.title = TITLE
        self.root = Builder.load_file(KV_FILE)
        self.create_button()
        return self.root

    def update_text(self):
        if self.place[2].lower() == 'important':
            if self.place[1].lower() == 'visited':
                self.text = 'You visited ' + self.place[0] + '. Great travelling!'
            else:
                self.text = 'You need to visit ' + self.place[0] + '. Get going!'
        else:
            if self.place[1].lower() == 'visited':
                self.text = 'You visited ' + self.place[0] + '.'
            else:
                self.text = 'You need to visit ' + self.place[0] + '.'

    def create_button(self):

        # Create a button for each place in the places list
        for place in self.place_collection:
            button = Button(text=str(place))
            button.bind(on_release=self.release_entry)
            button.place = place
            # Set the background color of the button based on whether the place is visited or not
            if place.visited:
                button.background_color = [1, 1, 1, 1]  # green
            else:
                button.background_color = [0, 1, 0, 1]  # red

            # Bind the button to the on_place_button_click function, passing the place object as an argument

            # Add the button to the place_box layout
            self.root.ids.place_box.add_widget(button)

    def release_entry(self, button):
        button.place.visited = not button.place.visited
        # Update the background color of the button based on the new visited status
        if button.place.visited:
            button.place.mark_unvisited()
            button.background_color = [1, 1, 1, 1]  # green
        else:
            button.place.mark_visited()
            button.background_color = [0, 1, 0, 1]  # red

    def change_sort_key(self, spinner_value):
        # update the current_sort_key
        self.current_sort_key = [key for key, value in self.SORT_KEY_TO_VALUE.items() if value == spinner_value][0]

        # run the sort method in PlaceCollection
        self.place_collection.sort(self.current_sort_key)

        # re-build the box of places
        self.build_place_boxes()

    def add_place(self):
        name = self.root.ids.name_input.text.strip()
        country = self.root.ids.country_input.text.strip()
        priority = self.root.ids.priority_input.text.strip()
        if not name or not country or not priority:
            self.bottom_status_label = "Please fill in all fields."
            return
        try:
            priority = int(priority)
        except ValueError:
            self.bottom_status_label = "Priority must be an integer."
            return
        new_place = Place(name, country, priority, "n")
        self.place_collection.add_place(new_place)
        self.root.ids.place_box.clear_widgets()
        self.show_places()
        self.clear_all_input()
        self.bottom_status_label = f"Added {new_place.name} to the list."

    def clear_all_input(self):
        self.root.ids.name_input.text = ""
        self.root.ids.country_input.text = ""
        self.root.ids.priority_input.text = ""

    def on_stop(self):
        self.place_collection.save_places(KV_FILE)
        # implement save_places


if __name__ == '__main__':
    Config.set('graphics', 'width', 600)
    Config.set('graphics', 'height', 500)
    TravelTrackerApp().run()
