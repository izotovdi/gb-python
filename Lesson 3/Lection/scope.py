# number = 1
#
#
# def increment():
#     number += 1
#
#
# increment()

def top_func():
    stat = 0

    def inner_func():
        nonlocal stat
        stat += 1

    inner_func()
    print(stat)


top_func()
