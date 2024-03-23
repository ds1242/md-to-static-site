import unittest
from copy_static import (
    copy_files,
)



class TestCopyStaticFiles(unittest.TestCase):
    def test_create_file_path(self):
        output = []
        start_path = './static'
        destination = './public'
        output = copy_files(start_path, output, destination)
        self.assertEqual(
            output,
            ['./public/index.css', './public/images/rivendell.png']
        )

        