"""
Challenge 01: Message
"""

import pathlib
from collections import defaultdict

import colored


def read_input(input_file: pathlib.Path):
    """
    Read input file
    """
    with input_file.open("r") as f:
        return f.read()


def main():
    """
    Decrypt message and print it
    """
    input_file = pathlib.Path(pathlib.Path(__file__).parent.parent / "inputs/message_01.txt")
    message_txt = read_input(input_file)
    message = message_txt.split(" ")
    lower_message = map(lambda x: x.lower(), message)
    words_counter =  defaultdict(int)
    for word in lower_message:
        words_counter[word] += 1
    result = "".join(f"{w}{c}" for w, c in words_counter.items())
    print(f"{colored.fg(2)}{colored.attr('bold')}Challenge 01:{colored.attr('reset')}:")
    print(result)

if __name__ == "__main__":
    main()
