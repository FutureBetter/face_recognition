# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 23:06:42 2018

@author: win7
"""

import cv2
import time

def getTrainingData(window_name, camera_id, path_name, max_num): # path_name是图片存储目录，max_num是需要捕捉的图片数量
    #cv2.resizeWindow(window_name, 1000, 1000)
    cv2.namedWindow(window_name) # 创建窗口
    cap = cv2.VideoCapture(camera_id) # 打开摄像头
    classifier = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml') # 加载分类器

    color = (0,255,0) # 人脸矩形框的颜色
    num = 0 # 记录存储的图片数量

    while cap.isOpened():
        ok, frame = cap.read()
        print(frame)
        if not ok:
            break
        time.sleep(1)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # 灰度化
        faceRects=classifier.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=3,minSize=(32,32))

        if len(faceRects) > 0:
            for faceRect in faceRects:
                x,y,w,h = faceRect
                # 捕捉到的图片的名字，这里用到了格式化字符串的输出
                image_name = ('E:\\shengtuo_face_recognition\\face_pictures_2\\%s%07d.jpg' % (path_name, num))
                image = frame[y:y+h, x:x+w] # 将当前帧含人脸部分保存为图片，注意这里存的还是彩色图片，前面检测时灰度化是为了降低计算量；这里访问的是从y位开始到y+h-1位
                #image = frame[y:y, x:x]
                #time.sleep(2)
                cv2.imwrite(image_name, image)
                num += 1
                # 超过指定最大保存数量则退出循环
                #if num > max_num:
                #    break
                #print(x,y,w,h)
                cv2.rectangle(frame, (x,y), (x+w,y+h), color, 2) # 画出矩形框
                font = cv2.FONT_HERSHEY_SIMPLEX # 获取内置字体
                cv2.putText(frame, ('%d'%num), (x+30, y+30), font, 1, (255,0,255), 4) # 调用函数，对人脸坐标位置，添加一个(x+30,y+30）的矩形框用于显示当前捕捉到了多少人脸图片
        if num > max_num:
            break
        #cv2.imshow(window_name, frame)
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break

    cap.release()#释放摄像头并销毁所有窗口
    cv2.destroyAllWindows()
    print('Finished.')
    

if __name__ == '__main__':
    # print ('catching your face and writting into disk...')
    getTrainingData('capture_video',0,'face_data',1000000)