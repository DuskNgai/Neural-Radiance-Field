import math
from typing import TypeVar

T = TypeVar('T')

def clip(val: T, min_val: T, max_val: T) -> T:
    """Clip a value between `min_val` and `max_val`."""
    if val < min_val:
        return min_val
    if val > max_val:
        return max_val
    return val

def lerp(t: float, u: T, v: T) -> T:
    """Interpolate linearly from `u` (t = 0) to `v` (t = 1)."""
    return clip(t, 0.0, 1.0) * (v - u) + u

def log_lerp(t: float, u: T, v: T) -> T:
    """Interpolate log-linearly from `u` (t = 0) to `v` (t = 1)."""
    if u <= 0 or v <= 0:
        raise ValueError("Interpolants {} and {} must be positive.".formar(u, v))    
    log_u = math.log(u)
    log_v = math.log(v)
    return math.exp(clip(t, 0.0, 1.0) * (log_v - log_u) + log_u)
