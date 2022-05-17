import sys


class QchemParser:
    def __init__(self, path, ncalcs=1):
        self.file = []
        self.ncalcs = ncalcs
        self.__read_file(path)

    def __read_file(self, path):
        try:
            with(open(path)) as ifile:
                self.file = ifile.readlines()
        except OSError:
            print("Error in Qchem_parser: cannot open " + path)
            sys.exit(1)
