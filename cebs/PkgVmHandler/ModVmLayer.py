'''
Created on 2018年12月8日

@author: Administrator
'''

import random
import time
from multiprocessing import Queue, Process
from PkgVmHandler import ModVmCfg

'''
#写进程
def write(q):
    for i in ["a","b","c","d"]:
        q.put(i)
        print("put {0} to queue".format(i))
#读进程
def read(q):
    while 1:
        result = q.get()
        print("get {0} from queue".format(result))
#主函数
def vm():
# 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pe，读入:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止
    pr.terminate()



def tup_vm_task_create(proc):
    q = Queue()
    p = Process(target=proc,args=(q,))
    #启动子进程
    p.start()
    return q

def tup_task_test1_handler(queue):
    while True:
        result = queue.get()
        print("put {0} to queue".format(result))

def tup_vm_msg_send(taskDest, msg):
    taskDest.put(msg)
'''






'''
全局常量
'''
TUP_SUCCESS = 1
TUP_FAILURE = -1
#三个基础状态
TUP_STM_NULL = 0
TUP_STM_INIT = 1
TUP_STM_COMN = 2


'''
全局配置参数
'''
class tupGlbCfg():
    def __init__(self):
        self.dbg_level = 1
        self.TUP_MSGID_MAX = 1000;
        self.TUP_STATE_MAX = 50;
        self.TUP_TASK_MAX = 200;
        self.taskTab = ['' for i in range(self.TUP_TASK_MAX)]
        
    def save_task_by_id(self, taskId, taskObj):
        if (taskId < 0) or (taskId >= self.TUP_TASK_MAX):
            return TUP_FAILURE
        self.taskTab.insert(taskId, taskObj)
        return TUP_SUCCESS;

    def get_task_by_id(self, taskId):
        if (taskId < 0) or (taskId >= self.TUP_TASK_MAX):
            return TUP_FAILURE, _
        return TUP_SUCCESS, self.taskTab[taskId]
    
    def tup_trc_print(self, taskid, string):
        ret,_ = self.get_task_by_id(taskid)
        if (ret == TUP_SUCCESS):
            print(time.asctime(), ", TRC_TSKID_", taskid, ": ", str(string))
        
TUP_GL_CFG = tupGlbCfg()


'''
基础任务模板
'''
class tupTaskTemplate():
    taskId = 0;
    taskName = '';
    queue = Queue();
    process = '';
    state = 0;
    msgStateMatrix = []   
    
    def __init__(self, taskid, taskName):
        super(tupTaskTemplate, self).__init__()
        self.taskId = taskid;
        self.taskName = taskName;
        self.queue = Queue();
        self.process = '';
        self.state = 0;
        self.msgStateMatrix = [[ '' for i in range(TUP_GL_CFG.TUP_MSGID_MAX)] for j in range(TUP_GL_CFG.TUP_STATE_MAX)]
        self.task_create();
        
    def get_task_id(self):
        return self.taskId

    def get_task_name(self):
        return self.taskName

    def get_task_queue(self):
        return self.queue

    def get_task_process(self):
        return self.process

    def fsm_set(self, newState):
        if (newState < 0) or (newState >= TUP_GL_CFG.TUP_STATE_MAX):
            self.tup_err_print("[VM ERR] fsm_set Error.")
            return -1;
        self.state = newState
        return 1;
    
    def fsm_get(self):
        return self.state

    def msg_send_in(self, msg):
        self.queue.put(msg)
        if (TUP_GL_CFG.dbg_level == 1):
            self.tup_trace(str(msg))

    def msg_send_out(self, taskDestId, msg):
        ret, taskObj = TUP_GL_CFG.get_task_by_id(taskDestId)
        if (ret == TUP_FAILURE):
            return TUP_FAILURE;
        taskObj.get_task_queue().put(msg)

    def add_stm_combine(self, state, msgid, proc):
        if (state < 0) or (state >= TUP_GL_CFG.TUP_STATE_MAX) or (msgid < 0) or (msgid >= TUP_GL_CFG.TUP_MSGID_MAX):
            print("[VM ERR] Add_stm_combine Error.")
            return -1
        self.msgStateMatrix[state][msgid] = proc
        return 1

    def task_create(self):
        self.process = Process(target=self.task_handler_enginee, args=(self.queue,))
            
    def task_handler_enginee(self, myque):
        while True:
            result = myque.get()
            msgId = int(result['mid'])
            srcId = int(result['src'])
            dstId = int(result['dst'])
            msgCont = result['content']
            if (msgId <0) or (msgId >= TUP_GL_CFG.TUP_MSGID_MAX):
                self.tup_err_print("Wrong msgId parameter.")
                continue
            if (srcId <0) or (srcId >= TUP_GL_CFG.TUP_TASK_MAX):
                self.tup_err_print("Wrong srcId parameter.")
                continue
            if (dstId <0) or (dstId >= TUP_GL_CFG.TUP_TASK_MAX):
                self.tup_err_print("Wrong dstId parameter.")
                continue
            if (dstId != self.taskId):
                self.tup_err_print("Wrong destination module, self Taskid = %d, rcvId=%d." % (self.taskId, dstId) )
                continue
            #首先确定COMN状态机，忽略当前的消息执行
            if self.msgStateMatrix[TUP_STM_COMN][msgId] != '':
                proc = self.msgStateMatrix[TUP_STM_COMN][msgId]
                if (proc(msgCont) == TUP_FAILURE):
                    self.tup_err_print("Proc execute error, Src/Dst/MsgId=%d/%d/%d, MsgContent=%s" % (srcId, dstId, msgId, str(msgCont)))
                    continue                
            #具体状态处理过程
            if self.msgStateMatrix[self.state][msgId] == '':
                self.tup_err_print("Un-valid state-message set.")
                continue
            proc = self.msgStateMatrix[self.state][msgId]
            if (proc(msgCont) == TUP_FAILURE):
                self.tup_err_print("Proc execute error, Src/Dst/MsgId=%d/%d/%d, MsgContent=%s" % (srcId, dstId, msgId, str(msgCont)))
                continue

    def task_run(self):
        self.process.start()

    def tup_trace(self, string):
        print(time.asctime(), ", [TRC] [", self.taskName, "]: ", str(string))

    def tup_dbg_print(self, string):
        print(time.asctime(), ", [DBG] [", self.taskName, "]: ", str(string))
        
    def tup_err_print(self, string):
        print(time.asctime(), ", [ERR] [", self.taskName, "]: ", str(string))
        
        
