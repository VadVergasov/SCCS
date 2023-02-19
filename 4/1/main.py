import sys
import os
import random

import ujson

print("Hello World")


operation_defs = {"/": [], "*": [], "+": [], "-": []}

try:
    with open(
        os.path.join(
            os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir)),
            "operations.json",
        ),
        "r",
        encoding="utf8",
    ) as fp:
        operation_defs = ujson.load(fp)
except FileNotFoundError:
    print("No operation definitions in operations.json found!")
    sys.exit(1)


def operation(first: float, second: float, oper: str) -> float:
    """
    Takes three parameters:

    two numbers and operation(string like “add”, “sub”, “mult” and “div”)

    returns the result of this operation with two given arguments;
    """
    for op, aliases in operation_defs.items():
        if oper in aliases:
            match op:
                case "/":
                    return first / second
                case "*":
                    return first * second
                case "-":
                    return first - second
                case "+":
                    return first + second
    return 0


first, second, oper = input().split(" ")
first = float(first)
second = float(second)

print(operation(first, second, oper))

numbers = []

for _ in range(random.randint(10, 100)):
    numbers.append(random.randint(1, 1000))

numbers = list(filter(lambda number: number % 2 == 0, numbers))

print(numbers)
