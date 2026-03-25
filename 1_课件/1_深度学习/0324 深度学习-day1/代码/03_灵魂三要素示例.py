import torch
import torch.nn as nn
import torch.optim as optim
# 第一部分 流水线
model = nn.Sequential(
    nn.Linear(5, 10),
    nn.ReLU(),
    nn.Linear(10, 2)
)
# 第二部分 算出损失
# 质检员
criterion = nn.MSELoss()

# 第三部分 学习率 ，Adam优化
# 厂长
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 第四部分
# 1 抓材料
inputs = torch.randn(1, 5)
# 2 准备标准答案
labels = torch.randn(1, 2)

# 这个是重点  五步骤
# 1.清空
optimizer.zero_grad()
# 2.前向出货
outputs = model(inputs)
# 3.误差
loss = criterion(outputs, labels)
print(f"当前 Loss 值: {loss.item()}")
# 4.方向盘 反向传播
loss.backward()
# 5.旋转调整
optimizer.step()
