import torch
import torch.nn as nn


class ANNSAVILearnedOnly(nn.Module):
    def __init__(self, device, input_size, X_columns, y_column):
        super().__init__()
        self.device = device
        self.input_size = input_size
        self.X_columns = X_columns
        self.y_column = y_column
        self.L = nn.Parameter(torch.tensor(0.5))
        self.criterion_soc = torch.nn.MSELoss(reduction='mean')

        self.linear1 = nn.Sequential(
            nn.Linear(1, 30),
            nn.LeakyReLU(),
            nn.Linear(30, 1)
        )

    def forward(self, x, soc):
        savi_hat = self.savi(x)
        soc_hat = self.linear1(savi_hat)
        soc_hat = soc_hat.reshape(-1)
        loss = self.criterion_soc(soc_hat, soc)
        return soc_hat, savi_hat, loss

    def savi(self,x):
        nir_index = self.X_columns.index("vnir4")
        red_index = self.X_columns.index("red")
        nir = x[:,nir_index]
        red = x[:,red_index]
        s = (nir - red) / (nir + red + self.L) * (1 + self.L)
        return s.reshape(s.shape[0],1)
