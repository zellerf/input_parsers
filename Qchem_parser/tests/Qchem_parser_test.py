from .. import Read


def main():
    print('start test')
    testparser = Read('/home/felix/local/pycharm-projects/Parses/Qchem_parser/tests/boc-chair-ee_b3lyp-d3_cc-pvdz_opt-freq.out')
    for i in testparser.get_calcs():
        print(i.get_type())


if __name__ == "__main__":
    main()