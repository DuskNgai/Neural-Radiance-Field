import json
from typing import Any

from .base_io import BaseIO

class JsonIO(BaseIO):
    """An encapsulation of reading and writing JSON files."""

    PathType = BaseIO.PathType
    Itype = Any
    Otype = Any

    @staticmethod
    def input(file_name: PathType, **kwargs) -> Itype:
        """Read JSON file from disk.
        Args:
            file_name (PathType): the file name of the JSON file.
            kwargs (Any): the keyword arguments for `json.load`.
        Returns:
            (Itype): the data loaded from the JSON file.
        """

        with open(file_name, 'r') as f:
            data = json.load(f, **kwargs)
        return data

    @staticmethod
    def output(file_name: PathType, data: Otype, **kwargs) -> None:
        """Write JSON file to disk.
        If the number of indentation is not specified, default to 4.
        Args:
            file_name (PathType): the file name of the JSON file.
            data (Otype): the data to be written.
            kwargs (Any): the keyword arguments for `json.dump`.
        """

        if "indent" not in kwargs:
            kwargs["indent"] = 4
        with open(file_name, 'w') as f:
            json.dump(data, f, **kwargs)
