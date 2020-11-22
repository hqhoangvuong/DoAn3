import torch
import torch.optim
import os
import model
import numpy as np
from PIL import Image

class LowLightEnhance():
    def __init__(self, gpu_id = -1, model_path = ''):
        self.gpu_id  = gpu_id
        self.model_path = model_path
        
    def torch_tensor_to_image(self, tensor):
        img = tensor.cpu().data.numpy()[0]
        img = np.transpose(img, (1, 2, 0)) * 255
        return img
        
    def enhance(self, frame):
        os.environ['CUDA_VISIBLE_DEVICES'] = str(self.gpu_id)
        data_lowlight = Image.fromarray(frame)
        data_lowlight = (np.asarray(data_lowlight) / 255.0)
        data_lowlight = torch.from_numpy(data_lowlight).float()
        data_lowlight = data_lowlight.permute(2, 0, 1)    
        data_lowlight = data_lowlight.cuda().unsqueeze(0)
        
        if self.model_path == '':
            print('error when load model!')
            return 0
        DCE_net = model.enhance_net_nopool().cuda()
        DCE_net.load_state_dict(torch.load(self.model_path))
        
        _,enhanced_image,_ = DCE_net(data_lowlight)    
        return self.torch_tensor_to_image(enhanced_image)

    
    