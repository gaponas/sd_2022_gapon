from unittest import TestCase
from src.commands import cat, echo, exit, pwd, wc
from src.cmd_work.shell import Shell_state
from src.errors.errors import CommandArgumentsError

import os.path


class TestCommands(TestCase):
    exit_state = Shell_state()

    def test_cat(self):
        cat_com = cat.Cat_inner("help_file.txt")
        cat_res = cat_com.run([], self.exit_state)
        expected_res = ["haha", "hahahaha", "it is test file only", "a a a a"]
        self.assertEqual(cat_res, expected_res)

    def test_cat_no_file(self):
        cat_com = cat.Cat_inner("hell_file.txt")
        with self.assertRaises(FileNotFoundError):
            cat_res = cat_com.run([], self.exit_state)

    def test_echo(self):
        echo_com = echo.Echo_inner("a", "b", "c", "abc")
        echo_res = echo_com.run([], self.exit_state)
        expected_res = ["a b c abc"]
        self.assertEqual(echo_res, expected_res)

    def test_pwd(self):
        pwd_com = pwd.Pwd_inner()
        pwd_res = pwd_com.run([], self.exit_state)
        expected_res = [os.getcwd()]
        self.assertEqual(pwd_res, expected_res)

    def test_wc(self):
        wc_com = wc.Wc_inner("help_file.txt")
        wc_res = wc_com.run([], self.exit_state)
        expected_res = ['4\t11\t42\thelp_file.txt']
        self.assertEqual(wc_res, expected_res)

    def test_wc_no_file(self):
        wc_com = wc.Wc_inner("hell_file.txt")
        with self.assertRaises(FileNotFoundError):
            wc_com.run([], self.exit_state)

    def test_exit(self):
        exit_cmd = exit.Exit_inner()
        exit_cmd.run([], self.exit_state)
        self.assertTrue(self.exit_state.get_state())

    def test_wrong_arguments(self):
        cat_com = cat.Cat_inner()
        with self.assertRaises(CommandArgumentsError):
            cat_com.run([], self.exit_state)

        echo_com = echo.Echo_inner()
        with self.assertRaises(CommandArgumentsError):
            echo_com.run([], self.exit_state)


