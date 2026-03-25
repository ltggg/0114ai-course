import torch
import torch.nn as nn

def persistence_demo():
    """
    [拆解] 08_模型的保存与加载
    目标：学会如何让模型“起死回生”
    """
    # 1. 结构必须一样
    structure = nn.Sequential(
        nn.Linear(8, 64),
        nn.ReLU(),
        nn.Linear(64, 32),
        nn.ReLU(),
        nn.Linear(32, 1)
    )
    
    # 2. 加载权重
    try:
        # map_location='cpu' 保证即使是 GPU 训练的模型在 CPU 上也能跑
        state_dict = torch.load('Housing_Master.pth', map_location='cpu')
        structure.load_state_dict(state_dict)
        structure.eval() # 切换至评估模式，关闭梯度计算
        print("✅ 成功从硬盘复活模型！")
        
        # 3. 模拟一次推理
        dummy_input = torch.randn(1, 8)
        prediction = structure(dummy_input)
        print(f"输入一条模拟数据，预测房价为: {prediction.item():.4f}")
        
    except FileNotFoundError:
        print("❌ 错误：请先运行 07 号脚本生成模型文件。")

if __name__ == "__main__":
    persistence_demo()
