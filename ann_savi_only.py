import torch
import torch.nn as nn


class ANNSAVIOnly(nn.Module):
    def __init__(self, device, input_size, X_columns, y_column):
        super().__init__()
        self.device = device
        self.input_size = input_size
        self.X_columns = X_columns
        self.y_column = y_column
        self.criterion_soc = torch.nn.MSELoss(reduction='mean')
        self.linear1 = nn.Sequential(
            nn.Linear(1, 10),
            nn.LeakyReLU(),
            nn.Linear(10, 1)
        )

    def forward(self, x, soc):
        savi = x.reshape(-1)
        soc_hat = self.linear1(x)
        soc_hat = soc_hat.reshape(-1)
        loss = self.criterion_soc(soc_hat, soc)
        return soc_hat, savi, loss
