import torch

# 与门
def and_gate(x1, x2):
    w1 = 1.0
    w2 = 1.0
    b = -1.5
    z = x1 * w1 + x2 * w2 + b
    output = 1 if z > 0 else 0
    return output

# 或门
def or_gate(x1, x2):
    w1 = 1.0  # 权重不变
    w2 = 1.0
    b = -0.5  # 偏置改这一个
    z = x1 * w1 + x2 * w2 + b
    output = 1 if z > 0 else 0
    return output

print("--- 与门 (AND Gate) ---")
print(f"(0,0) → {and_gate(0,0)}")
print(f"(0,1) → {and_gate(0,1)}")
print(f"(1,0) → {and_gate(1,0)}")
print(f"(1,1) → {and_gate(1,1)}")

print("\n--- 或门 (OR Gate) ---")
print(f"(0,0) → {or_gate(0,0)}")
print(f"(0,1) → {or_gate(0,1)}")
print(f"(1,0) → {or_gate(1,0)}")
print(f"(1,1) → {or_gate(1,1)}")