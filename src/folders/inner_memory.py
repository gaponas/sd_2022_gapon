from src.commands import cat, echo, exit, pwd, wc, grep


class VarMemory:
    """
    Класс, хранящий все локальные переменные, введенные пользователем в виде словаря <имя переменной>: <значение переменной>
    """

    def __init__(self):
        self.vars = {}

    def __getitem__(self, item):
        if item in self.vars:
            return self.vars[item]
        return None

    def __setitem__(self, key, value):
        self.vars[key] = value


class InnerCommands:
    """
    Класс, хранящий все реализованные команды bash
    """

    def __init__(self):
        self.commands = {}
        self.set_start_commands()

    def set_start_commands(self):
        self.commands['cat'] = cat.Cat_inner
        self.commands['echo'] = echo.Echo_inner
        self.commands['exit'] = exit.Exit_inner
        self.commands['pwd'] = pwd.Pwd_inner
        self.commands['wc'] = wc.Wc_inner
        self.commands['grep'] = grep.Grep_inner

    def __setitem__(self, name, func):
        self.commands[name] = func

    def __getitem__(self, name):
        if name in self.commands:
            return self.commands[name]
        else:
            return None
