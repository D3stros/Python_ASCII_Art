from pyfiglet import figlet_format
from termcolor import colored


def print_art(msg, color):
    valid_colors = ("red", "green", "yellow", "blue",
                    "magenta", "cyan", "white")

    if color not in valid_colors:
        color = "red"

    ascii_art = figlet_format(msg)
    colored_acii = colored(ascii_art, color=color)
    print(colored_acii)


msg = input("What would you like to print? ")
color = input("What color? ")
print_art(msg, color)
