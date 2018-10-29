def menu():
    """
    Display the menu with options that Marvin can do.
    """
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print("""
          ,     ,
         (\____/)
          (_oo_)
            (O)
          __||__    \)
       []/______\[] /
       / \______/ \/
      /    /__|
     (\   /____|
Hi, I'm Marvin. I know it all. What can I do you for?
    """)
    print("1) State your name and meet Marvin.")
    print("2) Get your age in seconds.")
    print("3) Get your weight in the moon.")
    print("4) Convert minutes to hours.")
    print("12) Get status.")
    print("q) Quit.")


def ask_name():
    name = input("Enter your name: ")
    if len(name) <= 0:
        print("Wrong name")
    else:
        print("Hello, " + name)


def age_in_seconds():
    age = input("Enter your age: ")
    if int(age) <= 0:
        print("Wrong age")
    else:
        age_in_seconds = int(age)*360*24*60*60
        print("Your age is " + str(age_in_seconds) + " seconds")


def weight_on_moon():
    weight = input("Enter your weight: ")
    if int(weight) <= 0:
        print("Wrong weight")
    else:
        weight_on_moon = float(weight) * 1.622 / 9.81
        print("Your weight on moon is " + str(round(weight_on_moon)))
