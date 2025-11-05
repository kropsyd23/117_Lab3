import unittest
from unittest.mock import patch

import reader
import io

class TestReaderMethods(unittest.TestCase):

    @patch("reader.open_country_file")
    def test_read_country_file(self, ocf):
        ocf.return_value = [ {"name": "foo"}, {"name": "bar"} ]
        countries = reader.read_country_file()
        self.assertEqual(countries, [ {"name": "foo"}, {"name": "bar"} ])

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("reader.open_country_file")
    def test_rcf_eoferror(self, ocf, sysout):
        ocf.side_effect = EOFError()
        self.assertEqual(reader.read_country_file(), [])
        self.assertIn("End of file error", sysout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("reader.open_country_file")
    def test_rcf_filenotfounderror(self, ocf, sysout):
        ocf.side_effect = FileNotFoundError()
        self.assertEqual(reader.read_country_file(), [])
        self.assertIn("File not found error", sysout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("reader.open_country_file")
    def test_rcf_permissionerror(self, ocf, sysout):
        ocf.side_effect = PermissionError()
        self.assertEqual(reader.read_country_file(), [])
        self.assertIn("Permission error", sysout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    @patch("reader.open_country_file")
    def test_rcf_oserror(self, ocf, sysout):
        ocf.side_effect = OSError()
        self.assertEqual(reader.read_country_file(), [])
        self.assertIn("OS error", sysout.getvalue())

if __name__ == '__main__':
    unittest.main()