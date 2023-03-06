from pathlib import Path
from typing import Any, Union

class BaseIO(object):
    """
    The base class for all customized IO classes.
    All the derived classes should implement the method defined in this base class.
    All the derived classes should clearly define the `Itype` and `Otype` of the class.

    `Itype`: the data type read from the file.
    `Otype`: the data type written to the file.
    """

    PathType = Union[str, Path]
    Itype = Any
    Otype = Any

    @staticmethod
    def input(file_name: PathType, **kwargs) -> Itype:
        raise NotImplementedError

    @staticmethod
    def output(file_name: PathType, data: Otype, **kwargs) -> None:
        raise NotImplementedError
