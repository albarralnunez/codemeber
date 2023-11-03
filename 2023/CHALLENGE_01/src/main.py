import pathlib
from collections import defaultdict


def read_input(input_file: pathlib.Path):
    with input_file.open("r") as f:
        return f.read()


def main():
    input_file = pathlib.Path(pathlib.Path(__file__).parent.parent / "inputs/message_01.txt")
    message_txt = read_input(input_file)
    message = message_txt.split(" ")
    lower_message = map(lambda x: x.lower(), message)
    words_counter =  defaultdict(int)
    for word in lower_message:
        words_counter[word] += 1
    result = "".join(f"{w}{c}" for w, c in words_counter.items())
    print(result)

if __name__ == "__main__":
    main()