from typing import Any

import toml

from .base_io import BaseIO

class TomlIO(BaseIO):
    """An encapsulation of reading and writing TOML files."""

    PathType = BaseIO.PathType
    Itype = Any
    Otype = Any

    @staticmethod
    def input(file_name: PathType, **kwargs) -> Itype:
        """Read TOML file from disk.
        Args:
            file_name (PathType): the file name of the TOML file.
            kwargs (Any): the keyword arguments for `toml.load`.
        Returns:
            (Itype): the data loaded from the TOML file.
        """

        with open(file_name, 'r') as f:
            data = toml.load(f, **kwargs)
        return data

    @staticmethod
    def output(file_name: PathType, data: Otype, **kwargs) -> None:
        """Write TOML file to disk.
        Args:
            file_name (PathType): the file name of the TOML file.
            data (Otype): the data to be written.
            kwargs (Any): the keyword arguments for `toml.dump`.
        """

        with open(file_name, 'w') as f:
            toml.dump(data, f, **kwargs)
