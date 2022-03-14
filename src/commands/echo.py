from src.commands.CommandInterface import CommandInterface


class Echo_inner(CommandInterface):
    def run(self, pipe_arg, exit_state):
        if len(self.args) == 0:
            # TODO error
            return []
        return [" ".join(self.args)]

