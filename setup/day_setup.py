import re
import sys
import urllib.request
from urllib.error import URLError

from setup import file_creator

BASE_URL = "https://adventofcode.com/2017/day/"


def get_puzzle_name(puzzle_url):
    """
    Finds the name of the given day's puzzle and formats it into a string that can be used for a Python class by
    lower-casing and replacing spaces with underscores. If the resulting string starts with a number, "a_" is added as a
    prefix.
    :param puzzle_url: the URL of the given day's puzzle
    :return: the puzzle name
    """
    try:
        with (urllib.request.urlopen(puzzle_url) as f):
            print(f"Retrieving contents of {puzzle_url}")
            entire_page = f.read().decode("utf-8")
            raw_puzzle_name = re.search("--- (.*) ---", entire_page).group(1).split(": ")[1]
            raw_puzzle_name_alphanumeric = "".join([c if (c.isalnum() or c == " ") else "" for c in raw_puzzle_name])
            parsed_puzzle_name = "a_" + raw_puzzle_name_alphanumeric if raw_puzzle_name_alphanumeric[0].isnumeric() \
                else raw_puzzle_name_alphanumeric
            return parsed_puzzle_name.strip().lower().replace(" ", "_").replace("-", "_")
    except URLError as e:
        sys.exit(f"Could not get puzzle at {puzzle_url}: {e.reason}")


def read_template_file(template_file_name):
    return open(f"templates/{template_file_name}_template.txt").read()


day = int(input(f"Please enter a day to be setup: "))
puzzle_name = get_puzzle_name(f"{BASE_URL}{day}")
print(f"Puzzle name: {puzzle_name}")

file_creator.create_python_file(f"{puzzle_name}.py", day, "main", read_template_file("main"))
file_creator.create_python_file(f"test_{puzzle_name}.py", day, "tests",
                                read_template_file("test").format(day=day, puzzle_name=puzzle_name))
file_creator.create_test_data_file(day, "test_input.txt")
file_creator.create_test_data_file(day, "input.txt")
