class Files:
    """
    Класс для работы с файлами
    """
    def read(self, path_to_file):
        """
        Выполняется чтение файла по заданному пути
        :param path_to_file: str, путь к файлу
        :return: list, массив строк файла
        """
        result = []
        with open(path_to_file) as f:
            for line in f:
                result.append(line.strip('\n'))
        return result

