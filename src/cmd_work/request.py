from src.parser.parser import Parser


class Request:
    """
    Класс-обаботчик одного запроса от пользователя
    """
    def __init__(self, exit_code):
        self.all_commands = []
        self.exit_code = exit_code
        self.parser = Parser()

    def run(self, text):
        """
        :param text: str, строка запроса
        :return: str, результат обработки запроса
        """
        self.all_commands = []
        self.all_commands = self.parser.parse(text)
        # TODO: errors
        result = ''
        for command in self.all_commands:
            result = command.run(result, self.exit_code)
        return result
