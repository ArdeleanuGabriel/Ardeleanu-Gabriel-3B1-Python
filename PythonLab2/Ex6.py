#! /usr/bin/python3
import itertools


def element_filter_count(count: int, *lists: list)-> list:
    megalist = list(itertools.chain(*lists))
    out = set()
    for i in megalist:
        if megalist.count(i) == count:
            out.add(i)

    return list(out)


def main():
    print(f"element_filter_count(2, [1,2,3], [2,3,4],[4,5,6], [4,1, 'test']) = {element_filter_count(2, [1,2,3], [2,3,4],[4,5,6], [4,1, 'test'])}")

if __name__ == "__main__":
    main()