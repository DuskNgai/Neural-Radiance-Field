from pathlib import Path
import sys
import unittest

import torch

sys.path.append(str(Path(__file__).parent.parent))

from model.encoders import make_encoder

class TestCase(unittest.TestCase):
    def setUp(self):
        self.x = torch.Tensor([[0.1, 0.2, 0.4]])

    def test_trigonometric(self):
        encoding = {
            "name": "Trigonometric",
            "in_dim": 3,
            "n_frequencies": 10,
            "log_sampling": True
        }
        encoder = make_encoder(encoding)
        self.assertEqual(encoder.in_dim, 3)
        self.assertEqual(encoder.out_dim, encoding["in_dim"] * encoding["n_frequencies"] * 2)
        output = encoder.forward(self.x)
        self.assertEqual(output.shape[:-1], self.x.shape[:-1])
        self.assertEqual(output.shape[-1], 60)

    def test_spherical_harmonics(self):
        encoding = {
            "name": "SphericalHarmonics",
            "in_dim": 3,
            "n_degrees": 4
        }
        encoder = make_encoder(encoding)
        self.assertEqual(encoder.in_dim, 3)
        self.assertEqual(encoder.out_dim, encoding["n_degrees"] ** 2)
        output = encoder.forward(self.x)
        self.assertEqual(output.shape[:-1], self.x.shape[:-1])
        self.assertEqual(output.shape[-1], encoding["n_degrees"] ** 2)

if __name__ == "__main__":
    unittest.main()
