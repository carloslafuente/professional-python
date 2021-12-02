from time import sleep


def fibonacci_generator(max):
    n1, n2 = 0, 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            if aux <= max:
                yield aux
            else:
                break


if __name__ == '__main__':
    fibonacci = fibonacci_generator(50)
    for element in fibonacci:
        print(element)
        sleep(0.5)
