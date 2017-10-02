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
        print("[File] {0}\t[Detector] {1}".format(file, detector.result))
        return detector.result['encoding']

    def convert(self, options, args):
        input_target = '{0}/*' if isdir(args) else '{0}'
        files = glob.glob(input_target.format(args))
        for file in files:
            input_encoding = self.check_encoding(file)
            df = pd.read_csv(file, delimiter=',', header='infer', encoding=input_encoding)
            filename, ext = splitext(basename(file))
            df.to_csv("result/{0}_{1}{2}".format(filename, options.output_encoding, ext), mode='w', index=False, header=True, encoding=options.output_encoding)

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
    parser = OptionParser(usage="usage: $ python cec.py [options]", option_class=MultipleOption)
    parser.add_option("--output-encoding", default="utf_8", help="specify the output file encoding")

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
