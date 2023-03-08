from typing import Union

import torch.nn as nn

from utils.str_utils import string_case_insensitive

def make_loss_function(config: dict) -> Union[nn.SmoothL1Loss, nn.MSELoss]:
    """Return a loss function with a given configuration."""

    name = config["name"]

    if string_case_insensitive(name, "L1"):
        return nn.SmoothL1Loss()
    elif string_case_insensitive(name, "L2"):
        return nn.MSELoss()
    else:
        raise KeyError("Wrong loss function name: got `{}`.".format(name))
