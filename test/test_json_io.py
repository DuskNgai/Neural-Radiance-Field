from pathlib import Path
import sys
import unittest

sys.path.append(str(Path(__file__).parent.parent))

from io_utils import JsonIO

class Test(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).parent.parent.joinpath("config")

    def test_input(self):
        data = JsonIO.input(self.root.joinpath("nerf.json"))
        print(data)

    def test_output(self):
        data = [{'A': 1}, {'B': 2}]
        JsonIO.output(self.root.joinpath("test.json"), data)

if __name__ == "__main__":
    unittest.main()
