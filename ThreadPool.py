import threading
import queue


class task:
    def __init__(self, method,  *args):
        self.func = method
        self.args = args
    def exec(self):
        if self.args:
            self.func(self.args)
        else: 
            self.func()
            
class workerQ:
    def __init__(self, nThreads):
        self.nThreads = nThreads
        self.task_q = queue.Queue()
        self.threads_pool = []
        
    def start_workers(self):
        for i in range(self.nThreads):
            t_name = "thread-"+str(i)
            t = threading.Thread(target = self.work, name = t_name )
            t.start()
            self.threads_pool.append(t)
    
    def stop_workers(self):            
        for i in range(self.nThreads):
            t.join()

    def join(self):
        for i in range(self.nThreads):
            self.addtask(None)

        self.task_q.join()
        print("q joined")
        self.stop_workers()
        print("workers joined")
        
    
    def work(self):
        while True:
            work_task = self.task_q.get(True, None)
            if work_task == None:
                print("exiting")
                break
            else:
                try:
                    work_task.exec()
                    self.task_q.task_done()
                except Exception as e:
                    print("runtime exception {}".format(e))
    def addtask(self, t):
        self.task_q.put(t)
        
def print_num(num):
    print ("printing: {}".format(num[0]))

if __name__ == "__main__":
    wq = workerQ(10)
    wq.start_workers()
    for i in range(10):
        t = task(print_num, i)
#         t.exec()
        wq.addtask(t)

    wq.join()
    
    
    
                

    