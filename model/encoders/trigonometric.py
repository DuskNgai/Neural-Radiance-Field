import torch

from model.encoders.encoder import Encoder 

class TrigonometricEncoder(Encoder):
    """
    Also called positional encoder. Using a series of `sin` and `cos` functions as encoding functions.
    sin(2 ** 0 * pi * x), cos(2 ** 0 * pi * x), sin(2 ** 1 * pi * x), cos(2 ** 1 * pi * x) ...
    sin(2 ** 0 * pi * y), cos(2 ** 0 * pi * y), sin(2 ** 1 * pi * y), cos(2 ** 1 * pi * y) ...
    sin(2 ** 0 * pi * z), cos(2 ** 0 * pi * z), sin(2 ** 1 * pi * z), cos(2 ** 1 * pi * z) ...
    """

    def __init__(self, config: dict) -> None:
        super().__init__(config)

        self.in_dim = config["in_dim"]
        self.n_frequencies = config["n_frequencies"]
        assert self.n_frequencies > 0, "n_frequencies should be a positive integer."
        self.out_dim = self.in_dim * self.n_frequencies * 2

        # frequencies.size() = [self.n_frequencies]
        if config["log_sampling"]:
            # equidistant in logarithm space
            frequencies = torch.logspace(0.0, float(self.n_frequencies - 1), self.n_frequencies, 2.0)
        else:
            # equidistant in linear space
            frequencies = torch.linspace(0.0, 2.0 ** float(self.n_frequencies - 1), self.n_frequencies)
        self.frequencies = frequencies * torch.pi

        self.enc_funcs = []
        for freq in self.frequencies:
            for func in [torch.sin, torch.cos]:
                self.enc_funcs.append(lambda x, freq=freq, func=func: func(x * freq))

    def forward(self, tensor_in: torch.Tensor) -> torch.Tensor:
        tensor_out = torch.cat([func(tensor_in) for func in self.enc_funcs], dim=-1)
        return tensor_out
