import sys
import re
from .calc_parser import ParserFactory


class Read:

    # list contains specific parser for each calculation
    __calcs = []

    # class constructor will read file and save it as list of calculations
    def __init__(self, path):
        if not isinstance(path, str):
            print('Error: QChem Parser expects string upon initialization')
            sys.exit(1)
        self.path = path
        self.__readfile__()

    # read file defined by path
    def __readfile__(self):
        print("reading file")
        try:
            with open(self.path) as ifile:
                file = ifile.read()

        except IOError:
            print("Error while opening file " + self.path)
            sys.exit(1)
        calcs = re.split('Welcome to Q-Chem', file)

        if len(calcs) == 1:
            print("Error: no Q-Chem calc_parser in file " + self.path)
            sys.exit(1)

        # skip first element in calcs since always only a blank
        for i in calcs[1:]:
            self.__calcs.append(ParserFactory(i).create_parser())

    # return list of calculations
    def get_calcs(self):
        return self.__calcs
