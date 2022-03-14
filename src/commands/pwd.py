from src.commands.CommandInterface import CommandInterface
import os.path


class Pwd_inner(CommandInterface):
    def run(self, pipe_arg, exit_state):
        return [os.getcwd()]

