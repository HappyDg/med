'''
Created on 2018/5/2

@author: Administrator
'''

####!/usr/bin/python3.6
#### -*- coding: UTF-8 -*-

import random
import sys
import time
import json
import os
import re
import urllib
import http
import socket
import datetime
import string
import ctypes 
import random
import cv2 as cv
import numpy as np  
from ctypes import c_uint8
from cv2 import waitKey

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot

# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

#Local include
from cebsMain import *
from PkgCebsHandler import ModCebsCom
from PkgCebsHandler import ModCebsCfg
from PkgCebsHandler import ModCebsVision
from PkgCebsHandler import ModCebsMoto
from PkgCebsHandler import ModCebsCtrl


#校准处理过程
#模块只能被CalibForm调用，所以打印只会打到CalibForm上去
class clsL3_CalibProc(object):
    def __init__(self, father):
        super(clsL3_CalibProc, self).__init__()
        self.identity = None;
        self.instL4CalibForm = father
        self.instL1ConfigOpr=ModCebsCfg.clsL1_ConfigOpr();
        self.instL2MotoProc=ModCebsMoto.clsL2_MotoProc(self.instL4CalibForm, 2);
        self.instL2VisCapProc=ModCebsVision.clsL2_VisCapProc(self.instL4CalibForm, 2);
        self.initParameter();

    def initParameter(self):
        #STEP1: 判定产品型号
        if (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_96_STANDARD):
            ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_BATCH_MAX;
        elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_48_STANDARD):
            ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH = ModCebsCom.GL_CEBS_HB_TARGET_48_SD_BATCH_MAX;
        elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_24_STANDARD):
            ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH = ModCebsCom.GL_CEBS_HB_TARGET_24_SD_BATCH_MAX;
        elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_12_STANDARD):
            ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH = ModCebsCom.GL_CEBS_HB_TARGET_12_SD_BATCH_MAX;
        elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_6_STANDARD):
            ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH = ModCebsCom.GL_CEBS_HB_TARGET_6_SD_BATCH_MAX;
        else:
            ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_BATCH_MAX;
        #STEP2：初始化工作环境
        self.funcInitHoleBoardPar();
        self.funcCleanWorkingEnv()
        #STEP3：初始化Pilot任务
        self.instL2CalibPiThd = clsL2_CalibPilotThread(self.instL4CalibForm, self.instL2MotoProc)
        self.instL2CalibPiThd.setIdentity("TASK_CalibPilotThread")
        self.instL2CalibPiThd.sgL3CalibFormPrtLog.connect(self.funcCalibLogTrace)
        self.instL2CalibPiThd.sgL2PiStart.connect(self.instL2CalibPiThd.funcCalibMotoPilotStart)
        self.instL2CalibPiThd.sgL2PiStop.connect(self.instL2CalibPiThd.funcCalibMotoPilotStop)
        self.instL2CalibPiThd.start();
        #STEP3：初始化摄像头视频展示任务 #SETUP 2nd task
        self.instL2CalibCamDisThd = clsL2_CalibCamDispThread(self.instL4CalibForm)
        self.instL2CalibCamDisThd.setIdentity("TASK_CalibCameraDisplay")
        self.instL2CalibCamDisThd.sgL3CalibFormPrtLog.connect(self.funcCalibLogTrace)
        self.instL2CalibCamDisThd.sgL2CamDiStart.connect(self.instL2CalibCamDisThd.funcCalibCameraDispStart)
        self.instL2CalibCamDisThd.sgL2CamDiStop.connect(self.instL2CalibCamDisThd.funcCalibCameraDispStop)
        self.instL2CalibCamDisThd.start();
        self.funcCalibLogTrace("L3CALIB: Instance start test!")
                        
    def setIdentity(self,text):
        self.identity = text

    def funcCalibLogTrace(self, myString):
        self.instL4CalibForm.calib_print_log(myString)

    def funcCleanWorkingEnv(self):
        if (self.instL2MotoProc.funcMotoRunningStatusInquery() == True):
            self.instL2MotoProc.funcMotoStop()        
        self.instL2VisCapProc.funcVisionClasEnd()

    def funcRecoverWorkingEnv(self):
        self.instL2MotoProc.funcMotoStop();
    
    def funcInitHoleBoardPar(self):
        if (ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE == 0 or ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE == 0 or ModCebsCom.GL_CEBS_HB_HOLE_X_NUM == 0 or ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM == 0):
            if (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_96_STANDARD):
                ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_XDIR_NBR;
                ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_YDIR_NBR;
                ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_X_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_X_NUM-1);
                ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_Y_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM-1);
            elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_48_STANDARD):
                ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = ModCebsCom.GL_CEBS_HB_TARGET_48_SD_XDIR_NBR;
                ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = ModCebsCom.GL_CEBS_HB_TARGET_48_SD_YDIR_NBR;
                ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_48_SD_X_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_X_NUM-1);
                ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_48_SD_Y_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM-1);
            elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_24_STANDARD):
                ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = ModCebsCom.GL_CEBS_HB_TARGET_24_SD_XDIR_NBR;
                ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = ModCebsCom.GL_CEBS_HB_TARGET_24_SD_YDIR_NBR;
                ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_24_SD_X_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_X_NUM-1);
                ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_24_SD_Y_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM-1);
            elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_12_STANDARD):
                ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = ModCebsCom.GL_CEBS_HB_TARGET_12_SD_XDIR_NBR;
                ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = ModCebsCom.GL_CEBS_HB_TARGET_12_SD_YDIR_NBR;
                ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_12_SD_X_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_X_NUM-1);
                ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_12_SD_Y_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM-1);
            elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_6_STANDARD):
                ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = ModCebsCom.GL_CEBS_HB_TARGET_6_SD_XDIR_NBR;
                ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = ModCebsCom.GL_CEBS_HB_TARGET_6_SD_YDIR_NBR;
                ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_6_SD_X_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_X_NUM-1);
                ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_6_SD_Y_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM-1);
            else:
                ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_XDIR_NBR;
                ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_YDIR_NBR;
                ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_X_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_X_NUM-1);
                ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_Y_MAX / (ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM-1);

        if (ModCebsCom.GL_CEBS_HB_POS_IN_UM[0] !=0 or ModCebsCom.GL_CEBS_HB_POS_IN_UM[1] !=0 or ModCebsCom.GL_CEBS_HB_POS_IN_UM[2] !=0 or ModCebsCom.GL_CEBS_HB_POS_IN_UM[3] !=0):
            xWidth = ModCebsCom.GL_CEBS_HB_POS_IN_UM[2] - ModCebsCom.GL_CEBS_HB_POS_IN_UM[0];
            yHeight = ModCebsCom.GL_CEBS_HB_POS_IN_UM[1] - ModCebsCom.GL_CEBS_HB_POS_IN_UM[3];
            ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE = xWidth / (ModCebsCom.GL_CEBS_HB_HOLE_X_NUM-1);
            ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE = yHeight / (ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM-1);
        else:
            pass        
    
    def funcUpdateHoleBoardPar(self):
        if (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_96_STANDARD):
            ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_XDIR_NBR;
            ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_YDIR_NBR;
        elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_48_STANDARD):
            ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = ModCebsCom.GL_CEBS_HB_TARGET_48_SD_XDIR_NBR;
            ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = ModCebsCom.GL_CEBS_HB_TARGET_48_SD_YDIR_NBR;
        elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_24_STANDARD):
            ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = ModCebsCom.GL_CEBS_HB_TARGET_24_SD_XDIR_NBR;
            ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = ModCebsCom.GL_CEBS_HB_TARGET_24_SD_YDIR_NBR;
        elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_12_STANDARD):
            ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = ModCebsCom.GL_CEBS_HB_TARGET_12_SD_XDIR_NBR;
            ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = ModCebsCom.GL_CEBS_HB_TARGET_12_SD_YDIR_NBR;
        elif (ModCebsCom.GL_CEBS_HB_TARGET_TYPE == ModCebsCom.GL_CEBS_HB_TARGET_6_STANDARD):
            ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = ModCebsCom.GL_CEBS_HB_TARGET_6_SD_XDIR_NBR;
            ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = ModCebsCom.GL_CEBS_HB_TARGET_6_SD_YDIR_NBR;
        else:
            ModCebsCom.GL_CEBS_HB_HOLE_X_NUM = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_XDIR_NBR;
            ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM = ModCebsCom.GL_CEBS_HB_TARGET_96_SD_YDIR_NBR;
        ModCebsCom.GL_CEBS_HB_WIDTH_X_SCALE = (ModCebsCom.GL_CEBS_HB_POS_IN_UM[0] - ModCebsCom.GL_CEBS_HB_POS_IN_UM[2]) / (ModCebsCom.GL_CEBS_HB_HOLE_X_NUM-1);
        ModCebsCom.GL_CEBS_HB_HEIGHT_Y_SCALE = (ModCebsCom.GL_CEBS_HB_POS_IN_UM[1] - ModCebsCom.GL_CEBS_HB_POS_IN_UM[3]) / (ModCebsCom.GL_CEBS_HB_HOLE_Y_NUM-1);

    def funcCheckHoldNumber(self, holeNbr):
        if (holeNbr <= 0):
            return 1;
        if (holeNbr >= ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH):
            return ModCebsCom.GL_CEBS_PIC_ONE_WHOLE_BATCH
        return holeNbr

    def funcCalibPilotStart(self):
        self.funcCalibLogTrace("L3CALIB: PILOT STARTING...")
        self.instL2CalibPiThd.sgL2PiStart.emit()

    def funcCalibPilotMove0(self):
        self.funcCalibLogTrace("L3CALIB: Move to Hole#0 point.")
        res, string = self.instL2MotoProc.funcMotoMove2Start()
        if (res < 0):
            self.funcCalibLogTrace("L3CALIB: Moving to start point error!")
            return -2;
        print("L3CALIB: " + string)
        return 1;
        
    def funcCalibPilotMoven(self, holeNbr):
        outputStr = "L3CALIB: Starting move to Hole#%d point." % (holeNbr)
        self.funcCalibLogTrace(outputStr)
        newHoldNbr = self.funcCheckHoldNumber(holeNbr)
        res = self.instL2MotoProc.funcMotoMove2HoleNbr(newHoldNbr)
        if (res < 0):
            outputStr = "L3CALIB: Move to Hole#%d point error!" % (newHoldNbr)
            self.funcCalibLogTrace(outputStr)
            return -1;
        else:
            outputStr = "L3CALIB: Move to Hole#%d point success!" % (newHoldNbr)
            self.funcCalibLogTrace(outputStr)
            return 1;
    
    def funcCalibPilotStop(self):
        self.funcCalibLogTrace("L3CALIB: PILOT STOP...")
        self.instL2CalibPiThd.sgL2PiStop.emit()
        self.instL2CalibCamDisThd.sgL2CamDiStop.emit()

    #Using different function/api to find the right position
    #pos = self.instL4CalibForm.size()
    #pos = self.instL4CalibForm.rect()
    #geometry will return (left, top, width, height)
    def funcCalibPilotCameraEnable(self):
        self.funcCalibLogTrace("L3CALIB: PILOT CEMERA ENABLE...")
        pos = self.instL4CalibForm.geometry()
        ModCebsCom.GL_CEBS_CAMERA_DISPLAY_POS_X = pos.x() + 420
        ModCebsCom.GL_CEBS_CAMERA_DISPLAY_POS_Y = pos.y() + 10
        #print(ModCebsCom.GL_CEBS_CAMERA_DISPLAY_POS_X, ModCebsCom.GL_CEBS_CAMERA_DISPLAY_POS_Y)    
        self.instL2CalibCamDisThd.sgL2CamDiStart.emit()

    #FINISH all the pilot functions
    def funcCtrlCalibComp(self):
        self.instL2CalibCamDisThd.sgL2CamDiStop.emit()
        self.funcUpdateHoleBoardPar()
        self.funcRecoverWorkingEnv()

    def funcCalibMove(self, parMoveScale, parMoveDir):
        self.instL2MotoProc.funcMotoCalaMoveOneStep(parMoveScale, parMoveDir);
        self.funcCalibLogTrace("L3CALIB: Moving one step. Current position XY=[%d/%d]." % (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0], ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1]))

    def funcCalibForceMove(self, parMoveDir):
        self.instL2MotoProc.funcMotoFmCalaMoveOneStep(parMoveDir);
        self.funcCalibLogTrace("L3CALIB: Force moving one step. Current position XY=[%d/%d]." % (ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0], ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1]))
        
    def funcCalibRightUp(self):
        ModCebsCom.GL_CEBS_HB_POS_IN_UM[2] = ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0];
        ModCebsCom.GL_CEBS_HB_POS_IN_UM[3] = ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1];
        self.funcUpdateHoleBoardPar()
        iniObj = ModCebsCfg.clsL1_ConfigOpr();
        iniObj.updateSectionPar();
        self.funcCalibLogTrace("L3CALIB: RightBottom Axis set!  XY=%d/%d." % (ModCebsCom.GL_CEBS_HB_POS_IN_UM[2], ModCebsCom.GL_CEBS_HB_POS_IN_UM[3]))       

    def funcCalibLeftDown(self):
        ModCebsCom.GL_CEBS_HB_POS_IN_UM[0] = ModCebsCom.GL_CEBS_CUR_POS_IN_UM[0];
        ModCebsCom.GL_CEBS_HB_POS_IN_UM[1] = ModCebsCom.GL_CEBS_CUR_POS_IN_UM[1];
        self.funcUpdateHoleBoardPar()
        iniObj = ModCebsCfg.clsL1_ConfigOpr();
        iniObj.updateSectionPar();
        self.funcCalibLogTrace("L3CALIB: LeftUp Axis set! XY=%d/%d." % (ModCebsCom.GL_CEBS_HB_POS_IN_UM[0], ModCebsCom.GL_CEBS_HB_POS_IN_UM[1]))

