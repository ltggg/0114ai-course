import torch
import torch.nn as nn
import cv2
import numpy as np

def model_inference():
    """
    [拆解] 12_从图片到分类：模型部署与推理
    目标：使用 OpenCV 加载自己的图片进行预测
    """
    # 1. 第一步：先建个一样的空壳模型
    class MNISTNet(nn.Module):
        def __init__(self):
            super().__init__()
            self.flatten = nn.Flatten()
            self.net = nn.Sequential(
                nn.Linear(784, 512),
                nn.ReLU(),
                nn.Linear(512, 128),
                nn.ReLU(),
                nn.Linear(128, 10)
            )
        def forward(self, x):
            x = self.flatten(x)
            return self.net(x)

    model = MNISTNet()
    # 2. 第二步：灌入训练好的“灵魂”
    try:
        model.load_state_dict(torch.load('MNIST_Master.pth', map_location='cpu'))
        model.eval()
        print("✅ 模型加载成功，准备识别图片...")
    except:
        print("❌ 找不到模型文件，请先运行 11 号脚本。")
        return

    # 3. 模拟 OpenCV 读取图片 (这里用一个全黑或全白的 28x28 数组代替)
    # 实际应用中：img = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
    img = np.zeros((28, 28), dtype=np.uint8) 
    
    # 4. 关键：图片预处理 (必须和训练时一模一样！)
    img_resized = cv2.resize(img, (28, 28))
    img_normalized = (img_resized / 255.0 - 0.5) / 0.5 # 对应训练时的 Normalize
    
    # 转换维度：[28, 28] -> [1, 1, 28, 28] (Batch, Channel, H, W)
    img_tensor = torch.FloatTensor(img_normalized).unsqueeze(0).unsqueeze(0)

    # 5. 推理
    with torch.no_grad():
        output = model(img_tensor)
        # argmax: 找出 10 个输出中概率最大的索引
        prediction = output.argmax(dim=1).item()
        
    print(f"--- 识别结果 ---")
    print(f"模型预测这张图片里的数字是: {prediction}")

if __name__ == "__main__":
    model_inference()
