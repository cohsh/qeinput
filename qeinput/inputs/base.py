class InputBase:
    def __init__(self):
        self.text = ""

    def add(self, string):
        self.text += string

    def clear(self):
        self.text = ""

    def generate(self, file_name):
        with open(file_name, mode="w") as f:
            f.write(self.text)
