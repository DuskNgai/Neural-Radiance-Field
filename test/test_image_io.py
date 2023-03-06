from pathlib import Path
import sys
import unittest

import numpy as np

sys.path.append(str(Path(__file__).parent.parent))

from io_utils import ImageIO

class Test(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).parent.parent.joinpath("image")
        self.new_root = self.root.parent.joinpath("new_root")

    def test(self):
        # input/output
        image = ImageIO.input(self.root.joinpath("test.png"))
        self.assertIsInstance(image, np.ndarray)
        ImageIO.output(self.new_root.joinpath("test.png"), image)

        # input_directory/output_directory
        images = ImageIO.input_directory(self.root)
        self.assertIsInstance(images, list)
        self.assertIsInstance(images[0], np.ndarray)
        self.assertEqual(len(images), 100)
        ImageIO.output_directory(self.new_root, images)

if __name__ == "__main__":
    unittest.main()
