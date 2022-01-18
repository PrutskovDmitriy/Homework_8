def type_log(func):
    def wrapper(*args):
        calc = func(*args)
        if len(args) == 1:
            print(f'{args[0]}: {type(args[0])}')
        else:
            for num in args:
                print(f'{num}: {type(num)}')
        return calc

    return wrapper


@type_log
def calc_cube(x, *args):
    return x ** 3


print(calc_cube(37))
