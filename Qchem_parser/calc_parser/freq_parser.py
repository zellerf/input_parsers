from .base_parser import BaseParser


class FreqParser(BaseParser):

    type = 'frequency'

    def __init__(self, file, userinput):
        BaseParser.__init__(self, file, userinput)
