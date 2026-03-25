import torch

def and_gate(x1, x2):
    w1 = 1.0
    w2 = 1.0
    b = -1.5
    z = x1 * w1 + x2 * w2 + b
    output = 1 if z > 0 else 0
    return output

print("--- 与门 (AND Gate) 运行结果 ---")
print(f"输入 (0, 0) -> 预测输出: {and_gate(0, 0)}")
print(f"输入 (0, 1) -> 预测输出: {and_gate(0, 1)}")
print(f"输入 (1, 0) -> 预测输出: {and_gate(1, 0)}")
print(f"输入 (1, 1) -> 预测输出: {and_gate(1, 1)}")
