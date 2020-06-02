import numpy as np
import cv2
import time
import os
import datetime
from multiprocessing import Process, Queue, Pipe

class Collect_face_data(Process):
    def __init__(self,queue_send,queue_recive,**kwargs):
        super(Collect_face_data, self).__init__()
        self.kwargs = kwargs
        self.FPS = 30
        self.Queue_send = queue_send
        self.Queue_recive = queue_recive
        self.capture_frame = False
        self.all_frame = 600
    def displayProgressBar(self, currentframe,percent):
        lineThickness = 10
        x = 0
        y = 450
        w = currentframe.shape[1]
        cv2.line(currentframe, (x, y), (w, y), (255,255,255), lineThickness)
        cv2.line(currentframe, (x, y), (int(percent*w/self.all_frame), y), (255,0,0), lineThickness)
        return currentframe

    def run(self):
        #cap = cv2.VideoCapture('rtsp://admin:AI_team123@192.168.1.64:554/Streaming/Channels/101/')
        cap = cv2.VideoCapture(0)
        frame_id = 0
        while(True):
            self.Comunicate_master()
            if cap.isOpened():
                ret, frame = cap.read()
                if ret == True:
                    h,w = frame.shape[0],frame.shape[1]
                    if self.capture_frame:
                        if frame_id % 5==0:
                            name_image_save = self.save_dir + "/" +str(int(frame_id/5))+'.jpg'
                            cv2.imwrite(name_image_save,frame)
                        frame_id+=1
                        if frame_id==self.all_frame:
                            frame_id=0
                            self.capture_frame = False
                            self.Queue_recive.put('DONE!!!')
                        cv2.putText(frame,'CAPTURE',(20,40),cv2.FONT_HERSHEY_COMPLEX,1,(0,0, 255),2)
                        self.displayProgressBar(frame,frame_id)
                    center_coordinates = (int(w/2),int(h/2)) 
                    radius = 180
                    color = (255, 0, 0) 
                    thickness = 2
                    cv2.circle(frame, center_coordinates, radius, color, thickness) 
                        
                    cv2.imshow('CAPTURE',frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
            else:
                print('CAN NOT CAPTURE FRAME')
                break
        # # Release everything if job is finished
        cap.release()
        cv2.destroyAllWindows()
    def Comunicate_master(self):
        if not self.Queue_send.empty():
            self.capture_frame = True
            self.save_dir = self.Queue_send.get()

if __name__ == "__main__":
    queue_send= Queue()
    queue_recive = Queue()
    Start_caputure = Collect_face_data(queue_send,queue_recive)
    Start_caputure.start()
    while True:
        print('================== PLEASE TYPE YOUR NAME =================')
        PERSON_NAME = (input("Your name : "))
        print('================== PLEASE TYPE YOUR SEX  =================')
        PERSON_SEX = (input("Your sex : "))
        print('================== PLEASE TYPE YOUR AGE  =================')
        PERSON_AGE = (input("Your age : "))
        DIR_DATA_SAVE = '/hdd/FACE_DATA'
        FOLDER_NAME = PERSON_NAME+'_'+PERSON_SEX+'_'+PERSON_AGE
        save_dir = os.path.join(DIR_DATA_SAVE,FOLDER_NAME)  
        if not os.path.isdir(save_dir):
            os.mkdir(save_dir)        # Create target Directory
            print("Directory " , save_dir ,  " Created ")
        else:
            print("Directory " , save_dir ,  " already exists")
        input('============ PRESS ENTER TO START CAPTURE ===============')
        queue_send.put(save_dir)
        while True:
            if not queue_recive.empty():
                print(queue_recive.get())
                break