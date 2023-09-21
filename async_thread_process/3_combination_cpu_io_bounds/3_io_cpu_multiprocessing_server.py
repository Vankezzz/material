from multiprocessing import Process

from server import run_server,compute

if __name__ == '__main__':
    Process(target=compute).start()
    run_server()

