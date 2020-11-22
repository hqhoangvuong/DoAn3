import insightface

class FaceDetector:
    def __init__(self, gpu_id):
        self.ctx_id = gpu_id
        self.model = insightface.app.FaceAnalysis()
        self.model.prepare(ctx_id = self.ctx_id, nms = 0.4)
        
    def detect(self, frame):
        faces = self.model.get(frame)
        return faces
        
        
        