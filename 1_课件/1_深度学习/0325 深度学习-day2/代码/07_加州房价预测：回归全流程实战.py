import torch
import torch.nn as nn
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

def industrial_regression():
    """
    [拆解] 07_加州房价预测：回归全流程实战
    目标：标准化 -> 训练 -> 保存，理解工业级全生命周期
    """
    # 1. 加载数据
    data = fetch_california_housing()
    X, y = data.data, data.target.reshape(-1, 1)
    
    # 2. 特征缩放 (这是工业成功的关键，不缩放会导致梯度爆炸)
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    
    # 保存缩放器 (部署时要用，不然输入数据对不上)
    joblib.dump(scaler, 'California_Scaler.pkl')
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    # 转换 Tensor (记得 float 类型)
    X_train = torch.FloatTensor(X_train)
    y_train = torch.FloatTensor(y_train)

    # 3. 搭建深度网络
    model = nn.Sequential(
        nn.Linear(8, 64),
        nn.ReLU(),
        nn.Linear(64, 32),
        nn.ReLU(),
        nn.Linear(32, 1)
    )

    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
    criterion = nn.MSELoss()

    # 4. 训练
    for epoch in range(500):
        pred = model(X_train)
        loss = criterion(pred, y_train)
        
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if epoch % 50 == 0:
            print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

    # 5. 保存灵魂 (权重)
    torch.save(model.state_dict(), 'models/Housing_Master.pth')
    print("🚀 工业级模型已训练成功并保存至 Housing_Master.pth")

if __name__ == "__main__":
    industrial_regression()
