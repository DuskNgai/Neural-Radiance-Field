import torch

from model.encoders.encoder import Encoder
from utils.sh_utils import generate_sh_funcs

class SphericalHarmonicEncoder(Encoder):
    """
    Using a set of spherical harmonics as encoding functions. 
    """

    def __init__(self, config: dict) -> None:
        super().__init__(config)

        self.in_dim = config["in_dim"]
        assert self.in_dim == 3, "spherical harmonics only support to encode 3-D vectors."
        self.n_degrees = config["n_degrees"]
        self.out_dim = self.n_degrees ** 2

        self.enc_funcs = generate_sh_funcs(self.n_degrees)

    def forward(self, tensor_in: torch.Tensor) -> torch.Tensor:
        # x, y, z.size() = [N, 1]
        x, y, z = torch.split(tensor_in, 1, dim=-1)
        tensor_out = torch.cat(self.enc_funcs(x, y, z), dim=-1)
        return tensor_out
