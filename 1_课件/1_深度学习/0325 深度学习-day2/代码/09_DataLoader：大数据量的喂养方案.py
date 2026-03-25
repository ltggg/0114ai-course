import torch
from torch.utils.data import DataLoader, TensorDataset

def dataloader_demo():
    """
    [拆解] 09_DataLoader：大数据量的喂养方案
    目标：理解 batch_size 和 shuffle 的真正含义
    """
    # 模拟 100 条数据，每条有 8 个特征
    x = torch.randn(100, 8)
    y = torch.randn(100, 1)

    # 1. 封装为 Dataset
    dataset = TensorDataset(x, y)

    # 2. 核心：封装为 DataLoader
    # batch_size=16 表示每次喂给模型 16 条数据
    # shuffle=True 表示每轮训练都打乱顺序，防止模型“死记硬背”
    loader = DataLoader(dataset, batch_size=16, shuffle=True)

    print(f"数据总数: {len(dataset)}")
    print(f"每批大小: 16")
    print(f"总打印次数 (Batch 数量): {len(loader)}")

    for step, (batch_x, batch_y) in enumerate(loader):
        print(f"第 {step+1} 次喂数据, 拿到了 {batch_x.shape[0]} 条")

if __name__ == "__main__":
    dataloader_demo()
