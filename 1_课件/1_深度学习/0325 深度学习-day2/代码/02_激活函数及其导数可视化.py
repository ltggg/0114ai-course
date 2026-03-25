import torch
import torch.nn as nn
import matplotlib.pyplot as plt

def activation_lab():
    """
    [拆解] 02_激活函数及其导数可视化
    对比别人代码 02：不仅看形状，更要看“导数”是如何流动的
    """
    # 1. 准备数据，开启 requires_grad 观察梯度
    x = torch.linspace(-8, 8, 200, requires_grad=True)
    
    # 选择常用的激活函数
    activations = {
        "Sigmoid": nn.Sigmoid(),
        "Tanh": nn.Tanh(),
        "ReLU": nn.ReLU(),
        "LeakyReLU": nn.LeakyReLU(0.1)
    }

    plt.figure(figsize=(15, 10))
    
    for i, (name, act) in enumerate(activations.items(), 1):
        # 前向传播
        y = act(x)
        
        # 反向传播求导 (这是精髓)
        # 我们给 y 一个 1.0 的梯度，让它往回传给 x
        y.backward(torch.ones_like(x), retain_graph=True)
        grad_x = x.grad.clone() # 获取 x 方向的梯度（斜率）
        x.grad.zero_() # 清空，防止下次叠加
        
        # 绘图
        plt.subplot(2, 2, i)
        plt.plot(x.detach().numpy(), y.detach().numpy(), label=f'{name} 曲线', color='blue', linewidth=2)
        plt.plot(x.detach().numpy(), grad_x.numpy(), label=f'{name} 导数(梯度)', color='orange', linestyle='--')
        plt.title(f"{name} 激活函数实验室")
        plt.legend()
        plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    activation_lab()
