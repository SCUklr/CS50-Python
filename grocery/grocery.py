def main():
    grocery_list = {}

    while True:
        try:
            # Read input without a prompt
            item = input()
        except EOFError:
            break

        # Normalize input: strip whitespace and convert to lowercase
        item = item.strip().lower()
        if item:
            grocery_list[item] = grocery_list.get(item, 0) + 1

    # Output the sorted list with counts, using uppercase for the item names
    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item.upper()}")


if __name__ == "__main__":
    main()
