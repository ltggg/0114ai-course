import torch

data = [[1, 2], [3, 4]]
x = torch.tensor(data)
x_rand = torch.randn(2, 3)

print(f"张量的形状: {x_rand.shape}")
print(f"张量的数据类型: {x_rand.dtype}")
print(f"张量所在的设备: {x_rand.device}")

if torch.cuda.is_available():
    device = torch.device("cuda")
    x_gpu = x_rand.to(device)
    print(f"现在张量在: {x_gpu.device}")
else:
    print("当前环境没有 GPU，继续用 CPU。")

x_flat = x_rand.view(1, 6)
print(f"变形后的形状: {x_flat.shape}")

a = torch.ones(2, 2)
b = torch.ones(2, 2)
result = a + b
print("张量加法结果:\n", result)
