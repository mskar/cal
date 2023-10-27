import itertools


def my_slice(start, stop=None, *args, **kwargs):
    if stop is None:
        start, stop = 0, start
    ascending = start < stop
    steps = args + tuple(kwargs.values())
    if steps:
        sum_steps = sum(steps)
        if (
            sum_steps == 0
            or ascending
            and sum_steps < 0
            or not ascending
            and sum_steps > 0
        ):
            raise ValueError(
                "The sum of positional arguments and "
                "keyword argument values cannot be zero and "
                "must have the same sign as stop - start."
            )
    if kwargs:
        key = list(kwargs.keys())[-1]
        steps = itertools.cycle((dict(enumerate(args)) | kwargs).items())
        while ascending == (start < stop):
            yield start, key
            key, value = next(steps)
            start += value
    else:
        steps = itertools.cycle(args)
        while ascending == (start < stop):
            yield start
            start += next(steps) if args else 1


list(my_slice(170))
list(my_slice(80, 170))[0:0]
dict(my_slice(80, 170, twoday=2))
list(my_slice(80, 170, 2, 3, 2, 3))
dict(my_slice(80, 170, twoday=2, fiveday=3, sevenday=2, zeroday=3))
dict(my_slice(80, 170, twoday=2, fiveday=3, sevenday=2, zeroday=3))
list(my_slice(80, 170, 2, 3, -2, 3))
list(my_slice(80, 170, -2, 3, -2, 3))
list(my_slice(170, 80, -2, -3, -2, -3))
list(my_slice(170, 80, 2, -3, -2, -3))
list(my_slice(170, 80, 2, 3, -2, 3))
list(my_slice(80, 170, *[2, 3, 2, 3]))
list(my_slice(-49, 32, *[2, 3, 2, 3]))


class MyList(list):
    def init(self, data):
        self.data = data

    def __getitem__(self, key):
        if isinstance(key, slice):
            return [self[i] for i in range(*key.indices(len(self)))]
        return self[key]
