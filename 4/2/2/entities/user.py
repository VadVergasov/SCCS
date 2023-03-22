"""
File with User class
"""
import os
import re

import ujson


class User:
    """
    User class with elements and username
    """
    def __init__(self) -> None:
        self.elements: set = set()
        self.username: str = str(input("Enter username: "))
        answer = str(input("Load data (Yes / No)?\n"))
        if answer == "Yes":
            self.load()

    def save(self) -> None:
        """
        Saving user to file
        """
        with open(os.path.join("data", self.username + ".json"), "w", encoding="utf8") as fp:
            ujson.dump(list(self.elements), fp)

    def load(self) -> None:
        """
        Loading user from file
        """
        try:
            file_stream = open(
                os.path.join("data", self.username + ".json"), "r", encoding="utf8"
            )
            self.elements = set(ujson.load(file_stream))
        except FileNotFoundError:
            pass

    def add(self, obj) -> None:
        """
        Adding object to elements
        """
        self.elements.add(obj)

    def remove(self, obj) -> None:
        """
        Removing object from elements
        """
        try:
            self.elements.remove(obj)
        except KeyError:
            pass

    def exists(self, objects: list) -> None:
        """
        Checks if object exists in elements
        """
        found_any = False
        for obj in objects:
            if len(obj) == 0:
                continue
            if set(obj).issubset(self.elements):
                print(f"{obj} - exists")
                found_any = True
        if not found_any:
            print("No such elements")

    def grep(self, expression: str) -> None:
        """
        Checks elements for any regex matches
        """
        found_any = False
        for value in self.elements:
            if len(value) == 0:
                continue
            if re.fullmatch(expression, str(value)) is not None:
                print(f"{value} - matches the expression")
                found_any = True
        if not found_any:
            print("No such elements")
