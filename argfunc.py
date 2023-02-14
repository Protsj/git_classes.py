def avg(*iterable):
    iterable_func = sum(iterable) / len(iterable)
    return iterable_func
'''EXAMPLE'''
print(avg(100,200,300,400))