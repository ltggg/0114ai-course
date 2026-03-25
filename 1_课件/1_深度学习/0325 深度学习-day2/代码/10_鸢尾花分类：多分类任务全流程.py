import torch
import torch.nn as nn
from sklearn.datasets import load_iris

def iris_classification():
    """
    [拆解] 10_鸢尾花分类：多分类任务全流程
    目标：理解 CrossEntropyLoss 与 3 分类的映射
    """
    # 1. 准备数据
    x, y = load_iris(return_X_y=True)
    x = torch.FloatTensor(x)
    y = torch.LongTensor(y) # 分类标签必须是整数 Long 类型

    # 2. 搭建 3 分类工厂
    model = nn.Sequential(
        nn.Linear(4, 16),
        nn.ReLU(),
        nn.Linear(16, 3) # 输出 3 个维度，对应 3 种花
    )

    # 3. 裁判与向导
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    # 4. 训练
    for epoch in range(100):
        pred = model(x)
        loss = criterion(pred, y)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if epoch % 20 == 0:
            print(f"Epoch {epoch}, 识别误差 (Loss): {loss.item():.4f}")

    print("✅ 鸢尾花分类模型训练完成！")

if __name__ == "__main__":
    iris_classification()
