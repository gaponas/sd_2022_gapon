from unittest import TestCase
from src.commands import grep
from src.cmd_work.shell import Shell_state
from src.errors.errors import CommandArgumentsError


class TestCommands(TestCase):
    exit_state = Shell_state()

    def test_simple(self):
        grep_com = grep.Grep_inner('a', "help_file.txt")
        grep_res = grep_com.run([], self.exit_state)
        expected_res = ['haha', 'hahahaha', 'a a a a']
        self.assertEqual(grep_res, expected_res)

    def test_regular(self):
        grep_com = grep.Grep_inner('(ha){3,}', "help_file.txt")
        grep_res = grep_com.run([], self.exit_state)
        expected_res = ['hahahaha']
        self.assertEqual(grep_res, expected_res)

    def test_regular_empty(self):
        grep_com = grep.Grep_inner('(ha){6}', "help_file.txt")
        grep_res = grep_com.run([], self.exit_state)
        self.assertEqual(grep_res, [])

    def test_A(self):
        grep_com = grep.Grep_inner('-A', 2, 'hahaha', "help_file.txt")
        grep_res = grep_com.run([], self.exit_state)
        expected_res = ['hahahaha', 'it is test file only', 'a a a a']
        self.assertEqual(grep_res, expected_res)

    def test_i(self):
        grep_com = grep.Grep_inner('-i', '(HA){3,}', "help_file.txt")
        grep_res = grep_com.run([], self.exit_state)
        expected_res = ['hahahaha']
        self.assertEqual(grep_res, expected_res)

    def test_w(self):
        grep_com = grep.Grep_inner('-w', 'ile', "help_file.txt")
        grep_res = grep_com.run([], self.exit_state)
        self.assertEqual(grep_res, [])

        grep_com = grep.Grep_inner('-i', 'file', "help_file.txt")
        grep_res = grep_com.run([], self.exit_state)
        expected_res = ['it is test file only']
        self.assertEqual(grep_res, expected_res)

    def test_file_error(self):
        grep_com = grep.Grep_inner('a', "hell_file.txt")
        with self.assertRaises(FileNotFoundError):
            grep_com.run([], self.exit_state)

    def test_arg_error(self):
        grep_com = grep.Grep_inner("help_file.txt")
        with self.assertRaises(CommandArgumentsError) as err:
            grep_com.run([], self.exit_state)

        grep_com = grep.Grep_inner('-a', 'a', "help_file.txt")
        with self.assertRaises(CommandArgumentsError) as err:
            grep_com.run([], self.exit_state)

        grep_com = grep.Grep_inner('-A', 'a', "help_file.txt")
        with self.assertRaises(CommandArgumentsError) as err:
            grep_com.run([], self.exit_state)

        grep_com = grep.Grep_inner()
        with self.assertRaises(CommandArgumentsError) as err:
            grep_com.run([], self.exit_state)

        grep_com = grep.Grep_inner('-A', '-5', 'a', "help_file.txt")
        with self.assertRaises(CommandArgumentsError) as err:
            grep_com.run([], self.exit_state)

        grep_com = grep.Grep_inner('a', '-i', "help_file.txt")
        with self.assertRaises(CommandArgumentsError) as err:
            grep_com.run([], self.exit_state)

        grep_com = grep.Grep_inner("-i")
        with self.assertRaises(CommandArgumentsError) as err:
            grep_com.run([], self.exit_state)
