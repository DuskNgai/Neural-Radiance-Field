from pathlib import Path

import imageio.v3 as iio
import numpy as np

from .base_io import BaseIO

class VideoIO(BaseIO):
    """An encapsulation of reading and writing video files using `imageio.ffmpeg` module."""

    PathType = BaseIO.PathType
    Itype = list[np.ndarray]
    Otype = list[np.ndarray]

    @staticmethod
    def input(file_name: PathType, **kwargs) -> Itype:
        """Reads a video file and returns a list of frames.
        Args:
            file_name (str): the file name of the video file.
            kwargs (Any): the keyword arguments for `imageio.imread`.
        Returns:
            (Itype): the list of frames.
        """

        data = iio.imread(file_name, **kwargs)
        return data

    @staticmethod
    def output(file_name: PathType, data: Otype, **kwargs) -> None:
        """Writes a list of frames to a video file.
        Default extension is `.mp4`, `fps` is 24 and `quality` is 10 if not specified.
        Args:
            file_name (PathType): the file name of the video file.
            data (Otype): the list of frames.
            kwargs (Any): the keyword arguments for `imageio.imwrite`.
        """

        extention = Path(file_name).suffix if Path(file_name).suffix else ".mp4"

        if "fps" not in kwargs:
            kwargs["fps"] = 24
        if "quality" not in kwargs:
            kwargs["quality"] = 10

        iio.imwrite(file_name, data, plugin = "pyav", extention = extention, **kwargs)
