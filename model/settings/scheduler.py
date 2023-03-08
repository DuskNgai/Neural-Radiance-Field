import math

from torch.optim import Optimizer
from torch.optim.lr_scheduler import LambdaLR

from utils.math_utils import clip, lerp, log_lerp

def make_scheduler(config: dict, optimizer: Optimizer) -> LambdaLR:
    """Return a scheduler with a given configuration."""

    lr_init = config["optimizer"]["lr"]
    lr_final = config["scheduler"]["lr_final"]
    lr_delay_steps = config["scheduler"]["lr_delay_steps"]
    lr_delay_mult = config["scheduler"]["lr_delay_mult"]
    max_steps = config["trainer"]["max_steps"]

    def scheduler_step_func(steps: int) -> float:
        if lr_delay_steps > 0:
            # A kind of reverse cosine decay.
            delay_rate = lerp(math.sin(0.5 * math.pi * clip(steps / lr_delay_steps, 0.0, 1.0)), lr_delay_mult, 1.0)
        else:
            delay_rate = 1.0
        return delay_rate * log_lerp(steps / max_steps, lr_init, lr_final) / lr_init

    return LambdaLR(optimizer, scheduler_step_func)
