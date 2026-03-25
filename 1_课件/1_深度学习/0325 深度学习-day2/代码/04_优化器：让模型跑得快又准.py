import torch
import torch.nn as nn
import torch.optim as optim

def optimizer_workshop():
    """
    [拆解] 04_优化器：让模型跑得快又准
    目标：理解 Adam、SGD 的工业配置
    """
    print("--- 深度学习优化器车间 ---")
    
    # 模拟一个两层模型
    model = nn.Sequential(
        nn.Linear(10, 50),
        nn.ReLU(),
        nn.Linear(50, 1)
    )

    # 1. SGD: 建议加上动量 (momentum=0.9) 否则太慢
    sgd = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)
    
    # 2. AdamW: 现代工业界首选，weight_decay 负责正则化，防止过拟合
    adamw = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)

    print(f"推荐向导：AdamW \n配置参数：{adamw.defaults}")
    
    # 核心步骤展示
    sgd.zero_grad() # 必做：梯度清零，不要捡别人剩的
    # ... 计算 loss ...
    # loss.backward() # 必做：反向传播
    # sgd.step() # 必做：迈出步子更新 W 和 b

if __name__ == "__main__":
    optimizer_workshop()
