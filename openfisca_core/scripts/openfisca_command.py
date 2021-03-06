import argparse
import sys

from openfisca_web_api_preview.scripts.serve import define_command_line_options, main as serve


"""
    Define the `openfisca` command line interface.
"""


def get_parser():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='Available commands')
    parser_serve = subparsers.add_parser('serve', help='Run the OpenFisca Web API')
    parser_serve = define_command_line_options(parser_serve)

    return parser


def main():
    parser = get_parser()
    sys.exit(serve(parser))


if __name__ == '__main__':
    sys.exit(main())
