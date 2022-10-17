#! /usr/bin/python3


def compose(notes: list[str], directions: list[int], start: int) -> list[str]:
    idx = start
    out = []
    for dir in directions:
        out += [notes[idx]]
        idx = idx + dir
        if idx < 0:
            idx = len(directions) + idx
        if idx > len(notes):
            idx = idx % len(notes)

    return out + [notes[idx]]

def main():
    notes = ["do", "re", "mi", "fa", "sol"]
    directions = [1, -3, 4, 2]
    start = 2
    print(compose(notes, directions, start))



if __name__ == "__main__":
    main()