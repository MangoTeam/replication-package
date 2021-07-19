# Replication Package Requirements

This replication package requires `git`, VirtualBox (`>=6.1`), and [Vagrant](https://www.vagrantup.com) (`>=2.0`). 

At minimum, VirtualBox alone is sufficient to run the provided VM image (see artifact details for Zenodo hosted VM).

Ensure that 

# Mockdown Requiremnts

Mockdown's requirements are listed in `implementation/mockdown/Pipfile`. A set of known-good pinned versions are listed in `Pipfile.lock` in the same directory.

In addition, `mockdown` itself requires `z3` and `swi-prolog`. Specifics are listed at the top of the `provision.sh` script in this directory, which also demonstrates how to install dependencies for each subpackage.

# Mockdown Client and Experiment Requirements

Similar to above, dependencies are listed in the `Pipfile` (and `package.json`) of each subpackage. Installation steps are very simple, and are demonstrated in `provision.sh`.