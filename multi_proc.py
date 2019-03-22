import multiprocessing
import subprocess
import time

def myping(ip):
    return not subprocess.run(["ping", "-n", "1",ip],stdout=subprocess.PIPE).returncode

def start_process():
    print('Starting', multiprocessing.current_process().name)

if __name__ == '__main__':
    ips = [ip.strip() for ip in open("ip.txt") if ip.startswith("G")]
    print('Input   :', ips)

    start = time.time()
    pool_size = multiprocessing.cpu_count() * 2
    pool = multiprocessing.Pool(
        processes=pool_size,
        initializer=start_process,
    )
    pool_outputs = pool.map(myping, ips)
    pool.close()  # no more tasks
    pool.join()  # wrap up current tasks
    end = time.time()
    print('Output    :', pool_outputs)
    print(start - end)


