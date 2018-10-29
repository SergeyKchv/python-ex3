import random
import datetime


def print_format():
    fhand = open("format.txt")

    line = random.choice(fhand.readlines())

    moods = ["happy", "sad", "depressed", "angry", "annoyed", "bored", "confused", "excited", "lonely"]
    mood = random.choice(moods)
    smilies = [":)", ":(", ":D", ":/", ":|", ":'(", ":O", ":@", ":P", ":3"]
    smiley = random.choice(smilies)

    now = datetime.datetime.now()

    date = now.strftime("%d.%m.%Y")
    time = now.strftime("%H:%m")

    random_int = random.randint(0, 9999)
    random_float = round( random.uniform(0, 9999), 3)
    print(line.format(mood=mood, smiley=smiley, date=date, time=time, int=random_int, float=random_float))