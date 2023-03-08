import torch
import torch.nn as nn

class Encoder(nn.Module):
    """The base class for all encoder, which maps low-dimentional input into high-dimentional feature."""

    def __init__(self, config: dict) -> None:
        super().__init__()

        self.in_dim = None
        self.out_dim = None

    def forward(self, tensor_in: torch.Tensor) -> torch.Tensor:
        """Encode the low dimentional input into high dimentional feature.
        Args:
            tensor_in (torch.Tensor): [N, self.in_dim], low dimentional input.
        Returns:
            (torch.Tensor): [N, self.out_dim], high dimentional feature.
        """
        raise NotImplementedError()
