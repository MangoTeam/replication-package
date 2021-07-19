## Installation instructions

This package requires `git`, VirtualBox, and [Vagrant](https://www.vagrantup.com). 

**Note:** we use git by SSH to fetch the submodules, so you will need to add an SSH key to your GitHub account.

To start, clone this repository using: 

> git clone git@github.com:MangoTeam/replication-package.git

Next, initialize the submodules to acquire the source code for `mockdown`, `mockdown-client`, `inferui-eval`, `flightlessbird.js` and `auto-mock`, using:

> git submodule update --init --recursive

If you get a permission error here from GitHub, it's probably because you need to add an SSH key to your GitHub account.

## Package structure

After following these instructions you should have a fully working copy of all of the following:

- In `./layouts/`, there should be a variety of JSON files. These correspond to our scraped websites.
- In `./implementation/`, there should be 5 different subfolders:
  + `mockdown`, Our main tool, written in Python.
  + `mockdown-client`, A JavaScript client for `mockdown`, intended for use in writing benchmarks, or integrating `mockdown` into web applications. Used by `auto-mock`.
  + `auto-mock` (placed in `implementation/web`), Evaluation for the web backend (RQ1-RQ3).
  + `inferui-eval` (placed in `implementation/android`), Evaluation for the Android backend (RQ4).
  + `flightlessbird.js`, A fork of the `kiwi.js` constraint solver, with some bug fixes and changes to faciliate adding multiple constraints at once. Used by `mockdown-client`.

- In `./experiments/`, there contains data and scripts for our experiments:
  + `overall`, CSV files and Excel spreadsheets for our RQ1 trials.

  + `noise`, CSV files and plotting scripts for our RQ2 trials. There are two subfolders, `3/` and `10/` which correspond to the 3 and 10 training examples. 

  + `scaling`, a CSV file, Excel spreadsheet, and helper python script for RQ3. 

  + `android`, a CSV file for RQ4.  

## Instructions: VirtualBox 

Simply decompress `mockdown-vm.tar.gz`, available at `https://goto.ucsd.edu/~dylan/mockdown-vm.tar.gz` and open the included `box.ovf` with VirtualBox.

The user credentials (if needed) are:

 - Username: `vagrant`
 - Password: `vagrant`

Contents are in ~/mockdown-replication-package.

## Instructions: Vagrant

Ensure you have VirtualBox installed. Then, you may provision and start the Vagrant virtual image by running:

> vagrant up

Lastly, connect to the running virtual machine with:

> vagrant ssh

## Instructions: Vagrant + Standalone Box

To reproduce the included image, first:

> STANDALONE=1 vagrant up

Note: if you have already created a non-standalone Vagrant VM, you will have to `vagrant destroy` it first, or instead run `STANDALONE=1 vagrant provision` on an existing image.

Then, with VirtualBox running:

> vagrant package --base $VM_NAME --output $OUTPUT_NAME.tar.gz

Where `$VM_NAME` is the name or UUID of your running VirtualBox VM , and `$OUTPUT_NAME` is the desired output location for the compressed image (and other files). *Note: this image does *not* depend on Vagrant, and is an "as-is" dump of the provisioned and running VM.*

You can get `$VM_NAME` either from the VirtualBox GUI or `cat .vagrant/machines/default/virtualbox/id`.

By default, the vagrant image is set up such that `/vagrant` maps to the root replication package; and also, if using VirtualBox, the VM is configured with 8GB of memory and 2 CPU cores (see lines 8 and 9 of `Vagrantfile`). Please adjust to your own machine as needed.

## Instructions: A Note on VM Performance

Note that replicating our results in a virtual machine, either through Vagrant, or with the provided VirtualBox image, will be slower than running outside of a VM. We evaluated our results on a machine with a quad-core 4ghz Intel i-6700k processor with 32GB of RAM. 

If you wish to, the included `provision.sh` shows which packages must be installed, and how to build/link each included component. On an Ubuntu or Debian system, it is sufficient to change $ROOT_DIR to the parent folder of this README.

Further details, including instructions for running experiments, can be found below, in the **Package Structure** section.