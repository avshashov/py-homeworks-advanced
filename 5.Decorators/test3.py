import os
from datetime import datetime


def logger(path):
    def decorator(old_function):
        def wrapper(*args, **kwargs):
            date = datetime.now()
            res = old_function(*args, **kwargs)

            logs = [date, old_function.__name__, args, kwargs, res]

            action = 'a' if os.path.exists('main.log') else 'w'
            with open(path, action) as f:
                for row in logs:
                    print(row, file=f)
                print('_' * 10, file=f)
            return res

        return wrapper

    return decorator

@logger('generator.log')
def flat_generator(list_of_lists):
    for el in list_of_lists:
        if isinstance(el, list):
            yield from flat_generator(el)
        else:
            yield el


list_of_lists = [
    [['a'], ['b', 'c']],
    ['d', 'e', [['f'], 'h'], False],
    [1, 2, None, [[[[['!']]]]], []]
]

print(*flat_generator(list_of_lists))
