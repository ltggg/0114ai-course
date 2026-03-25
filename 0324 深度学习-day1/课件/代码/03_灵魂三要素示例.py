import torch
import torch.nn as nn
import torch.optim as optim

model = nn.Sequential(
    nn.Linear(5, 10),
    nn.ReLU(),
    nn.Linear(10, 2)
)

criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

inputs = torch.randn(1, 5)
labels = torch.randn(1, 2)

optimizer.zero_grad()
outputs = model(inputs)
loss = criterion(outputs, labels)
print(f"当前 Loss 值: {loss.item()}")
loss.backward()
optimizer.step()
