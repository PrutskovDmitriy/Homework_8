from functools import wraps


def val_checker(callback):
    def _val_checker(func):
        @wraps(func)
        def wrapper(*args):
            for x in args:
                if not callback(x):
                    raise ValueError(f'Ошибка значения: {x}')
            return func(*args)

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

print(calc_cube(6))