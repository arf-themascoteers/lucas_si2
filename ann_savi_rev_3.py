import torch
import torch.nn as nn


class ANNSAVIRev3(nn.Module):
    def __init__(self, device, input_size, X_columns, y_column):
        super().__init__()
        self.device = device
        self.input_size = input_size
        self.X_columns = X_columns
        self.y_column = y_column

        self.L = nn.Parameter(torch.tensor(0.5))

        self.input_to_soc = nn.Sequential(
            nn.Linear(input_size-1, 30),
            nn.LeakyReLU(),
            nn.Linear(30, 1)
        )

        self.inputsoc_to_savi = nn.Sequential(
            nn.Linear(1, 10),
            nn.LeakyReLU(),
            nn.Linear(10, 1)
        )

        self.alpha = 0.3
        self.criterion_soc = torch.nn.MSELoss(reduction='sum')
        self.criterion_savi = torch.nn.MSELoss(reduction='sum')

    def forward(self, x, soc):
        #savi_index = self.X_columns.index("savi")
        base_x = x[:,0:-1]
        savi_x = x[:,-1]

        soc_hat = self.input_to_soc(base_x)
        savi_hat = self.inputsoc_to_savi(soc_hat)

        soc_hat = soc_hat.reshape(-1)
        savi_hat = savi_hat.reshape(-1)

        loss_soc = self.criterion_soc(soc_hat, soc)
        loss_savi = self.criterion_savi(savi_hat, savi_x)
        loss = loss_soc * (1-self.alpha) + loss_savi * self.alpha

        return soc_hat, savi_hat, loss

    def savi(self,x):
        nir_index = self.X_columns.index("vnir4")
        red_index = self.X_columns.index("red")
        nir = x[:,nir_index]
        red = x[:,red_index]
        s = (nir - red) / (nir + red + self.L) * (1 + self.L)
        return s.reshape(s.shape[0],1)
