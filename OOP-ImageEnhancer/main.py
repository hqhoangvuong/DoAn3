# -*- coding: utf-8 -*-
import cv2
from video_reader import VideoReader

video_reader = VideoReader()

video_reader.setVideoPath(r'D:\video\video2.mp4')
video_reader.setFrameSavePath(r'savedframes')

ret = True
while ret:
    ret, frame, frame_no = video_reader.getFrame()
    video_reader.saveFrame()
    cv2.imshow('Sakurasoul', frame) 
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()