# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 10:03:55 2018

@author: Administrator
"""

import os
import time
def number_people(path):
    while True:
        path_ = path
        count = 0
        for fn in os.listdir(path_): #fn 表示的是文件名
                count = count+1
        #return count
        print(count)
        time.sleep(10)
        
if __name__ == '__main__':
    number_people(path = 'E:\\shengtuo_face_recognition\\face_pictures_')