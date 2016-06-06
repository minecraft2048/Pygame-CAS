import multiprocessing
import time
import sys
import queue

q = queue.Queue()
q.put('test')


def daemon(out_q):
    while True:
        out_q.put('hi')
        print(out_q.get())
        time.sleep(2)



d = multiprocessing.Process(name='daemon', target=daemon, args=(q,))
d.daemon = True
d.start()

while True:
    print(q.get())
    time.sleep(1)
