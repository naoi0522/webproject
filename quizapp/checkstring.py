class CheckString:
    @staticmethod
    def trim_spaces(str):
        return str.replace(' ', '').replace('　', '')

    @staticmethod
    def check_str_length(problem, length):
        if len(problem) >= length:
            return True
        else:
            return False