#Pilot thread, control moto moving and accomplish activities
#只可能被CalibForm调用，所以father传进去后，只能被它锁调用
class clsL2_CalibPilotThread(QThread):
    sgL3CalibFormPrtLog = pyqtSignal(str)
    sgL2PiStart = pyqtSignal()
    sgL2PiStop = pyqtSignal()

    def __init__(self, father, instMotoHandler):
        super(clsL2_CalibPilotThread, self).__init__()
        self.identity = None;
        self.instL4CalibForm = father
        self.instMotoHandler = instMotoHandler
        self.cntCtrl = -1;
        '''简化Class调用过程
        #self.instL2MotoProc = ModCebsMoto.clsL2_MotoProc(self.instL4CalibForm, 2);
        '''
        self.funcCalibPiLogTrace("L2CALPI: Instance start test!")

    def setIdentity(self,text):
        self.identity = text

    def funcCalibPiLogTrace(self, myString):
        self.instL4CalibForm.calib_print_log(myString)
                
    def funcCalibMotoPilotStart(self):
        self.cntCtrl = ModCebsCom.GL_CEBS_PILOT_WOKING_ROUNDS_MAX+1;

    def funcCalibMotoPilotStop(self):
        self.cntCtrl = 1;

    #OPTIMIZE PILOT WORKING METHOD
    def funcMotoCalibPilotWorkingOnces(self):
        self.instMotoHandler.funcMotoMove2HoleNbr(1);
        self.instMotoHandler.funcMotoMove2HoleNbr(ModCebsCom.GL_CEBS_HB_HOLE_X_NUM);
        self.instMotoHandler.funcMotoMove2HoleNbr(ModCebsCom.GL_CEBS_HB_TARGET_96_SD_BATCH_MAX);
        self.instMotoHandler.funcMotoMove2HoleNbr(ModCebsCom.GL_CEBS_HB_TARGET_96_SD_BATCH_MAX - ModCebsCom.GL_CEBS_HB_HOLE_X_NUM + 1);
                
    def run(self):
        while True:
            time.sleep(1)
            self.cntCtrl -= 1;
            if (self.cntCtrl > 0):
                self.sgL3CalibFormPrtLog.emit("L2CALPI: Running Calibration pilot process! roundIndex = %d" % (self.cntCtrl))
                self.funcMotoCalibPilotWorkingOnces();
            #STOP
            elif (self.cntCtrl == 0): 
                self.sgL3CalibFormPrtLog.emit("L2CALPI: Stop Calibration pilot!")
                self.instMotoHandler.funcMotoStop();


