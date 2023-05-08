from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    # Open the file for reading
    filename = 'languages.csv'
    try:
        in_file = open(filename, 'r')
    except FileNotFoundError:
        print(f"Unable to open {filename}")
        return

    # File format is like: Language,Typing,Reflection,Year,Pointer Arithmetic
    # 'Consume' the first line (header) - we don't need its contents
    in_file.readline()
    # All other lines are language data
    for line in in_file:
        # print(repr(line))  # debugging
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # print(parts)  # debugging
        # Reflection and Pointer Arithmetic are stored as a string (Yes/No) and we want Booleans
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[4] == "Yes"
        # Construct a ProgrammingLanguage object using the elements
        # year should be an int
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
        # Add the language we've just constructed to the list
        languages.append(language)
    # Close the file as soon as we've finished reading it
    in_file.close()

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)


if __name__ == "__main__":
    main()