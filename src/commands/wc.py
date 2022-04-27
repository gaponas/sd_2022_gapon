from src.commands.CommandInterface import CommandInterface


class Wc_inner(CommandInterface):

    def run(self, pipe_arg, exit_state):
        res_array = []
        count_of_lines, count_of_words, count_of_bytes = 0, 0, 0
        if len(self.args) == 0:
            count_of_lines, count_of_words, count_of_bytes = self.count_for_one(pipe_arg)
            res_array.append('%d\t%d\t%d' % (count_of_lines, count_of_words, count_of_bytes))
            return res_array
        for path_to_file in self.args:
            try:
                with open(path_to_file) as f:
                    file_lines, file_words, file_bytes = self.count_for_one(f)
                    count_of_lines += file_lines
                    count_of_words += file_words
                    count_of_bytes += file_bytes
                    res_array.append('%d\t%d\t%d\t%s' % (file_lines, file_words, file_bytes, path_to_file))
            except FileNotFoundError:
                raise FileNotFoundError(f"Not found {path_to_file}")
        if len(self.args) != 1:
            res_array.append('%d\t%d\t%d\ttotal' % (count_of_lines, count_of_words, count_of_bytes))
        return res_array

    @staticmethod
    def count_for_one(text):
        file_lines = 0
        file_words = 0
        file_bytes = 0
        for line in text:
            file_lines += 1
            file_words += len(line.split())
            file_bytes += len(line)
        return file_lines, file_words, file_bytes
