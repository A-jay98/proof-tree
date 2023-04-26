import argparse
from conf.loaders import *
from conf.base import settings
import logging

logging.basicConfig(level=logging.WARNING, format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S')


def main():
    if settings.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
        logging.debug("Config read:\n %s" % settings)
    if settings.UI:
        logging.debug("starting gui")
        from gui.app import App
        App().run()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a dependency graph of the proofs in a latex project.')

    conf_group = parser.add_argument_group('Configuration Options')
    conf_group.add_argument('-c', '--conf', help='configuration file')

    io_group = parser.add_argument_group('No Configuration Options')
    io_group.add_argument('-I', '--input', help='input root')
    io_group.add_argument('-O', '--output', default='out.png', help='output file')
    io_group.add_argument('-v', '--verbose', action='store_true', help='enable verbose output')

    args = parser.parse_args()

    if args.conf:
        if args.input:
            parser.error('Input/output options are not allowed when using a configuration file')
        if args.conf.endswith('.json'):
            load_json(args.conf)
        elif args.conf.endswith('.ini'):
            load_ini(args.conf)
    else:
        if not args.input:
            parser.error('At least one of input_file or conf_file must be provided')
            # TODO: handle arg inputs instead of conf file.
            raise NotImplementedError("This functionality is not implemented yet. Please use conf.json file.")

    main()
