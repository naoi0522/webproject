class Check_String():
    def trim_spaces(self, str):
        return str.replace(' ', '').replace('　', '')
        # TODO 入力値の制限(改行など)

    def check_str_length(self, problem, len):
        if len(problem) >= len:
            return True
        else:
            return False
