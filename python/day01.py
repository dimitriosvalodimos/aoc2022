from utils import load, split, eager, max_n


def part1(data: list[list[int]]) -> int:
    # find chunk with largest sum
    sums = [sum(chunk) for chunk in data]
    return max(sums)


def part2(data: list[list[int]]) -> int:
    sums = [sum(chunk) for chunk in data]
    total = sum(max_n(sums, 3))
    return total


def main():
    data = load(1)
    chunked = [eager(map(int, chunk)) for chunk in split(data, lambda x: x == "")]
    result1 = part1(chunked)
    print(result1)
    result2 = part2(chunked)
    print(result2)


main()
