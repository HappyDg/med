'''
Created on 2018年12月8日

@author: Administrator
'''

import random
import time
from multiprocessing import Queue, Process
from PkgVmHandler.ModVmCfg import *
from PkgVmHandler.ModVmLayer import *
from PkgCebsHandler.ModCebsCom import *
from PkgCebsHandler.ModCebsCfg import *
from PkgVmHandler.ModVmConsole import *
from PkgVmHandler.ModVmTimer import *

from PyQt5 import QtGui

class tupTaskGpar(tupTaskTemplate, clsL1_ConfigOpr):
    _STM_ACTIVE = 3
    _STM_TRAINING = 4
    
    #模块中的局部变量
    picDirFile = ''
    orgPicWidth = 0
    orgPicHeight = 0
    cfyPicWidth = 0
    cfyPicHeight = 0

    def __init__(self, glPar):
        tupTaskTemplate.__init__(self, taskid=TUP_TASK_ID_GPAR, taskName="TASK_GPAR", glTabEntry=glPar)
        #ModVmLayer.TUP_GL_CFG.save_task_by_id(ModVmCfg.TUP_TASK_ID_GPAR, self)
        self.fsm_set(TUP_STM_NULL)
        #STM MATRIX
        self.add_stm_combine(TUP_STM_INIT, TUP_MSGID_INIT, self.fsm_msg_init_rcv_handler)
        self.add_stm_combine(TUP_STM_COMN, TUP_MSGID_RESTART, self.fsm_msg_restart_rcv_handler)
        self.add_stm_combine(TUP_STM_COMN, TUP_MSGID_TIME_OUT, self.fsm_msg_time_out_rcv_handler)
        self.add_stm_combine(TUP_STM_COMN, TUP_MSGID_GPAR_INIT_INF, self.fsm_msg_init_inf_rcv_handler)

        #业务处理部分
        self.add_stm_combine(self._STM_ACTIVE, TUP_MSGID_GPAR_PIC_TRAIN_REQ, self.fsm_msg_pic_train_req_rcv_handler)
        self.add_stm_combine(self._STM_TRAINING, TUP_MSGID_GPAR_PIC_TRAIN_RESP, self.fsm_msg_pic_train_resp_rcv_handler)
        
        #START TASK
        self.fsm_set(TUP_STM_INIT)
        self.task_run()

    def fsm_msg_init_rcv_handler(self, msgContent):
        self.picDirFile = ''
        self.orgPicWidth = 0
        self.orgPicHeight = 0
        self.cfyPicWidth = 0
        self.cfyPicHeight = 0
        self.fsm_set(self._STM_ACTIVE)
        return TUP_SUCCESS;

    def fsm_msg_restart_rcv_handler(self, msgContent):
        self.fsm_set(self._STM_ACTIVE)
        return TUP_SUCCESS;
        
    def fsm_msg_time_out_rcv_handler(self, msgContent):
        return TUP_SUCCESS;

    def funcGparLogTrace(self, myString):
        self.msg_send(TUP_MSGID_TRACE, TUP_TASK_ID_UI_GPAR, myString)
        #SAVE INTO MED FILE
        self.medCmdLog(str(myString))
        #PRINT to local
        self.tup_dbg_print(str(myString))
        return
    
    def funcGparErrTrace(self, myString):
        self.msg_send(TUP_MSGID_TRACE, TUP_TASK_ID_UI_GPAR, myString)
        #SAVE INTO MED FILE
        self.medErrorLog(str(myString));
        #PRINT to local
        self.tup_err_print(str(myString))
        return        

    '''
    SERVICE PROCESSING
    '''
    def fsm_msg_init_inf_rcv_handler(self, msgContent):
        self.orgPicWidth = msgContent['orgWidth']
        self.orgPicHeight = msgContent['orgHeight']
        self.cfyPicWidth = msgContent['cfyWidth']
        self.cfyPicHeight = msgContent['cfyHeight']
 
    def fsm_msg_pic_train_req_rcv_handler(self, msgContent):
        self.funcGparLogTrace("Picture training starting!")
        self.msg_send(TUP_MSGID_GPAR_PIC_TRAIN_REQ, TUP_TASK_ID_VISION, msgContent)
        self.fsm_set(self._STM_TRAINING)
        return TUP_SUCCESS

    def fsm_msg_pic_train_resp_rcv_handler(self, msgContent):
        self.funcGparLogTrace("Picture training accomplish!")
        self.msg_send(TUP_MSGID_GPAR_PIC_TRAIN_RESP, TUP_TASK_ID_UI_GPAR, msgContent)
        self.fsm_set(self._STM_ACTIVE)
        return TUP_SUCCESS