#Camera display thread, control camera video and easy calibration action
#只可能被CalibForm调用，所以father传进去后，只能被它锁调用
class clsL2_CalibCamDispThread(QThread):
    sgL3CalibFormPrtLog = pyqtSignal(str)
    sgL2CamDiStart = pyqtSignal()
    sgL2CamDiStop = pyqtSignal()

    def __init__(self, father):
        super(clsL2_CalibCamDispThread,self).__init__()
        self.identity = None;
        self.runFlag = False;
        self.cap = ''
        self.instL4CalibForm = father
        self.funcCalibCamDisLogTrace("L2CALCMDI: Instance start test!")

    def setIdentity(self,text):
        self.identity = text

    def funcCalibCamDisLogTrace(self, myString):
        self.instL4CalibForm.calib_print_log(myString)
                
    def funcCalibCameraDispStart(self):
        #SETUP 2nd task
        self.runFlag = True;

    def funcCalibCameraDispStop(self):
        self.runFlag = False;
        try:
            self.cap.release()
        except Exception:
            pass
        try:
            cv.destroyAllWindows()
        except Exception:
            pass

    def run(self):
        while True:
            time.sleep(0.1)
            if (self.runFlag == True):
                print("L2CALCMDI: Active the camera display!")
                self.cap = cv.VideoCapture(ModCebsCom.GL_CEBS_VISION_CAMBER_NBR)
                self.cap.set(3, ModCebsCom.GL_CEBS_VISION_CAMBER_RES_WITDH)
                self.cap.set(4, ModCebsCom.GL_CEBS_VISION_CAMBER_RES_HEIGHT)             
                break;
        if not self.cap.isOpened():
            self.instL1ConfigOpr.medErrorLog("L2CALCMDI: Cannot open webcam!")
            return -1;
        #Prepare to show window
        cv.namedWindow('CAMERA CAPTURED', 0)
        cv.resizeWindow('CAMERA CAPTURED', 800, 600);
        #Not yet able to embed vision into UI, so has to put at another side
        #cv.moveWindow('CAMERA CAPTURED', ModCebsCom.GL_CEBS_CAMERA_DISPLAY_POS_X, ModCebsCom.GL_CEBS_CAMERA_DISPLAY_POS_Y)
        cv.moveWindow('CAMERA CAPTURED', 0, ModCebsCom.GL_CEBS_CAMERA_DISPLAY_POS_Y)
        while True:
            time.sleep(0.001)
            try:
                ret, frame = self.cap.read()
            except Exception:
                break;
            if (self.runFlag == True) and (ret == True):
                cv.imshow('CAMERA CAPTURED', frame)
                waitKey(50)
            else:
                break;

            
            #第二种设计的方案，本来想解决第二次启动后的工作问题，但并没有真正起到作用
#             workingMode = False
#             while True:
#                 if (self.runFlag == True):
#                     self.runFlag = False
#                     workingMode = True
#                     self.cap = cv.VideoCapture(ModCebsCom.GL_CEBS_VISION_CAMBER_NBR)
#                     if not self.cap.isOpened():
#                         self.instL1ConfigOpr.medErrorLog("L3CALIB: Cannot open webcam!")
#                         print("L2CALCMDI: Cannot open webcam!")
#                         return -1;
#                     cv.namedWindow('CAMERA CAPTURED', 0)
#                     cv.resizeWindow('CAMERA CAPTURED', 640, 480);
#                     cv.moveWindow('CAMERA CAPTURED', 0, ModCebsCom.GL_CEBS_CAMERA_DISPLAY_POS_Y)
#                 else:
#                     workingMode = False
# 
#                 if (workingMode == False):
#                     time.sleep(0.1)
#                 else:
#                     try:
#                         ret, frame = self.cap.read()
#                     except Exception:
#                         time.sleep(0.1)
#                         continue
#                     print("Ret = %d", ret)
#                     if (ret == True):
#                         cv.imshow('CAMERA CAPTURED', frame)
#                         waitKey(100)
#                     else:
#                         time.sleep(0.1)
#                         continue



