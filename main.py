import marvin
import quote
import format


def main():
    """
    This is the main method, I call it main by convention.
    """
    while True:
        marvin.menu()
        choice = input("--> ")

        if choice == "q":
            break
        elif choice == "1":
            marvin.ask_name()
        elif choice == "2":
            marvin.age_in_seconds()
        elif choice == "3":
            marvin.weight_on_moon()
        elif choice == "12":
            format.print_format()
        elif 'quote' in choice.lower():
            quote.print_random_quote()
        else:
            print(choice)
            input("Press enter to continue...")


if __name__ == "__main__":
    main()