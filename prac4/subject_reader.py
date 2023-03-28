
FILENAME = "subject_data.txt"

def main():
    data = get_data()
    display_subject_details(data)

def display_subject_details(data):
    for subject in data:
        print(subject[0], "is taught by", subject[1], "and has", subject[2], "students")
        
def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data.append(parts)  # Add the parts to the list
    input_file.close()
    return data

main()