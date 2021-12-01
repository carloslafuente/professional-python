
def is_prime(number: int) -> bool:
    limit = (number // 2) + 1
    for i in range(1, limit):
        if number % i == 0 and i != 1:
            return False
    return True


def run():
    print(is_prime(13))


if __name__ == '__main__':
    run()
