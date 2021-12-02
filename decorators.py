# def decorator(func):
#     def wrapper():
#         print('Added functionality')
#         func()
#     return wrapper


# @decorator
# def greating():
#     print('Hello!')


# greating()


# def to_upper(func):
#     def wrapper(text):
#         return func(text).upper()
#     return wrapper


# @to_upper
# def message(name):
#     return f'{name}, you got a message.'


# print(message('Carlos'))


from datetime import datetime


def execution_type(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        func(*args, **kwargs)
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos.')
        return func(*args, **kwargs)
    return wrapper


@execution_type
def random_func():
    for _ in range(1, 1000000):
        pass


@execution_type
def addition(a: int, b: int) -> int:
    return a + b


@execution_type
def greating(name: str = 'Carlos') -> str:
    return f'Hello {name}'


random_func()
print(addition(5, 11))
print(greating())
