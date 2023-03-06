import imageio as iio
import numpy as np

from .base_io import BaseIO

class VolumeIO(BaseIO):
    """An encapsulation of reading and writing volume files using `imageio` module."""

    PathType = BaseIO.PathType
    Itype = None
    Otype = None

    @staticmethod
    def input(file_name: PathType, **kwargs) -> Itype:
        raise NotImplementedError

    @staticmethod
    def output(file_name: PathType, data: Otype, **kwargs) -> None:
        raise NotImplementedError
