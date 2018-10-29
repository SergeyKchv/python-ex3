import random


def print_random_quote():
    file_name = "quotes.txt"
    quote = random.choice(open(file_name).readlines())
    print(quote)