import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from toml_task.convert import convert_file


class TestTomlToJson(unittest.TestCase):
    def test_conversion_and_sorting(self):
        with TemporaryDirectory() as temp_dir:
            src = Path(temp_dir) / "input.toml"
            dst = Path(temp_dir) / "result.json"
            src.write_text('student = "Анна"\ncourse = 2\nscores = [5, 3, 4, 2]\n', encoding="utf-8")
            data = convert_file(src, dst)
            self.assertEqual(data["scores"], [2, 3, 4, 5])
            self.assertEqual(json.loads(dst.read_text(encoding="utf-8")), data)
            self.assertEqual(len(data), 3)

    def test_less_than_three_fields(self):
        with TemporaryDirectory() as temp_dir:
            src = Path(temp_dir) / "input.toml"
            src.write_text('scores = [2, 1]\nname = "X"\n', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "минимум 3"):
                convert_file(src, Path(temp_dir) / "out.json")

    def test_array_missing(self):
        with TemporaryDirectory() as temp_dir:
            src = Path(temp_dir) / "input.toml"
            src.write_text('name = "X"\ncourse = 1\nscores = 3\n', encoding="utf-8")
            with self.assertRaises(ValueError):
                convert_file(src, Path(temp_dir) / "out.json")

    def test_custom_array_field(self):
        with TemporaryDirectory() as temp_dir:
            src = Path(temp_dir) / "input.toml"
            src.write_text('name = "X"\ncourse = 1\nnumbers = [9, -2, 3]\n', encoding="utf-8")
            data = convert_file(src, Path(temp_dir) / "out.json", "numbers")
            self.assertEqual(data["numbers"], [-2, 3, 9])


if __name__ == "__main__":
    unittest.main()
