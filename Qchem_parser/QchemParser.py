import sys
import re
from calculation import calculations


class QchemParser:

    # list of calculations found in file
    calculations = []

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
            print("Error: no Q-Chem calculation in file " + self.path)
            sys.exit(1)

        # skip first element in calcs since always only a blank
        for i in calcs[1:]:
            self.calculations.append(calculations.CalcCreator(i).create_calc_parser())

    # return list of calculations
    def get_calcs(self):
        return self.calculations
