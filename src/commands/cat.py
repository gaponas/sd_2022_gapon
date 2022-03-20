from src.commands.CommandInterface import CommandInterface
from src.errors.errors import CommandArgumentsError


class Cat_inner(CommandInterface):

    def run(self, pipe_arg, exit_state):
        if len(self.args) == 0:
            raise CommandArgumentsError('cat expected 1 or more arguments')
        else:
            res_array = []
            for path_to_file in self.args:
                try:
                    with open(path_to_file) as f:
                        for line in f:
                            res_array.append(line.strip('\n'))
                except FileNotFoundError:
                    res_array.append("error info")
                    raise FileNotFoundError(f"Not found {path_to_file}")
            return res_array
