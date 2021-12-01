
from types import FunctionType


def make_repeater_of(times: int) -> FunctionType:
    def repeater(word: str) -> str:
        return word * times
    return repeater


def make_division_by(n: int) -> FunctionType:
    return lambda x: x // n


def run():
    repeat_5 = make_repeater_of(5)
    print(repeat_5('Hola'))
    repeat_10 = make_repeater_of(10)
    print(repeat_10('Platzi'))

    division_by_3 = make_division_by(3)
    print(division_by_3(30))
    division_by_5 = make_division_by(5)
    print(division_by_5(55))


if __name__ == '__main__':
    run()
