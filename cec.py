import glob
import os
import pandas as pd
import sys
from optparse import Option, OptionParser
from os.path import basename, isdir, splitext
from chardet.universaldetector import UniversalDetector

class CEC(object):
    def check_encoding(self, file):
        detector = UniversalDetector()
        with open(file, mode='rb') as f:
            for binary in f:
                detector.feed(binary)
                if detector.done:
                    break
        detector.close()
        print("[File] {0}\t[Detects] {1}".format(file, detector.result))
        return detector.result['encoding']

    def output_header(self, header):
        return False if header == -1 else True

    def convert(self, options, args):
        input_target = '{0}/*' if isdir(args) else '{0}'
        files = glob.glob(input_target.format(args))
        for file in files:
            input_encoding = self.check_encoding(file)
            enc = input_encoding if options.input_encoding is None else options.input_encoding
            header = int(options.header)
            df = pd.read_csv(file, delimiter=options.input_delimiter, quotechar='\'', header=header, encoding=enc)
            filename, ext = splitext(basename(file))
            df.to_csv("result/{0}_{1}{2}".format(filename, options.output_encoding, ext), mode='w', sep=options.output_delimiter, quoting=3, index=False, header=self.output_header(header), encoding=options.output_encoding)

class MultipleOption(Option):
    ACTIONS = Option.ACTIONS + ("extend",)
    STORE_ACTIONS = Option.STORE_ACTIONS + ("extend",)
    TYPED_ACTIONS = Option.TYPED_ACTIONS + ("extend",)
    ALWAYS_TYPED_ACTIONS = Option.ALWAYS_TYPED_ACTIONS + ("extend",)

    def take_action(self, action, dest, opt, value, values, parser):
        if action == "extend":
            values.ensure_value(dest, []).append(value)
        else:
            Option.take_action(self, action, dest, opt, value, values, parser)

def start():
    parser = OptionParser(usage="usage: $ ./python.sh cec.py [options]", option_class=MultipleOption)
    parser.add_option("--input-encoding", default=None, help="specify the input file encoding")
    parser.add_option("--output-encoding", default="utf_8", help="specify the output file encoding. Default is 'utf_8'")
    parser.add_option("--input-delimiter", default="\t", help="specify the output file delimiter. Default is 'TAB'.")
    parser.add_option("--output-delimiter", default="\t", help="specify the output file delimiter. Default is 'TAB'.")
    parser.add_option("--header", default=-1, help="specify row number(s) to use as the column names, and the start of the data in input file."
                                                   "Default 'header=-1' has no header and reads the first line as data."
                                                   "header=0 denotes the first line of data rather than the first line of the file."
                                                   " e.g, -1: no header, 0: first line, 1: second line")

    options, args = parser.parse_args()

    if len(args) != 1:
        parser.print_help()
        sys.exit()

    cec = CEC()
    cec.convert(options, args[0])

if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        pass
    except IOError as e:
        if e.errno == errno.EPIPE:
            pass
        else:
            raise
