# -*- coding: utf-8 -*-
import cv2
import os

class VideoReader:
    global frame_No
    global frame
    
    def __init__(self, video_path=''):
        self.video_path = video_path
        self.video_obj = cv2.VideoCapture(self.video_path)
        self.frame_No = -1
        
    
    def setVideoPath(self, video_path):
        self.video_path = video_path
        self.video_obj = cv2.VideoCapture(self.video_path)
        
    def setFrameSavePath(self, save_path):
        self.save_path = save_path
        if not os.path.isdir(self.save_path):
            os.mkdir(self.save_path)
        
    def getFrame(self):
        self.frame_No += 1
        ret, self.frame = self.video_obj.read()
        return ret, self.frame, self.frame_No

    def getVideoDimension(self):
        pass
    
    def releaseCapture(self):
        self.video_obj.release()
        
    def saveFrame(self, user_frame = None):
        if self.save_path is None:
            print('Save path is None')
            return 0
        path = self.save_path + '\FrameNo{0}.png'.format(self.frame_No)
        if user_frame is None:
            cv2.imwrite(path, self.frame)
        else:
            cv2.imwrite(path, user_frame)
        
        
        