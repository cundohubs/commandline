import subprocess
import sys

RESERVED = {
    "update": 'CuralateUpdate'
}

HELP = """
Usage: %s <service> <command> <command options>
where:
    service - path name of collection of scripts
    command - script name inside of the service
    options - parameters/flags passed to script

Default location of services is in /usr/local/Library/Taps/curalate/"""

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
        return subprocess.check_call([self._subcommand] + self._options)


class CuralateUpdate(CuralateCommand):
    def __init__(self):
        CuralateCommand.__init__(self, 'update', 'brew', [''])
        sys.stdout.write(subprocess.check_call(['git', 'pull']))


def handle_service(service_name=None):
    if service_name is None:
        print (subprocess.check_call(['ls']))
        return 0
    assert isinstance(service_name, str)
    if service_name.lower() == 'update':
        CuralateUpdate()


class CuralateHelp(CuralateCommand):
    def __init__(self, service=None):
        if service is None:
            self.service = "curalate"
        else:
            self.service = service
        CuralateCommand.__init__(self.service, "help", [])

    def run(self):
        if self.service == "curalate":
            return self.help_message

    @property
    def help_message(self):
        return HELP
