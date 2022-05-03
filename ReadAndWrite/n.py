def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value


# Note that the initializer, when not None, is used as the first value instead of the first value from iterable , and after the whole iterable.
tup = ()
print(reduce(lambda x, y: x + y, tup, 0))
