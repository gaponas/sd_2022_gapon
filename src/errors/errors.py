class CommandArgumentsError(ValueError):
    def __init__(self, about_error):
        super().__init__(f"Command error: {about_error}")


class BashCommandError(Exception):
    def __init__(self, about_error):
        super().__init__(f"Bash error: {about_error}")


class NoVariableInMemory(ValueError):
    def __init__(self, about_error):
        super().__init__(f"Variable error: {about_error}")
