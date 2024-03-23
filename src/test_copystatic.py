import unittest
from copy_static import (
    create_file_path
)


class TestCopyStaticFiles(unittest.TestCase):
    def test_create_file_path(self):
        output = []
        start_path = './static'
        output = create_file_path(start_path, output)
        self.assertEqual(
            output,
            ['./static/index.css', './static/images/rivendell.png']
        )

    def test_file_path_no_dir(self):
        output = []
        start_path = './static/images/rivendell.png'
        output = create_file_path(start_path, output)
        self.assertEqual(
            output,
            ['./static/images/rivendell.png']
        )

    def test_invalid_path(self):
        output = []
        start_path = '/'
        output = create_file_path(start_path, output)
        self.assertEqual(
            output,
            Exception('not a valid path')
        )