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


#Global parameter set for PICTURE
GL_CEBS_PIC_PROC_BATCH_INDEX = 0;
GL_CEBS_PIC_PROC_CLAS_INDEX = 0;  #WHICH CATEGORY IS TO BE IDENTIFY
GL_CEBS_PIC_PROC_REMAIN_CNT = 0;
GL_CEBS_PIC_CLAS_FLAG = False;  #True means it is able to start picture identification
GL_CEBS_CFG_FILE_NAME = r"cebsConfig.ini";
GL_CEBS_PIC_ORIGIN_PATH = r"pic_origin";
GL_CEBS_PIC_MIDDLE_PATH = r"pic_middle";
GL_CEBS_PIC_ABS_ORIGIN_PATH = "";
GL_CEBS_PIC_ABS_MIDDLE_PATH = "";
#Fix point to take picture or not? Formally auto-working shall set as False.
GL_CEBS_PIC_TAKING_FIX_POINT_SET = False; 
#After taking picture, whether the pic identification will be run automatically
GL_CEBS_PIC_CLASSIFIED_AFTER_TAKE_SET = True;
#Whether taking picture will be happened automatically after starting.
GL_CEBS_PIC_AUTO_WORKING_AFTER_START_SET = True;
#Auto taking picture TTI times in minutes
GL_CEBS_PIC_AUTO_WORKING_TTI_IN_MIN = 60;

#ROUNDS of auto-pilot run
GL_CEBS_PILOT_WOKING_ROUNDS_MAX = 5;
#To enable debug UI under MOTOAPI not yet installed. Formally it sets as True.
GL_CEBS_MOTOAPI_INSTALLED_SET = True; 


#MEACHNICAL HARDWARE PLATFORM SCOPE DEFINATION
GL_CEBS_HB_MECHNICAL_PLATFORM_X_MAX = 200000;
GL_CEBS_HB_MECHNICAL_PLATFORM_Y_MAX = 180000;
#CONTROL AXIS DIRECTION
GL_CEBS_HB_TARGET_BOARD_X_MAX = 120000;
GL_CEBS_HB_TARGET_BOARD_Y_MAX = 90000;
GL_CEBS_HB_TARGET_BOARD_BATCH_MAX = 96;
GL_CEBS_HB_TARGET_96_STANDARD = "96_STANDARD";
GL_CEBS_HB_TARGET_96_SD_X_MAX = 120000;
GL_CEBS_HB_TARGET_96_SD_Y_MAX = 90000;
GL_CEBS_HB_TARGET_96_SD_BATCH_MAX = 96;
GL_CEBS_HB_TARGET_48_STANDARD = "48_STANDARD";
GL_CEBS_HB_TARGET_48_SD_X_MAX = 120000;
GL_CEBS_HB_TARGET_48_SD_Y_MAX = 90000;
GL_CEBS_HB_TARGET_48_SD_BATCH_MAX = 48;
GL_CEBS_HB_TARGET_32_STANDARD = "32_STANDARD";
GL_CEBS_HB_TARGET_32_SD_X_MAX = 120000;
GL_CEBS_HB_TARGET_32_SD_Y_MAX = 90000;
GL_CEBS_HB_TARGET_32_SD_BATCH_MAX = 32;
GL_CEBS_HB_TARGET_12_STANDARD = "12_STANDARD";
GL_CEBS_HB_TARGET_12_SD_X_MAX = 120000;
GL_CEBS_HB_TARGET_12_SD_Y_MAX = 90000;
GL_CEBS_HB_TARGET_12_SD_BATCH_MAX = 12;
#ACTION SELCTION
GL_CEBS_HB_TARGET_TYPE = GL_CEBS_HB_TARGET_96_STANDARD;
GL_CEBS_PIC_ONE_WHOLE_BATCH = GL_CEBS_HB_TARGET_96_SD_BATCH_MAX;
GL_CEBS_HB_HOLE_X_NUM = 0;          #HOW MANY BOARD HOLES， X DIRECTION
GL_CEBS_HB_HOLE_Y_NUM = 0;          #HOW MANY BOARD HOLES，Y DIRECTION
GL_CEBS_HB_WIDTH_X_SCALE = 0;       #HOW MANY BOARD HOLES， X DIRECTION
GL_CEBS_HB_HEIGHT_Y_SCALE = 0;      #HOW MANY BOARD HOLES，Y DIRECTION
GL_CEBS_HB_POS_IN_UM = [0, 0, 0, 0];  #USING INT, um, 96 HOLES, POSITION OF = X1/Y1, X2/Y2
GL_CEBS_CUR_POS_IN_UM = [0, 0];  #USING INT, um, POSITION X/Y AXIS

#SERIAL COM NUMBER => THIS NEED SET IN THE BEGINNING, CAN NOT WAIT UNTIL SYSTEM START!
#SO WHOLE DESIGN LOGIC OF MOTO-API SHOULD RE-DONE!
#NOT YET USE FOLLOWING PORT SETTING.
GL_CEBS_COM_NUMBER_SET = 11;


