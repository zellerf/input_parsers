class BaseParser:

    type = None

    def __init__(self, file, userinput):
        self.file = file
        self.input = userinput

    def get_type(self):
        return self.type
