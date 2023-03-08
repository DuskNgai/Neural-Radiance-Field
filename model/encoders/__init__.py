from model.encoders.encoder import Encoder
from model.encoders.trigonometric import TrigonometricEncoder
from model.encoders.spherical_harmonic import SphericalHarmonicEncoder
from utils.str_utils import string_case_insensitive

def make_encoder(config: dict) -> Encoder:
    """Build the encoder with respect to the configuration.
    Args:
        config (dict): The configuration of the encoder.
    Returns:
        Encoder: The encoder.
    """

    name = config["name"]
    if string_case_insensitive(name, "Trigonometric"):
        return TrigonometricEncoder(config)
    elif string_case_insensitive(name, "SphericalHarmonics"):
        return SphericalHarmonicEncoder(config)
    else:
        raise KeyError("Wrong encoder name: got `{}`.".format(name))
