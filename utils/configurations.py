import argparse

from io_utils import BaseIO, TomlIO

def load_config(file_name: BaseIO.PathType) -> dict:
    """Loads a configuration file and returns a dictionary.
    Args:
        file_name (TomlIO.PathType): the file name of the configuration file.
    Returns:
        (dict): the dictionary of the configuration.
    """

    return TomlIO.input(file_name)

def save_config(file_name: BaseIO.PathType, config: dict) -> None:
    """Saves a dictionary to a configuration file.
    Args:
        file_name (TomlIO.PathType): the file name of the configuration file.
        config (dict): the dictionary of the configuration.
    """

    TomlIO.output(file_name, config)

def merge_config_with_args(config: dict, args: argparse.Namespace) -> dict:
    """Merges a configuration dictionary with a namespace of command line arguments.
    Args:
        config (dict): the dictionary of the configuration.
        args (argparse.Namespace): the namespace of command line arguments.
    Returns:
        (dict): the merged dictionary of the configuration.
    """

    for args_key, args_value in vars(args).items():
        for sub_config in config.values():
            # Each `sub_config` should be a dictionary. Otherwise, skip it.
            if not isinstance(sub_config, dict):
                continue
            # Insert the value if find the corresponding key.
            if args_key in sub_config:
                sub_config[args_key] = args_value
                break
        # if `args_key` is not found in any sub-config, add it to the root config.
        else:
            config[args_key] = args_value

    return config
