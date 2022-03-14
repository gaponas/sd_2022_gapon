from src.commands.CommandInterface import CommandInterface
from src.folders.files import Files


class Cat_inner(CommandInterface):

    def run(self, pipe_arg, exit_state):
        if len(self.args) == 0:
            # TODO: error
            return []
        else:
            res_array = []
            for path_to_file in self.args:
                try:
                    res_array += Files.read(path_to_file)
                except FileNotFoundError:
                    res_array.append("error info")
                    break
                    # TODO: error
            return res_array
