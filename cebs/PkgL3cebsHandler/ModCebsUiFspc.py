'''
Created on 2019年1月22日

@author: Administrator
'''

####!/usr/bin/python3.6
#### -*- coding: UTF-8 -*-

import random
import time
import json
from multiprocessing import Queue, Process
from PkgL1vmHandler.ModVmCfg import *
from PkgL1vmHandler.ModVmLayer import *
from PkgL3cebsHandler.ModCebsCom import *
from PkgL3cebsHandler.ModCebsCfg import *
from PkgL1vmHandler.ModVmConsole import *


class tupTaskUiFspc(tupTaskTemplate, clsL1_ConfigOpr):
    _STM_ACTIVE = 3
    _STM_DEACT  = 4 #界面没激活

    def __init__(self, glPar):
        tupTaskTemplate.__init__(self, taskid=TUP_TASK_ID_UI_FSPC, taskName="TASK_UI_FSPC", glTabEntry=glPar)
        self.fsm_set(TUP_STM_NULL)
        self.fatherUiObj = ''   #父对象界面，双向通信
        #STM MATRIX
        self.add_stm_combine(TUP_STM_INIT, TUP_MSGID_INIT, self.fsm_msg_init_rcv_handler)
        self.add_stm_combine(TUP_STM_COMN, TUP_MSGID_RESTART, self.fsm_com_msg_restart_rcv_handler)
        self.add_stm_combine(TUP_STM_COMN, TUP_MSGID_EXIT, self.fsm_com_msg_exit_rcv_handler)
        self.add_stm_combine(TUP_STM_COMN, TUP_MSGID_TEST, self.fsm_com_msg_test_rcv_handler)
        self.add_stm_combine(TUP_STM_COMN, TUP_MSGID_TRACE, self.fsm_msg_trace_inc_rcv_handler)
        self.add_stm_combine(TUP_STM_COMN, TUP_MSGID_FSPC_UI_SWITCH, self.fsm_msg_ui_focus_rcv_handler)

        #业务态
        self.add_stm_combine(self._STM_ACTIVE, TUP_MSGID_FSPC_CMD_S1_RESP, self.fsm_msg_cmd_s1_resp_rcv_handler)
        self.add_stm_combine(self._STM_ACTIVE, TUP_MSGID_FSPC_CMD_S2_RESP, self.fsm_msg_cmd_s2_resp_rcv_handler)
        self.add_stm_combine(self._STM_ACTIVE, TUP_MSGID_FSPC_CMD_S3_RESP, self.fsm_msg_cmd_s3_resp_rcv_handler)
        self.add_stm_combine(self._STM_ACTIVE, TUP_MSGID_FSPC_CMD_S4_RESP, self.fsm_msg_cmd_s4_resp_rcv_handler)
        self.add_stm_combine(self._STM_ACTIVE, TUP_MSGID_FSPC_CMD_S5_RESP, self.fsm_msg_cmd_s5_resp_rcv_handler)
        self.add_stm_combine(self._STM_ACTIVE, TUP_MSGID_FSPC_CMD_S6_RESP, self.fsm_msg_cmd_s6_resp_rcv_handler)
        self.add_stm_combine(self._STM_ACTIVE, TUP_MSGID_FSPC_CMD_S7_RESP, self.fsm_msg_cmd_s7_resp_rcv_handler)
        self.add_stm_combine(self._STM_ACTIVE, TUP_MSGID_FSPC_CMD_SUM_RESP, self.fsm_msg_cmd_sum_resp_rcv_handler)

        #START TASK
        self.fsm_set(TUP_STM_INIT)
        self.task_run()

    def fsm_msg_init_rcv_handler(self, msgContent):
        self.fsm_set(self._STM_DEACT)
        return TUP_SUCCESS;

    def fsm_msg_trace_inc_rcv_handler(self, msgContent):
        self.funcDebugPrint2Qt(msgContent);
        return TUP_SUCCESS;
        
    #界面切换进来
    def fsm_msg_ui_focus_rcv_handler(self, msgContent):
        self.fsm_set(self._STM_ACTIVE)
        return TUP_SUCCESS;
    
    #将界面对象传递给本任务，以便将打印信息送到界面上
    def funcSaveFatherInst(self, instance):
        self.fatherUiObj = instance
    
    def funcDebugPrint2Qt(self, string):
        if (self.fatherUiObj == ''):
            print("FSPC_UI task lose 1 print message due to time sync.")
        else:
            self.fatherUiObj.cetk_debug_print(str(string))

    #界面切走
    def func_ui_click_fspc_switch_to_main(self):
        print("I am func_ui_click_fspc_switch_to_main!")
        self.fsm_set(self._STM_DEACT)       

    #清理各项操作
    def func_ui_click_fspc_close(self):
        print("I am func_ui_click_fspc_close!")
        #暂时没有要做的，所以不发送消息给FSPC模块

            
    #业务状态处理过程

    #主界面承接过来的执行函数
    #parInput = (parMarkLine, parAreaMin, parAreaMax, parAreaDilate, parAreaErode, parCellMin, parCellMax, parRaduisMin, parRaduisMax, parCellDilate, parCellErode, parCellCe, parCellDist, addupSet)
    def func_ui_click_cmd_s1(self, fileName, parInput):
        print("I am func_ui_click_cmd_s1!")
        mbuf = self.proc_cmd_store_into_buffer(fileName, parInput)
        self.msg_send(TUP_MSGID_FSPC_CMD_S1_REQ, TUP_TASK_ID_FSPC, mbuf)

    def func_ui_click_cmd_s2(self, fileName, parInput):
        print("I am func_ui_click_cmd_s2!")
        mbuf = self.proc_cmd_store_into_buffer(fileName, parInput)
        self.msg_send(TUP_MSGID_FSPC_CMD_S2_REQ, TUP_TASK_ID_FSPC, mbuf)

    def func_ui_click_cmd_s3(self, fileName, parInput):
        print("I am func_ui_click_cmd_s3!")
        mbuf = self.proc_cmd_store_into_buffer(fileName, parInput)
        self.msg_send(TUP_MSGID_FSPC_CMD_S3_REQ, TUP_TASK_ID_FSPC, mbuf)

    def func_ui_click_cmd_s4(self, fileName, parInput):
        print("I am func_ui_click_cmd_s4!")
        mbuf = self.proc_cmd_store_into_buffer(fileName, parInput)
        self.msg_send(TUP_MSGID_FSPC_CMD_S4_REQ, TUP_TASK_ID_FSPC, mbuf)

    def func_ui_click_cmd_s5(self, fileName, parInput):
        print("I am func_ui_click_cmd_s5!")
        mbuf = self.proc_cmd_store_into_buffer(fileName, parInput)
        self.msg_send(TUP_MSGID_FSPC_CMD_S5_REQ, TUP_TASK_ID_FSPC, mbuf)

    def func_ui_click_cmd_s6(self, fileName, parInput):
        print("I am func_ui_click_cmd_s6!")
        mbuf = self.proc_cmd_store_into_buffer(fileName, parInput)
        self.msg_send(TUP_MSGID_FSPC_CMD_S6_REQ, TUP_TASK_ID_FSPC, mbuf)

    def func_ui_click_cmd_s7(self, fileName, parInput):
        print("I am func_ui_click_cmd_s7!")
        mbuf = self.proc_cmd_store_into_buffer(fileName, parInput)
        self.msg_send(TUP_MSGID_FSPC_CMD_S7_REQ, TUP_TASK_ID_FSPC, mbuf)

    def func_ui_click_cmd_sum(self, fileName, parInput):
        print("I am func_ui_click_cmd_sum!")
        mbuf = self.proc_cmd_store_into_buffer(fileName, parInput)
        self.msg_send(TUP_MSGID_FSPC_CMD_SUM_REQ, TUP_TASK_ID_FSPC, mbuf)
    
    def proc_cmd_store_into_buffer(self, fileName, parInput):
        mbuf={}
        mbuf['fileName'] = fileName
        index=-1;
        index+=1; mbuf['markLine'] = parInput[index]; 
        index+=1; mbuf['markWidth'] = parInput[index]; 
        index+=1; mbuf['markArea'] = parInput[index]; 
        index+=1; mbuf['markDilate'] = parInput[index]; 
        index+=1; mbuf['areaMin'] = parInput[index];
        index+=1; mbuf['areaMax'] = parInput[index];
        index+=1; mbuf['areaDilate'] = parInput[index];
        index+=1; mbuf['areaErode'] = parInput[index];
        index+=1; mbuf['cellMin'] = parInput[index];
        index+=1; mbuf['cellMax'] = parInput[index];
        index+=1; mbuf['raduisMin'] = parInput[index];
        index+=1; mbuf['raduisMax'] = parInput[index];
        index+=1; mbuf['cellDilate'] = parInput[index];
        index+=1; mbuf['cellErode'] = parInput[index];
        index+=1; mbuf['cellCe'] = parInput[index];
        index+=1; mbuf['cellDist'] = parInput[index];
        index+=1; mbuf['addupSet'] = parInput[index];
        return mbuf

    #业务态
    def fsm_msg_cmd_s1_resp_rcv_handler(self, msgContent):
        if (msgContent['res'] < 0):
            self.funcDebugPrint2Qt("Cmd1 exect failure! Error with [%s]" % (msgContent['errInfo']));
        else:
            if (self.fatherUiObj != ''):
                if (msgContent['res'] > 0) and (msgContent['totalCnt'] >= 2):
                    self.fatherUiObj.fspc_callback_cmd_exec_resp(msgContent['fileName1'])
                if (msgContent['res'] > 0) and (msgContent['totalCnt'] >= 3):
                    time.sleep(5)
                    self.fatherUiObj.fspc_callback_cmd_exec_resp(msgContent['fileName2'])
                if (msgContent['res'] > 0) and (msgContent['totalCnt'] >= 1):
                    time.sleep(5)
                    self.fatherUiObj.fspc_callback_cmd_exec_resp(msgContent['fileName'])
        return TUP_SUCCESS;

    def fsm_msg_cmd_s2_resp_rcv_handler(self, msgContent):
        if (msgContent['res'] < 0):
            self.funcDebugPrint2Qt("Cmd2 exect failure! Error with [%s]" % (msgContent['errInfo']));
        else:
            if (self.fatherUiObj != ''):
                self.fatherUiObj.fspc_callback_cmd_exec_resp(msgContent['fileName'])
        return TUP_SUCCESS;

    def fsm_msg_cmd_s3_resp_rcv_handler(self, msgContent):
        if (msgContent['res'] < 0):
            self.funcDebugPrint2Qt("Cmd3 exect failure! Error with [%s]" % (msgContent['errInfo']));
        else:
            if (self.fatherUiObj != ''):
                self.fatherUiObj.fspc_callback_cmd_exec_resp(msgContent['fileName'])
        return TUP_SUCCESS;

    def fsm_msg_cmd_s4_resp_rcv_handler(self, msgContent):
        if (msgContent['res'] < 0):
            self.funcDebugPrint2Qt("Cmd4 exect failure! Error with [%s]" % (msgContent['errInfo']));
        else:
            if (self.fatherUiObj != ''):
                self.fatherUiObj.fspc_callback_cmd_exec_resp(msgContent['fileName'])
        return TUP_SUCCESS;

    def fsm_msg_cmd_s5_resp_rcv_handler(self, msgContent):
        if (msgContent['res'] < 0):
            self.funcDebugPrint2Qt("Cmd5 exect failure! Error with [%s]" % (msgContent['errInfo']));
        else:
            if (self.fatherUiObj != ''):
                self.fatherUiObj.fspc_callback_cmd_exec_resp(msgContent['fileName'])
        return TUP_SUCCESS;

    def fsm_msg_cmd_s6_resp_rcv_handler(self, msgContent):
        if (msgContent['res'] < 0):
            self.funcDebugPrint2Qt("Cmd6 exect failure! Error with [%s]" % (msgContent['errInfo']));
        else:
            if (self.fatherUiObj != ''):
                self.fatherUiObj.fspc_callback_cmd_exec_resp(msgContent['fileName'])
        return TUP_SUCCESS;

    def fsm_msg_cmd_s7_resp_rcv_handler(self, msgContent):
        if (msgContent['res'] < 0):
            self.funcDebugPrint2Qt("Cmd7 exect failure! Error with [%s]" % (msgContent['errInfo']));
        else:
            if (self.fatherUiObj != ''):
                self.fatherUiObj.fspc_callback_cmd_exec_resp(msgContent['fileName'])
        return TUP_SUCCESS;

    def fsm_msg_cmd_sum_resp_rcv_handler(self, msgContent):
        if (msgContent['res'] < 0):
            self.funcDebugPrint2Qt("CmdSum exect failure! Error with [%s]" % (msgContent['errInfo']));
        else:
            if (self.fatherUiObj != ''):
                self.fatherUiObj.fspc_callback_cmd_exec_resp(msgContent['fileName'])
        return TUP_SUCCESS;























