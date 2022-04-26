from src.commands.CommandInterface import CommandInterface
from src.errors.errors import BashCommandError

import subprocess


class GoToBash(CommandInterface):
    def run(self, pipe_arg, exit_state):
        # TODO: error
        if isinstance(pipe_arg, list):
            pipe_arg = "\n".join(pipe_arg)
        try:
            res_arr = subprocess.run(self.args, input=pipe_arg, stdout=subprocess.PIPE, text=True)
            res_arr = res_arr.stdout.split("\n")
        except Exception as e:
            raise BashCommandError(e)
        return res_arr
