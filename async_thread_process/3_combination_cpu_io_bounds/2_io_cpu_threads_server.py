from threading import Thread

from server import run_server,compute

if __name__ == '__main__':
    Thread(target=compute).start()
    run_server()
