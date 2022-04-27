class CommandInterface:
    def __init__(self, *args):
        self.args = args

    def run(self, pipe_arg, exit_state):
        return []
