import torch.nn as nn


class ANNSimple(nn.Module):
    def __init__(self, device, input_size, X_columns, y_column):
        super().__init__()
        self.device = device
        self.input_size = input_size
        self.X_columns = X_columns
        self.y_column = y_column

        self.linear1 = nn.Sequential(
            nn.Linear(input_size, 3),
            nn.LeakyReLU(),
            nn.Linear(3, 1)
        )

    def forward(self, x):
        x = self.linear1(x)
        return x.reshape(-1)
