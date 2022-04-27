from src.commands.CommandInterface import CommandInterface
from src.errors.errors import CommandArgumentsError
import re


class Grep_inner(CommandInterface):

    def __init__(self, *args):
        self.error = None
        if len(args) == 0:
            self.error = CommandArgumentsError('grep expected template at least')
        self.ignore_case = False
        self.found_word = False
        self.show_lines_after = False
        self.count_lines_after = 0
        self.template = None
        self.file_paths = None

        self.parse_args(args)

    def parse_args(self, *args):
        prev_arg = None

        for arg in args[0]:
            if prev_arg == "-A":
                try:
                    self.count_lines_after = int(arg)
                    prev_arg = None
                    if self.count_lines_after < 0:
                        self.error = CommandArgumentsError('grep argument -A should be with number of lines')
                except ValueError:
                    self.error = CommandArgumentsError('grep argument -A should be with number of lines')
            elif arg[0] == "-":
                if prev_arg is None or prev_arg[0] == "-":
                    prev_arg = arg
                    if arg == "-i":
                        self.ignore_case = True
                    elif arg == "-w":
                        self.found_word = True
                    elif arg == "-A":
                        self.show_lines_after = True
                    else:
                        self.error = CommandArgumentsError(f'invalid argument {arg}')
                else:
                    self.error = CommandArgumentsError('grep wrong arguments')
            elif self.template is None and (prev_arg is None or prev_arg[0] == "-"):
                prev_arg = arg
                self.template = arg
            elif self.file_paths is None:
                self.file_paths = [arg]
            else:
                self.file_paths.append(arg)

        if self.template is None:
            self.error = CommandArgumentsError('grep expected template')

    def run(self, pipe_arg, exit_state):
        res_array = []
        if self.error is not None:
            raise self.error
        if self.file_paths is None and len(pipe_arg) == 0:
            raise CommandArgumentsError('grep: no file to search')
        if self.found_word:
            self.template = r'(^|\W){template}($|\W)'.format(template=self.template)
        else:
            self.template = r'{template}'.format(template=self.template)
        if self.ignore_case:
            self.template = re.compile(self.template, re.IGNORECASE)
        else:
            self.template = re.compile(self.template)
        if self.file_paths is None:
            return self.found_in_text(pipe_arg)
        for file_path in self.file_paths:
            try:
                with open(file_path) as f:
                    res_array += self.found_in_text(f)
            except FileNotFoundError:
                raise FileNotFoundError(f"Not found {file_path}")
        return res_array

    def found_in_text(self, text):
        res = []
        text = [l for l in text]
        for i in range(len(text)):
            if self.template.search(text[i]):
                for j in range(i, i + 1 + self.count_lines_after):
                    res.append(text[j].strip('\n'))
        return res
