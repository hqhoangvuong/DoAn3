import insightface
import numpy as np
import cv2

class FaceDetector:
    def __init__(self, gpu_id):
        self.ctx_id = gpu_id
        self.model = insightface.app.FaceAnalysis()
        self.model.prepare(ctx_id = self.ctx_id, nms = 0.4)
        
    def detect(self, frame):
        self.faces = self.model.get(frame)
        return self.faces
    
    def draw_boundary_box(self, frame, user_face = None):
        faces_data = self.faces
        if user_face is not None:
            faces_data = user_face
            
        for idx, face in enumerate(faces_data):
            b = face.bbox.astype(np.int).flatten()
            cv2.rectangle(frame, (b[0], b[1]), (b[2], b[3]), (0, 255, 0), 2)
            
        return frame
        
        
        