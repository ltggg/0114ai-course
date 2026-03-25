import torch
import torch.nn as nn
import matplotlib.pyplot as plt

def dynamic_plot():
    """
    [拆解] 06_训练过程的动态可视化
    目标：使用 plt.ion() 实时观看红线如何变“弯”
    """
    x = torch.linspace(-1, 1, 100).unsqueeze(1)
    y = x.pow(2) + 0.1 * torch.randn(x.size())

    model = nn.Sequential(
        nn.Linear(1, 20),
        nn.ReLU(),
        nn.Linear(20, 1)
    )
    
    optimizer = torch.optim.Adam(model.parameters(), lr=0.05)
    loss_func = nn.MSELoss()

    plt.ion() # 开启交互模式，这是画动画的关键

    for i in range(100):
        prediction = model(x)
        loss = loss_func(prediction, y)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        # 每隔 5 步刷新一次图像
        if i % 5 == 0:
            plt.cla() # 清空画布
            plt.scatter(x.numpy(), y.numpy(), color='blue', label='原始数据(点)')
            plt.plot(x.numpy(), prediction.detach().numpy(), color='red', lw=3, label='模型预测(线)')
            plt.text(0.5, 0, f'Loss={loss.item():.4f}', fontdict={'size': 15, 'color': 'red'})
            plt.legend()
            plt.pause(0.1) # 暂停一下，不然人眼看不清

    print("✅ 可视化训练完成！")
    plt.ioff() # 关闭交互模式
    plt.show()

if __name__ == "__main__":
    dynamic_plot()
