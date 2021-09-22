#multiProcessing module https://docs.python.org/3/library/multiprocessing.html / https://www.youtube.com/watch?v=CRJOQtaRT_8
import multiprocessing as mp
import time
import random
import cx_Oracle
import facilities.custom_logger as c_log
import lib as l

#Check the number of CPUS
cpu_count = mp.cpu_count()
print(f"CPU Count: {cpu_count}")


# Proccess Clas -- Forked Copy Of Current Proccess
#               -- Creates new pid
#               -- runs as an independent child process
#

#1° Create a Process Object
#2º Start the proccess
#3º Terminate the process
#WARNING -- Failing to terminate process may result in resource shortage
MAX_CON = 3

log = c_log.setup('main', log_level = c_log.DEBUG)
c_log.set_output(log)

def myfunc(param, queue):
    pool = queue.get()
    s = random.uniform(1, 3)
    log.info(f"F1 - Hello {param}: wait {s}s")
    time.sleep(s)
    log.info(f"F1 - {param}: waited {s}s. -- {pool.busy} out of {MAX_CON} connections in use ")
    connection = pool.acquire()
    log.info(f"F1 - {param}: Acquired a connection:  {pool.busy} connections in use out of {MAX_CON} available ")
    time.sleep(random.uniform(5, 10))
    pool.release(connection)
    log.info(f"F1 - {param}: Released a connection:  {pool.busy} connections in use out of {MAX_CON} available ")
    

def startSessionPool():
    cx_Oracle.init_oracle_client(config_dir="oracle_config")
    pool = cx_Oracle.SessionPool(user='hisu', password='h1s_pa55', dsn ='his_dvl35cpl', min=1, max=MAX_CON, increment = 1,
         getmode=cx_Oracle.SPOOL_ATTRVAL_TIMEDWAIT)
    print(f"Pool created with {MAX_CON} connections where {pool.busy} are busy")
    return pool


def increment(param, iv):
    
    s = random.uniform(1, 3)
    log.info(f"F1 - Hello {param}: wait {s}s")
    time.sleep(s)
    #iv = queue.get()
    log.info(f"F1 - {param}: waited {s}s. -- iv is {iv} ")
    log.info(f"F1 - {param}: is inctrementing iv. current {iv}, next {iv + 1}")
    iv = iv+1
    log.info(f"F1 - {param}: is finishing. iv is {iv}")
    #queue.put(iv)
    

def main0():
    names = ['Albert', 'Alan', 'Von', 'Isac']
    processes = []
    queue = mp.Queue()
    i = 0
    queue.put(i)
    #Create and start processes for executing myfun independently
    for n in names:
        #Create Processe Object to execute my func
        proc = mp.Process(target=l.increments, args=(n,queue))
        #Store proccess
        processes.append(proc)
        #start proccess
        proc.start()

    for p in processes:   
        #terminate proccess when compeleted
        p.join() 

class MyObj:
    def __init__(self, pool):
        super().__init__()
        self.pool = pool

def main1():
    names = ['Albert', 'Alan', 'Von', 'Isac']
    
    processes = []
    pool = startSessionPool()
 
    queue = mp.Queue()
    for i in range(MAX_CON):
        queue.put(pool)
    print("starting subprocces")
    ##Create and start processes for executing myfun independently
    #for n in names:
    #    #Create Processe Object to execute my func
    #    proc = mp.Process(target=myfunc, args=(n,queue))
    #    #Store proccess
    #    processes.append(proc)
    #    #start proccess
    #    proc.start()
#
    #for p in processes:   
    #    #terminate proccess when compeleted
    #    p.join() 

#main0()
main1()
#Class mp.Lock -- Semaphores
#Class mp.Queue -- Channels
#Class mp. -- Maps array of inputs to multiple proccess to execute a target function



