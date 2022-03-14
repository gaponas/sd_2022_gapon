from src.commands.CommandInterface import CommandInterface

import subprocess


class GoToBash(CommandInterface):
    def run(self, pipe_arg, exit_state):
        # TODO: error
        if isinstance(pipe_arg, list):
            pipe_arg = "\n".join(pipe_arg)
        res_arr = subprocess.run(self.args, input=pipe_arg, stdout=subprocess.PIPE, text=True)
        res_arr = res_arr.stdout.split("\n")
        return res_arr
