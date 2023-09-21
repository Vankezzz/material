from time import sleep
from multiprocessing import Process, active_children, current_process
from prettytable import PrettyTable

report_table = PrettyTable()
report_table.field_names = ["Stage", "Name", "PID", "Parent PID", "IsAlive", "IsDaemon", "ExitCode"]


# custom function to be executed in a child process
def task(process_num):
    print(f'task {process_num} is started', flush=True)
    # block for a moment
    sleep(1)
    # report a message
    print(f'task {process_num} is finished', flush=True)


# custom process class
class CustomProcess(Process):
    # override the run function
    def run(self):
        task()


def print_report(process: Process, stage: str):
    report_table.add_row([
        stage,
        process.name,
        process.pid,
        process._parent_pid,
        process.is_alive(),
        process.daemon,
        process.exitcode,
    ])


if __name__ == '__main__':
    # get the current process
    process = current_process()
    # report details
    print_report(process, "Before Creating")

    # create a new process instance
    process = Process(
        target=task,
        name='MyProcess',
        args=(1, )
    )
    print_report(process, "Creating")

    # start executing the function in the process
    process.start()
    print_report(process, "Starting")
    # wait for the process to finish
    print('Waiting for the process...')
    process.join()
    print_report(process, "Finished")

    print(report_table)
    # # create the process
    # process = CustomProcess()
    # # start the process
    # process.start()
    # # wait for the process to finish
    #
    # # wait for the process to finish
    # print('Waiting for the process...')
    # process.join()
    #
    #
    #
    #
    # # create a number of child processes
    # processes = [Process(target=task) for _ in range(5)]
    # # start the child processes
    # for process in processes:
    #     process.start()
    # # get a list of all active child processes
    # children = active_children()
    # # report a count of active children
    # print(f'Active Children Count: {len(children)}')
    # # report each in turn
    # for child in children:
    #     print(child)
    #

    # # create a daemon process
    # process = Process(daemon=True)
    # # report if the process is a daemon
    # print(process.daemon)