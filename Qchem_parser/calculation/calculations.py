import re
import sys


class CalcCreator:

    def __init__(self, file):

        if not isinstance(file, str):
            print("Error calculations classes expect file to be a raw string")
            sys.exit(1)
        self.__file = file

    # read inputsection from file containing Q-Chem calculation
    def __get_input__(self):
        # search for start of input
        inputstart = re.search('-{62}\nUser input:\n-{62}', self.__file)

        # input reaches from end of user input pattern to next input divison line
        inputend = re.search('-{20}', self.__file[inputstart.end():])

        # error if input patterns are not found
        if not bool(inputstart) or not bool(inputend):
            print("Error: calculation does not have an input.")
            sys.exit(1)
        userinput = self.__file[inputstart.end():inputstart.end() + inputend.start()]
        return userinput

    # get jobtype of calculation input string
    def __get_type__(self, userinput):

        # search for jobtype line
        match = re.search('jobtype\W+\w+', userinput, flags=re.I)

        # job_type REM variable is also valid
        if not match:
            match = re.search('job_type\W+\w+', userinput, flags=re.I)

        # if jobtype was not set use sp, which is default
        if match:
            jobtype = re.findall('\w+', userinput[match.start():match.end()], flags=re.I)[1]
        else:
            jobtype = 'sp'

        return jobtype

    def create_calc_parser(self):
        input = self.__get_input__()
        jobtype = self.__get_type__(input)

       #TODO: make real calc parser objects
        print(jobtype)
        return jobtype

