#!/bin/bash

# Tell apt (and others) this is not an interactive shell.
# e.g. don't try to access non-existent stdin.
export DEBIAN_FRONTEND=noninteractive

# Configuration:
APT_PKGS="python3.8 python3-pip nodejs curl z3 jq swi-prolog"
ROOT_DIR="/vagrant"
SYM_DIR="/home/vagrant/replication-package"

# Convenience:
PYTHON="python3.8"
PIP="python3.8 -m pip"
PIPENV="python3.8 -m pipenv"
JS="node"
NPM="npm"
YARN="yarn"

if [[ -n "$STANDALONE" ]]; then
    echo "PROVISION [0/X]: Provisioning in STANDALONE mode..."
    echo "---------------------------------------------------"
    mkdir /home/vagrant/mockdown-replication-package
    # Note: this is rsync to facilitate repeated debugging of provisioning...
    rsync -a /vagrant/. /home/vagrant/mockdown-replication-package/
    ROOT_DIR="/home/vagrant/mockdown-replication-package"
fi

cd $ROOT_DIR
ln -s $ROOT_DIR $SYM_DIR

echo "PROVISION [1/X]: Ensuring installed packages..."
echo "-----------------------------------------------"

# Ubuntu 18.04's default PPA has ancient Node.
curl -sL https://deb.nodesource.com/setup_16.x | sudo -E bash - 

sudo apt-get -y update
sudo apt-get -y install $APT_PKGS

# Package managers: bet you can't have just one.
$PYTHON -m pip install --user pipenv
sudo $NPM install --global yarn

echo ""
echo "PROVISION [2/X]: Setting up mockdown..."
echo "----------------------------------------------------"

pushd "$ROOT_DIR/implementation/mockdown"
$PIPENV sync --dev
$PIPENV run -- python setup.py install
popd

echo ""
echo "PROVISION [3/X]: Setting up flightlessbird.js..."
echo "----------------------------------------------------"

pushd "$ROOT_DIR/implementation/flightlessbird.js"
$YARN install
$YARN build
$YARN link
popd

echo ""
echo "PROVISION [4/X]: Setting up mockdown-client"
echo "----------------------------------------------------"

pushd "$ROOT_DIR/implementation/mockdown-client"
$YARN link flightlessbird.js
$YARN install
$YARN build
$YARN link
popd

echo ""
echo "PROVISION [5/X]: Setting up eval-web"
echo "----------------------------------------------------"

# TODO: HANDLE PYTHON DEPS PROPERLY, MISSING PIPFILE.LOCK
# Best for John to add his from his computer where this was known to work?s

pushd "$ROOT_DIR/implementation/eval-web"
$YARN link flightlessbird.js
$YARN link mockdown-client
$YARN install
$YARN build
popd

echo ""
echo "PROVISION [6/X]: Setting up eval-android"
echo "----------------------------------------------------"

# TODO: HANDLE PYTHON DEPS PROPERLY, ADD PIPFILE?
# e.g. dataclasses_json

pushd "$ROOT_DIR/implementation/eval-android"
$PIPENV sync --dev
popd