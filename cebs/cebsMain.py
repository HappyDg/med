'''
Created on 2018/4/29

@author: hitpony
'''

####!/usr/bin/python3.6
#### -*- coding: UTF-8 -*-

import sys
import time
import cebsL4Ui
from PkgCetkHandler import ModCetkPrjEntry

GL_MAIN_WORK_MODE_CEBSL4UI = 1
GL_MAIN_WORK_MODE_VM_TASK = 2
GL_MAIN_CUR_WORK_MODE = GL_MAIN_WORK_MODE_VM_TASK

#SYSTEM ENTRY
if __name__ == '__main__':
    print("[CEBS] ", time.asctime(), ", System starting...\n" );
    
    if (GL_MAIN_CUR_WORK_MODE == GL_MAIN_WORK_MODE_CEBSL4UI):
        cebsL4Ui.cebs_l4ui_main_form_entry();
    else:
        ModCetkPrjEntry.prj_cebs_main_entry();
    


