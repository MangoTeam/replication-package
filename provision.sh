# Configuration:
APT_PKGS="python3.8 python3-pip nodejs curl z3"
ROOT_DIR="/vagrant"

# Convenience:
PYTHON="python3.8"
PIP="python3.8 -m pip"
PIPENV="python3.8 -m pipenv"
JS="node"
NPM="npm"
YARN="yarn"

# TODO:
# if STANDALONE:

cd $ROOT_DIR

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

pushd ./implementation/mockdown
$PIPENV sync --dev
$PIPENV run -- python setup.py install
popd

echo ""
echo "PROVISION [3/X]: Setting up flightlessbird.js..."
echo "----------------------------------------------------"

pushd ./implementation/flightlessbird.js
$YARN install
$YARN link
popd

echo ""
echo "PROVISION [4/X]: Setting up mockdown-client"
echo "----------------------------------------------------"

pushd ./implementation/mockdown-client
$YARN link flightlessbird.js
$YARN install
$YARN link
popd

echo ""
echo "PROVISION [5/X]: Setting up eval-web"
echo "----------------------------------------------------"

# TODO: HANDLE PYTHON DEPS PROPERLY, MISSING PIPFILE.LOCK
# Best for John to add his from his computer where this was known to work?s

pushd ./implementation/eval-web
$YARN link flightlessbird.js
$YARN link mockdown-client
$YARN install
$YARN link
popd

echo ""
echo "PROVISION [6/X]: Setting up eval-android"
echo "----------------------------------------------------"

# TODO: HANDLE PYTHON DEPS PROPERLY, ADD PIPFILE?
# e.g. dataclasses_json

pushd ./implementation/eval-android
$PIPENV sync --dev
popd