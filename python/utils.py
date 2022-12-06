from pathlib import Path
from typing import Callable, TypeVar

T = TypeVar("T")


def load(day: int) -> list[str]:
    formatted = str(day).zfill(2)
    p = Path(f"../inputs/day{formatted}.txt").resolve()

    with open(p, "r") as f:
        data = [x.strip() for x in f.readlines()]
    return data


def take(n: int, _from: list[T]) -> list[T]:
    if n >= len(_from):
        return _from
    else:
        return _from[:n]


def sliding_window(window_size: int, _from: list[T]) -> list[list[T]]:
    if window_size >= len(_from):
        return [_from]
    else:
        result = []
        for i in range(0, (len(_from) - window_size) + 1):
            result.append(_from[i : i + window_size])
        return result


def eager(transformation) -> list:
    return list(transformation)


def max_n(_from: list[int], n: int) -> list[int]:
    tmp = _from
    result = []

    for _ in range(n):
        m = max(tmp)
        result.append(m)
        tmp.remove(m)

    return result


def min_n(_from: list[int], n: int) -> list[int]:
    tmp = _from
    result = []

    for _ in range(n):
        m = min(tmp)
        result.append(m)
        tmp.remove(m)

    return result


def split(_from: list[T], by: Callable[[T], bool], keep=False) -> list[list[T]]:
    result = []
    tmp = []
    for v in _from:
        if by(v):
            if keep:
                tmp.append(v)
            result.append(tmp)
            tmp = []
        else:
            tmp.append(v)

    return result
