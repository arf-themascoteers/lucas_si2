import torch
import torch.nn as nn
import torch.nn.functional as F


class ANNSAVI(nn.Module):
    def __init__(self, device, input_size, X_columns, y_column):
        super().__init__()
        self.device = device
        self.input_size = input_size
        self.X_columns = X_columns
        self.y_column = y_column

        self.L = nn.Parameter(torch.tensor(0.5))

        self.alpha = 10

        self.criterion_soc = torch.nn.MSELoss(reduction='mean')

        self.linear1 = nn.Sequential(
            nn.Linear(input_size+1, 30),
            nn.LeakyReLU(),
            nn.Linear(30, 1)
        )

    def forward(self, x, soc):
        savi = self.savi(x)
        x = torch.cat((x, savi), dim=1)
        x = self.linear1(x)
        soc_hat = x.reshape(-1)

        loss_soc = self.criterion_soc(soc_hat, soc)
        loss = loss_soc
        print(round(loss_soc.item(), 3))

        return soc_hat, savi, loss

    def savi(self,x):
        nir_index = self.X_columns.index("vnir4")
        red_index = self.X_columns.index("red")
        nir = x[:,nir_index]
        red = x[:,red_index]
        s = (nir - red) / (nir + red + self.L) * (1 + self.L)
        return s.reshape(s.shape[0],1)
