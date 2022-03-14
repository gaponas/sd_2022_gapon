import re
from shlex import shlex

from src.folders.inner_memory import VarMemory, InnerCommands
from src.commands.go_to_bash import GoToBash


class Parser:

    def __init__(self):
        self.vars = VarMemory()
        self.inner_commands = InnerCommands()
        self.bash_commands = GoToBash

    def make_command_call(self, name, args):
        """
        Формирует команду из переданных значений
        :param name: str, имя команды
        :param args: list, список аргументов
        :return: CommandInterface, команда с переданными аргументами
        """
        command_info = self.inner_commands[name]
        if command_info is not None:
            return command_info(*args)
        return self.bash_commands(name, *args)

    def substitute_vars(self, line):
        """
        Выполняет подстановку значений локальных переменных в строку
        :param line: str, строка
        :return: str, строка-результат подстановки
        """
        find_vars = re.findall(r'\$\w{1,20}', line)
        find_vars = list(set(find_vars))
        for var in find_vars:
            var_name = var[1:]
            var_value = self.vars[var_name]
            if var_value is not None:
                line = line.replace('$' + var_name, var_value)

        return line

    def split(self, line):
        """
        Делит строку на токены -- части команд. Если передана строка присваивания значения переменной -- выполняет присваивание
        :param line: str, строка
        :return: list, список строк; если выполнили присваивание -- строка пустая
        """
        res_of_split = []
        split_line = shlex(line)
        split_line.wordchars += '$_-./'
        subline_count = 0
        for subline in split_line:
            subline_count += 1
            if subline[0] == '\'':
                res_of_split.append(subline[1:-1])
                continue
            if subline[0] == '\"':
                subline_for_process = subline[1:-1]
            else:
                subline_for_process = subline
            subst_subline = self.substitute_vars(subline_for_process)
            res_of_split.append(subst_subline)

        if re.match(r'\w{1,20}=\S', line) and subline_count == 3:
            var_name, var_value = line.split("=", maxsplit=1)
            self.vars[var_name] = var_value
            return []

        return res_of_split

    def parse(self, line):
        """
        Функция парсинга строки запроса
        :param line: str, строка запроса
        :return: list, массив команд
        """
        sublines = self.split(line)
        if not sublines:
            return []
        subcommands = []
        wait_new_command = True
        command_name = ''
        command_args = []
        for sub in sublines:
            if sub == '|':
                wait_new_command = True
                subcommands.append(self.make_command_call(command_name, command_args))
                command_name = ''
                command_args = []
            elif wait_new_command:
                command_name = sub
                wait_new_command = False
            else:
                command_args.append(sub)
        subcommands.append(self.make_command_call(command_name, command_args))
        return subcommands
