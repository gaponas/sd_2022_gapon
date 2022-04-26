from src.parser.parser import Parser

from src.errors.errors import *


class Request:
    """
    Класс-обаботчик одной строки запросов от пользователя
    """

    def __init__(self, exit_code):
        self.all_commands = []
        self.exit_code = exit_code
        self.parser = Parser()

    def run(self, text):
        """
        Выполняет строку запроса
        :param text: str, строка запроса
        :return: list[str], результат обработки запроса разбитый на строки для вывода
        """
        self.all_commands = []
        try:
            self.all_commands = self.parser.parse(text)
        except NoVariableInMemory as e:
            return [str(e)]
        result = ''
        try:
            for command in self.all_commands:
                result = command.run(result, self.exit_code)
        except FileNotFoundError as e:
            return [str(e)]
        except CommandArgumentsError as e:
            return [str(e)]
        except BashCommandError as e:
            return [str(e)]
        return result
