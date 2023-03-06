from pathlib import Path
from typing import Callable, Optional

import imageio.v3 as iio
import numpy as np

from .base_io import BaseIO

class ImageIO(BaseIO):
    """
    An encapsulation namespace of reading and writing image files using `imageio` module.
    It can read from and write to a directory.
    """

    PathType = BaseIO.PathType
    Itype = np.ndarray
    Otype = np.ndarray

    @staticmethod
    def input(file_name: PathType, **kwargs) -> Itype:
        """Read single image file.
        Args:
            file_name (PathType): the file name of the image file.
            kwargs (Any): the keyword arguments for `imageio.imread`.
        Returns:
            (Itype): The image data with shape (H, W, C).
        """

        data = iio.imread(file_name, **kwargs)
        return data

    @staticmethod
    def input_directory(dir_name: str, *, key: Callable[[str, str], bool] = None, **kwargs) -> list[Itype]:
        """Read all the images from a directory.
        Args:
            dir_name (str): the directory name.
            key (Callable[[str, str], bool]): the key function for sorting the images.
            kwargs (Any): the keyword arguments for `imageio.imread`.
        Returns:
            (list[Itype]): the list of image data.
        """

        assert Path(dir_name).is_dir(), "Directory name [{}] is not a directory.".format(dir_name)
        file_names = [file_name for file_name in Path(dir_name).iterdir() if file_name.is_file()]
        file_names.sort(key = key)

        data = [ImageIO.input(file_name, **kwargs) for file_name in file_names]
        return data

    @staticmethod
    def output(file_name: PathType, data: Otype, **kwargs) -> None:
        """Write single image file to disk.
        Args:
            file_name (PathType): the file name of the image file.
            data (Otype): the image data to be written.
            kwargs (Any): the keyword arguments for `imageio.imwrite`.
        """

        iio.imwrite(file_name, data, **kwargs)

    @staticmethod
    def output_directory(dir_name: str, data: list[Otype], *, name_list: Optional[list[str]] = None, **kwargs) -> None:
        """Write all the images to a directory.
        Args:
            dir_name (str): the directory name.
            data (list[Otype]): the list of image data.
            name_list (list[str], Optional): the list of file names.
            kwargs (Any): the keyword arguments for `imageio.imwrite`.
        """

        Path(dir_name).mkdir(exist_ok = True)

        if name_list is None:
            name_list = ["{}.png".format(i) for i in range(len(data))]
        for image, name in zip(data, name_list):
            ImageIO.output(Path(dir_name).joinpath(name), image, **kwargs)
