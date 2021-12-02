def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates


def convert_to_set(some_list):
    return list(set(some_list))


def run():
    random_list = [1, 2, 3, 4, 5, 6, 6, 6, 6, 3]
    print(remove_duplicates(random_list))
    print(convert_to_set(random_list))


if __name__ == '__main__':
    run()
