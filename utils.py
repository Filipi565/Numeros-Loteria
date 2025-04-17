from collections.abc import Iterable, Callable
from typing import Union

__all__ = (
    "get_rights",
    "parse_numbers"
)

def get_rights(results: Iterable[int], numbers: Iterable[int]):
    lists = list[int]()
    lists += results
    lists += numbers

    numbers_dict = dict[int, int]()

    _get_repeated = lambda x: (numbers_dict[x] >= 2)

    for number in lists:
        if number not in numbers_dict:
            numbers_dict[number] = 0
        
        numbers_dict[number] += 1
    
    return sum(map(_get_repeated, numbers_dict))

ParserError = type("ParserError", (Exception,), {})

def _parse_numbers(numbers, func):
    err = lambda: func("Error: Por favor, digite números separados por vírgula (,)")

    for number in numbers.split(","):
        try:
            yield int(number.strip())
        except ValueError:
            err()
            raise ParserError

def parse_numbers(numbers: str, func: Callable[[str], object]) -> Union[list[int], None]:
    if not callable(func):
        raise TypeError("func must be callable")
    
    if not isinstance(numbers, str):
        raise TypeError("numbers must be string")

    try:
        return list(_parse_numbers(numbers, func))
    except ParserError:
        return