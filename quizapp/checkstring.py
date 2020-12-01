class CheckString:
    def trim_spaces(self, str):
        return str.replace(' ', '').replace('　', '')

    def check_str_length(self, problem, length):
        if len(problem) >= length:
            return True
        else:
            return False
