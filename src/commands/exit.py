from src.commands.CommandInterface import CommandInterface


class Exit_inner(CommandInterface):
    def run(self, pipe_arg, exit_state):
        exit_state.change_state(True)
        return pipe_arg
