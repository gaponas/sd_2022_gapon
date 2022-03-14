from src.cmd_work.request import Request


class Shell_state:
    """
    Класс для сохранения текущего состояния потока
    """

    def __init__(self):
        self.state = False

    def change_state(self, value):
        self.state = value

    def get_state(self):
        return self.state


class Shell:
    """
    Класс-интерпритатор bash
    """

    def __init__(self):
        self.exit_state = Shell_state()
        self.request = Request(self.exit_state)

    def run_shell(self):
        """
        выполняет последовательную обработку строк пока состояние не станет = False
        """
        while not self.exit_state.get_state():
            line_of_command = input()
            request_res = self.request.run(line_of_command)
            for line in request_res:
                print(line)
