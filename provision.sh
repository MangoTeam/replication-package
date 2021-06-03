PYTHON="python3.8"
APT_PKGS="python3.8 python3-pip nodejs z3"

echo "PROVISION [1/X]: Ensuring installed packages..."
echo "-----------------------------------------------"

apt-get -y update
apt-get -y install $APT_PKGS

cd /vagrant

echo ""
echo "PROVISION [2/X]: Installing mockdown dependencies..."
echo "----------------------------------------------------"

pushd implementation/mockdown
$PYTHON -m pip install pipenv
pipenv sync
popd

