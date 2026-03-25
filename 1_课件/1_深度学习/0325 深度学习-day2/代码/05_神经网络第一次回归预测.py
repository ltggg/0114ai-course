import torch
import torch.nn as nn

def regression_first_try():
    """
    [拆解] 05_神经网络第一次回归预测
    目标：拟合非线性函数 y = x^2，理解 unsqueeze(1) 的重要性
    """
    # 1. 准备数据 (-1 到 1 均匀取 100 个点)
    x = torch.linspace(-1, 1, 100).unsqueeze(1) # [100] -> [100, 1] 只有变成矩阵才能喂给神经网络
    # 生成 y，并加入一点噪声 (不然太简单了)
    y = x.pow(2) + 0.2 * torch.rand(x.size())

    # 2. 搭建网络 (虽然只有 2 层，但它已经是深度学习了！)
    class SimpleNet(nn.Module):
        def __init__(self):
            super(SimpleNet, self).__init__()
            self.hidden = nn.Linear(1, 10) # 输入 1 维，隐藏层 10 个神经元
            self.predict = nn.Linear(10, 1) # 输出 1 维
            self.relu = nn.ReLU() # 激活函数，没有它就拟合不了抛物线

        def forward(self, x):
            x = self.relu(self.hidden(x))
            x = self.predict(x)
            return x

    model = SimpleNet()
    criterion = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)

    # 3. 训练初体验
    print("正在尝试拟合抛物线...")
    for epoch in range(200):
        prediction = model(x)
        loss = criterion(prediction, y)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if epoch % 50 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

if __name__ == "__main__":
    regression_first_try()
