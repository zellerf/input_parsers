from .base_parser import BaseParser


class OptParser(BaseParser):

    type = 'opt'

    def __init__(self, file, userinput):
        BaseParser.__init__(self, file, userinput)
