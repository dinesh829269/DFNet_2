import torch
import torch.nn as nn

class MaskedL1Loss(nn.Module):
    def __init__(self):
        super(MaskedL1Loss, self).__init__()

    def forward(self, input, target, mask=None):
        loss = torch.abs(input - target)
        if mask is not None:
            loss = loss * mask
        return loss.mean()
