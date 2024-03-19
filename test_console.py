import unittest
from unittest.mock import patch
import io
from console import HBNBCommand
from models.base_model import BaseModel


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_preloop(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.console.preloop()
            self.assertEqual(fake_out.getvalue(), '(hbnb)\n')

    def test_precmd(self):
        cases = [
            ("show BaseModel 1234", "show BaseModel 1234"),
            ("all", "all"),
            ("BaseModel.show()", "show BaseModel "),
            ("BaseModel.update(\"1234\", {\"name\": \"test\"})",
                "update BaseModel 1234 {\"name\": \"test\"}"),
        ]

        for input_cmd, expected_cmd in cases:
            with self.subTest(input_cmd=input_cmd, expected_cmd=expected_cmd):
                actual_cmd = self.console.precmd(input_cmd)
                self.assertEqual(actual_cmd, expected_cmd)

    def test_postcmd(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.console.postcmd(False, '')
            self.assertEqual(fake_out.getvalue(), '(hbnb) ')

    def test_quit(self):
        with self.assertRaises(SystemExit):
            self.console.do_quit(None)

    def test_help_quit(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.console.help_quit()
            self.assertEqual(
                    fake_out.getvalue(), "Exit the program with formatting\n")

    def test_EOF(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.console.do_EOF(None)
            self.assertEqual(fake_out.getvalue(), "\n")


if __name__ == '__main__':
    unittest.main()
