import unittest
from copy_static import (
    create_file_path,
    copy_files
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

    def test_copy_file(self):
        list_of_files = []
        list_of_files = create_file_path('./static', list_of_files)
        destination = './public'
        copy_files(list_of_files, destination)
    