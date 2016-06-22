#!/usr/bin/env python

from curalate import *
import argparse
import sys
import subprocess


def handle_service(service_name=None):
    if service_name is None:
        print (subprocess.check_call(['ls']))
        return 0
    assert isinstance(service_name, str)
    if service_name.lower() == 'update':
        CuralateUpdate()


def main(args=None):
    cura_command = CuralateCommand(service=args.service, subcommand=args.command, options=args.options)
    try:
        output, err = cura_command.run()
        if output is not None:
            sys.stdout.write(output)
        return 0
    except Exception as e:
        sys.stderr(err)
    sys.stdout.flush()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Curalate dev tools')

    parser.add_argument('service', action="store", type=str)
    parser.add_argument('command', action="store", type=str)
    parser.add_argument('options', nargs='*', type=str)
    parser.parse_known_args(['service', 'command'])

    if len(sys.argv) == 2:
        sys.argv = sys.argv + ['run']

    # Add '--' to indicate to argparse that subsequent strings are not flags
    sys.argv = sys.argv[:3] + ['--'] + sys.argv[3:]

    args = parser.parse_args()
    print (args)
    sys.exit(main(args))

    # exe = CuralateExecution(service=args.service, subcommand=args.command, options=args.options)
    # exe.process()
    # handle_service(args.service)
