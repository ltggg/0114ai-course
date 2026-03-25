import torch
import torch.nn as nn

def layer_demo():
    """
    [拆解] 01_全连接层的奥秘
    目标：理解 in_features/out_features 及其对维度的改变
    """
    print("--- 走进全连接层 nn.Linear ---")
    
    # 模拟输入：假设有 10 个人，每个人有 5 个特征 (面积, 楼层, 房龄, 车站距离, 绿化率)
    # 形状：[10, 5] (BatchSize, Features)
    input_data = torch.randn(10, 5)
    
    # 定义一层全连接：输入 5 维，输出 7 维
    # 这相当于这 5 个特征经过 7 组不同的“公式”转换，变成了 7 个新特征
    layer1 = nn.Linear(in_features=5, out_features=7, bias=True)
    
    output = layer1(input_data)
    
    print(f"输入形状: {input_data.shape}")
    print(f"输出形状: {output.shape} (成功的将 5 个特征转化为了 7 个特征)")
    print(f"权重矩阵权重形状 (W): {layer1.weight.shape} (正好是 7x5)")
    print(f"偏置量形状 (b): {layer1.bias.shape} (对应 7 个神经元)")

if __name__ == "__main__":
    layer_demo()
