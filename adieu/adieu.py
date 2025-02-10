#!/usr/bin/env python3
import sys
import inflect

def main():
    # Create an inflect engine instance
    engine = inflect.engine()

    names = []
    print("Enter names (one per line). Press Ctrl-D (Unix/Mac) or Ctrl-Z (Windows) to finish:")

    # Read names until an EOFError is raised when the user signals end-of-input.
    try:
        while True:
            name = input()
            if name.strip():
                names.append(name.strip())
    except EOFError:
        pass

    # Ensure that at least one name was entered
    if not names:
        sys.exit("Error: No names were entered.")

    # Use engine.join() to create a natural language list of names.
    # For example, for three names, it will produce: "Liesl, Friedrich, and Louisa"
    joined_names = engine.join(names)

    # Construct and output the farewell message
    farewell_message = "Adieu, adieu, to " + joined_names
    print(farewell_message)

if __name__ == '__main__':
    main()
