import random
import multiprocessing as mp
import time
import logging
log = logging.getLogger('main')
def increments(param, queue):
    s = random.uniform(1, 3)
    log.info(f"F1 - Hello {param}: wait {s}s")
    time.sleep(s)
    iv = queue.get()
    log.info(f"F1 - {param}: waited {s}s. -- iv is {iv} ")
    log.info(f"F1 - {param}: is inctrementing iv. current {iv}, next {iv + 1}")
    iv = iv+1
    log.info(f"F1 - {param}: is finishing. iv is {iv}")
    queue.put(iv)
    