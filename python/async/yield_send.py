def jumping_range(up_to):
    """Generator for the sequence of integers from 0 to up_to, exclusive.

    Sending a value into the generator will shift the sequence by that amount.
    """
    index = 0
    while index < up_to:
        jump = yield index
        if jump is None:
            jump = 1
        index += jump


def lazy_range(up_to):
    """Generator to return the sequence of integers from 0 to up_to, exclusive."""
    index = 0
    def gratuitous_refactor():
        nonlocal index
        while index < up_to:
            yield index
            index += 1
    yield from gratuitous_refactor()


if __name__ == '__main__':
    print('start..')
    iterator = jumping_range(20)
    print(next(iterator)) 
    print(iterator.send(15))
    print(next(iterator)) 
    #print(iterator.send(-1))  # 2
    for x in iterator:
        print(x)  # 3, 4

    i = lazy_range(10)
    for x in i:
        print(x)
