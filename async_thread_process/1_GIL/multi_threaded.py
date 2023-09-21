import time
from threading import Thread
from typing import List

COUNT = 100_000_000
def countdown(n):
    while n > 0:
        n -= 1


def create_threads(count_operation, count_threads, func):
    return [Thread(target=countdown, args=(count_operation // count_threads,), name=f"{i}") for i in range(count_threads)]


one_threads = create_threads(COUNT, 1, countdown)
two_threads = create_threads(COUNT, 2, countdown)
four_threads = create_threads(COUNT, 4, countdown)
eight_threads = create_threads(COUNT, 8, countdown)
twelve_threads = create_threads(COUNT, 16, countdown)
sto_threads = create_threads(COUNT, 100, countdown)


def start_threads(threads: List[Thread]):
    start = time.time()
    for thread in threads:
        thread.start()
        thread.join()

    end = time.time()
    print('Затраченное время -', end - start)


start_threads(one_threads)
start_threads(two_threads)
start_threads(four_threads)
start_threads(eight_threads)
start_threads(twelve_threads)
start_threads(sto_threads)
