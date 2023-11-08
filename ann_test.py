from ann_simple import ANNSimple
from ds_manager import DSManager
from spectral_dataset import SpectralDataset
import torch
import spec_utils
from torch.utils.data import DataLoader
from sklearn.metrics import r2_score


def train(ds, X_columns, y_column):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    batch_size = 1000
    dataloader = DataLoader(ds, batch_size=batch_size)
    model = ANNSimple(device, ds.x.shape[1], X_columns, y_column)
    model.train()
    model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01, weight_decay=0.001)
    criterion = torch.nn.MSELoss(reduction='sum')
    n_batches = int(len(ds)/batch_size) + 1
    batch_number = 0
    loss = None
    num_epochs = 3000
    for epoch in range(num_epochs):
        batch_number = 0
        for (x, y) in dataloader:
            x = x.to(device)
            y = y.to(device)
            y_hat = model(x)
            y_hat = y_hat.reshape(-1)
            loss = criterion(y_hat, y)
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            batch_number += 1
            print(f'Epoch:{epoch + 1} (of {num_epochs}), Batch: {batch_number} of {n_batches}, Loss:{loss.item():.6f}')

    torch.save(model, "ann.pt")
    return model


def test(model=None, ds=None):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    if model is None:
        model = torch.load("ann.pt")
    batch_size = 30000
    dataloader = DataLoader(ds, batch_size=batch_size, shuffle=True)
    model.eval()
    model.to(device)

    for (x, y) in dataloader:
        x = x.to(device)
        y = y.to(device)
        y_hat = model(x)
        y_hat = y_hat.reshape(-1)
        y = y.detach().cpu().numpy()
        y_hat = y_hat.detach().cpu().numpy()
        r2 = r2_score(y, y_hat)
        return r2


ds = DSManager(folds=0, X_columns=spec_utils.get_rgb())
train_data, test_data = ds.get_train_test()
train_sds = SpectralDataset(*DSManager.split_X_y_array(train_data))
test_sds = SpectralDataset(*DSManager.split_X_y_array(test_data))
model = train(train_sds, ds.X_columns, ds.y_column)
r2 = test(model, test_sds)
print(r2)