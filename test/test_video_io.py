from pathlib import Path
import sys
import unittest

import numpy as np

sys.path.append(str(Path(__file__).parent.parent))

from io_utils import ImageIO, VideoIO

class Test(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).parent.parent.joinpath("video")

    def test_input(self):
        data = VideoIO.input(self.root.joinpath("test.mp4"))
        self.assertEqual(len(data), 100)
        self.assertIsInstance(data, list)
        self.assertIsInstance(data[0], np.ndarray)

    def test_output(self):
        data = ImageIO.input_directory(self.root.parent.joinpath("image"), key = lambda x: int(Path(x).name.split(".")[0]))
        VideoIO.output(self.root.joinpath("new_test.mp4"), data)

if __name__ == "__main__":
    unittest.main(warnings="ignore")
