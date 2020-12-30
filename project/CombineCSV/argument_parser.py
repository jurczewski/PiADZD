import argparse

class ArgumentParser:
    args = None

    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog='combine csv files', formatter_class=argparse.RawTextHelpFormatter)

        self.parser.add_argument(metavar='Directory', dest='directory', type=str,
                                 help='Pelna sciezka do folderu z csv')
        self.parser.add_argument(metavar='outputName', dest='outputName', type=str,
                                 help='nazwa pliku wyjsciowego np test.csv')

        self.args = self.parser.parse_args()

    def get_directory(self):
        return self.args.directory
    def get_outputName(self):
        return self.args.outputName