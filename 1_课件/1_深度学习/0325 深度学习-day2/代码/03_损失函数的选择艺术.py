import torch
import torch.nn as nn

def loss_gallery():
    """
    [拆解] 03_损失函数的选择艺术
    目标：知道什么任务该选什么“标尺”
    """
    print("--- 深度学习损失函数展厅 ---")
    
    predict = torch.randn(3, 5) # 模拟预测值：3个样本，每个样本预测5类
    label_reg = torch.randn(3, 5) # 模拟回归标签
    label_cls = torch.tensor([1, 0, 4]) # 模拟分类标签 (属于第1, 0, 4类)

    # 1. 回归标配：MSE (均方误差)
    mse = nn.MSELoss()
    loss_mse = mse(predict, label_reg)
    print(f"MSE 损失 (回归): {loss_mse.item():.4f}")

    # 2. 多分类标配：CrossEntropy (交叉熵)
    # 它会自动帮你做 Softmax
    ce = nn.CrossEntropyLoss()
    loss_ce = ce(predict, label_cls)
    print(f"CrossEntropy 损失 (多分类): {loss_ce.item():.4f}")

    # 3. 稳健回归：SmoothL1 (Huber)
    # 它是 MSE 和 L1 的结合体，对异常值不敏感
    huber = nn.SmoothL1Loss()
    loss_huber = huber(predict, label_reg)
    print(f"SmoothL1 损失 (稳健回归): {loss_huber.item():.4f}")

if __name__ == "__main__":
    loss_gallery()
