# -*- coding: utf-8 -*-
import cv2
from video_reader import VideoReader
from frame_enhancer import LowLightEnhance
from face_detector import FaceDetector

video_reader = VideoReader()
low_light_enhancer = LowLightEnhance(0, 'snapshots/Epoch99.pth')
face_detector = FaceDetector(0)

video_reader.setVideoPath(r'D:\video\video2.mp4')
video_reader.setFrameSavePath(r'savedframes')

ret = True
while ret:
    ret, frame, frame_no = video_reader.getFrame()
    frame = low_light_enhancer.enhance(frame)
    face_detector.detect(frame)
    video_reader.saveFrame(frame)
    cv2.imshow('Sakurasoul', face_detector.draw_boundary_box(frame)) 
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()