import torch
import torch.nn as nn

layer1 = nn.Linear(in_features=5, out_features=7, bias=True)
layer2 = nn.Linear(in_features=7, out_features=10, bias=True)
output_layer = nn.Linear(in_features=10, out_features=2, bias=True)

print("--- 神经网络结构展示 ---")
print("第一层:", layer1)
print("第二层:", layer2)
print("输出层:", output_layer)

print("\n--- 权重参数详情 ---")
print("第一层权重形状:", layer1.weight.shape)
print("第一层偏置形状:", layer1.bias.shape)
