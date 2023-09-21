from threading import BrokenBarrierError
from time import sleep
from random import random
from multiprocessing import Process
from multiprocessing import Barrier, Event, Condition, Lock, Semaphore


# custom function to be executed in a child process
def task(shared_barrier, ident):
    # generate a unique value between 0 and 10
    value = random() * 10
    # block for a moment
    sleep(value)
    # report result
    print(f'Process {ident} got: {value}', flush=True)
    # wait for all other processes to complete
    shared_barrier.wait()


# protect the entry point
if __name__ == '__main__':
    # Создание barrier для (5 workers + 1 main process)
    barrier_num = 5 + 1
    # Количество workers + 1 главный процесс приложения
    workers_num = barrier_num - 1
    # Будет просто висеть, потому что последний барьер никто не выполняет - закроется по timeout
    # workers_num = barrier_num - 2
    # Запуск на 1 больше worker, чем процессов - в итоге после завершения барьера выполнится еще один
    # workers_num = barrier_num

    # timeout=10 - по истечению BrokenBarrierError и Barrier будет помечен как сломанный
    barrier = Barrier(barrier_num)
    # create the worker processes
    workers = [Process(target=task,
                       args=(barrier, i)) for i in range(6)]
    # start the worker processes
    for worker in workers:
        # start process
        worker.start()
    # wait for all worker processes to finish
    print('Main process waiting on all results...')
    # Это блокирующий вызов, который вернется, как только все остальные процессы
    # (заранее настроенное количество сторон) достигнут барьера.
    try:
        barrier.wait()
        # ToDo Параметры barrier - party, n_waiting, broken
    except BrokenBarrierError:
        # сбрасываем барьер для перезапуска - ToDo не знаю примера
        barrier.reset()
    print('All processes have their result')
