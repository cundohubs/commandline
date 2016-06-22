# curacmd
Curalate command line tools

# Work in Progress
## Intentions
Integrate with Homebrew so that it can be deployed on Mac with a couple of commands: brew tap add curalate/curacmd; brew install curalate


Homebrew depends on a GitHub release package, or a *.tar.gz and then the curalate.rb file is the install script to download the package and configure locally.

Homebrew should install the Tap package in /usr/local/Library/Taps/

- The package should be in /usr/local/Library/Taps/
- Custom scripts, written by developers, should be deployed in /usr/local/Library/Taps/curalate/services/
- The brew tap when executed as follows:
-    curalate <service> <command> <options>
-    would execute the <command>.sh script in the /usr/local/Library/Taps/<service>/ directory passing the <options> as params

This allows developers to create and define their own "services" directory and store all shared scripts inside. This git repo will manage the services and scripts and be deployed as a package with the curalate command.
