# -*- coding: utf-8 -*-
import cv2
from video_reader import VideoReader
from frame_enhancer import LowLightEnhance

video_reader = VideoReader()
low_light_enhancer = LowLightEnhance(0, 'snapshots/Epoch99.pth')

video_reader.setVideoPath(r'D:\video\video2.mp4')
video_reader.setFrameSavePath(r'savedframes')

ret = True
while ret:
    ret, frame, frame_no = video_reader.getFrame()
    frame = low_light_enhancer.enhance()
    video_reader.saveFrame(frame)
    cv2.imshow('Sakurasoul', frame) 
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()