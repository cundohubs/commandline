import sys, os
import subprocess
from subprocess import Popen, PIPE


RESERVED = {
    "update": 'CuralateUpdate'
}


CURALATE_PATH = os.environ['CURALATEPATH'] if 'CURALATEPATH' in os.environ.keys() \
    else "/usr/local/Library/Taps/curalate"


class CuralateExecution:
    def __init__(self, service, subcommand, options):
        self._service = service
        self._subcommand = subcommand
        self._options = options

    def process(self):
        if self._service in RESERVED.keys():
            getattr(RESERVED[self._service],'__init__')()


class CuralateCommand:
    def __init__(self, service, subcommand, options):
        self.service = service
        self._subcommand = subcommand
        self._options = options

    @property
    def subcommand(self):
        return self._subcommand

    def run(self):
        command = "/".join([CURALATE_PATH, "services", self.service, self.subcommand])
        try:
            sys.stdout.write(str([command] + self._options))
            p = Popen([command] + self._options, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            output, err = p.communicate(b"input data that is passed to subprocess' stdin")
            rc = p.returncode
            return output, err
        except OSError as e:
            sys.stdout.write("Failed executing command: %s" % command)
            sys.stdout.write(e.message)
        except subprocess.CalledProcessError as e:
            # print ("Subcommand failed to execute properly: %s" % command)
            if e.message is not None:
                sys.stdout.write(e.message)


class CuralateUpdate(CuralateCommand):
    def __init__(self):
        CuralateCommand.__init__(self, 'update', 'brew', [''])
        sys.stdout.write(subprocess.check_call(['git', 'pull']))
