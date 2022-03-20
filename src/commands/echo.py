from src.commands.CommandInterface import CommandInterface
from src.errors.errors import CommandArgumentsError


class Echo_inner(CommandInterface):
    def run(self, pipe_arg, exit_state):
        if len(self.args) == 0:
            raise CommandArgumentsError("echo expected 1 or more arguments")
        return [" ".join(self.args)]
