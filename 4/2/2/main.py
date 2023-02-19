"""
Main code of this program
"""
import os
import sys

import re
import ujson


def load(username: str) -> set:
    """
    Load file
    """
    try:
        file_stream = open(
            os.path.join("/data", username + ".json"), "r", encoding="utf8"
        )
        data = set(ujson.load(file_stream))
    except FileNotFoundError:
        data = set()
    return data


def save(username: str, data: set) -> None:
    """
    Save file
    """
    file_stream = open(os.path.join("/data", username + ".json"), "w", encoding="utf8")
    ujson.dump(list(data), file_stream)


def enter_user() -> str:
    """
    Gets username
    """
    username = str(input("Enter username:\n"))
    return username


def main() -> None:
    """
    Main funtcion
    """
    username = enter_user()
    data = load(username)
    try:
        while True:
            commands = input("Enter next command:\n").split(" ")
            match commands[0]:
                case "add":
                    for value in commands[1:]:
                        if len(value) == 0:
                            continue
                        data.add(value)
                case "remove":
                    for value in commands[1:]:
                        if len(value) == 0:
                            continue
                        data.remove(value)
                case "find":
                    found_any = False
                    for value in commands[1:]:
                        if set(value).issubset(data):
                            print(f"{value} - exists")
                            found_any = True
                    if not found_any:
                        print("No such elements")
                case "list":
                    print(data)
                case "grep":
                    expression = commands[1]
                    found_any = False
                    for value in data:
                        if re.fullmatch(expression, str(value)) is not None:
                            print(f"{value} - matches the expression")
                            found_any = True
                    if not found_any:
                        print("No such elements")
                case "save":
                    save(username, data)
                case "load":
                    data = load(username)
                case "switch":
                    answer = str(input("Save data (Yes / No)?\n"))
                    if answer == "Yes":
                        save(username, data)
                    username = enter_user()
                    data = load(username)
    except KeyboardInterrupt:
        answer = str(input("Save data (Yes / No)?\n"))
        if answer == "Yes":
            save(username, data)
        sys.exit(0)


if __name__ == "__main__":
    main()
