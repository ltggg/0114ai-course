import torch
import torch.nn as nn
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

def train_mnist():
    """
    [拆解] 11_MNIST手写数字识别：神经网络的Hello_World
    目标：掌握图片数据的“拉直”与分批训练
    """
    # 1. 图片预处理指令集
    transform = transforms.Compose([
        transforms.ToTensor(), # 转为 Tensor 且归一化到 0-1
        transforms.Normalize((0.5,), (0.5,)) # 标准化到 -1 到 1 之间
    ])

    # 2. 下载并加载数据集 (由 torchvision 自动完成)
    train_set = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
    train_loader = DataLoader(train_set, batch_size=128, shuffle=True)

    # 3. 搭建网络：把 28x28 的平面拉成 784 的长线
    class MNISTNet(nn.Module):
        def __init__(self):
            super().__init__()
            self.flatten = nn.Flatten() # 自动帮你“拉直”
            self.net = nn.Sequential(
                nn.Linear(784, 512),
                nn.ReLU(),
                nn.Linear(512, 128),
                nn.ReLU(),
                nn.Linear(128, 10) # 最终落到 0-9 这 10 个房间
            )
        
        def forward(self, x):
            x = self.flatten(x)
            return self.net(x)

    model = MNISTNet().cuda() if torch.cuda.is_available() else MNISTNet()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    # 4. 正式训练
    print("开始训练手写数字识别模型...")
    for epoch in range(5): # 这里为了演示只跑 5 轮，实际建议更多
        for batch_x, batch_y in train_loader:
            if torch.cuda.is_available(): batch_x, batch_y = batch_x.cuda(), batch_y.cuda()
            
            pred = model(batch_x)
            loss = criterion(pred, batch_y)
            
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
        
        print(f"Epoch {epoch+1} 完成, 当前 Loss: {loss.item():.4f}")

    # 保存模型
    torch.save(model.state_dict(), 'models/MNIST_Master.pth')
    print("🚀 MNIST 模型训练完成并保存！")

if __name__ == "__main__":
    train_mnist()
