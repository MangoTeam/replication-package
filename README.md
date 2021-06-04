# fse-21-24-replication-package
This a replication package for FSE 2021 submission Synthesis of Web Layouts from Examples.
It contains our experimental data, scraped web layouts, our implementation as submodules,
and a Vagrant provisioning script for replicating our experimental results.

## Installation instructions

This package requires `git`, VirtualBox, and [Vagrant](https://www.vagrantup.com). Note:
 we use git by SSH to fetch the submodules, so you will need to add an SSH key to 
 your GitHub account.

To start, clone this repository using: 
> git clone git@github.com:MangoTeam/replication-package.git

Next, initialize the submodules to acquire the source code for `mockdown`, `mockdown-client`, `inferui-eval`, `flightlessbird.js` and `auto-mock`, using:

> git submodule --init --recursive

If you get a permission error here from GitHub, it's probably because you need to add 
an SSH key to your GitHub account.

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

## Instructions: VirtualBox (TODO)

Simply load the provided `mockdown.vbox` into VirtualBox.

The user credentials are:

 - Username: `vagrant`
 - Password: `vagrant`

## Instructions: Vagrant

Ensure you have VirtualBox installed. Then, you may provision and start the Vagrant virtual image image by running:

> vagrant up

Lastly, connect to the running virtual machine with:

> vagrant ssh

To reproduce the included image, with VirtualBox running:

> vagrant package --base $VM_NAME --output $OUTPUT_NAME

Where `$VM_NAME` is the name of or UUID of your running VirtualBox VM, and `$OUTPUT_NAME` is the desired output location for the image. *Note: this image does *not* depend on Vagrant, and is an "as-is" dump of the provisioned and running VM.*

Further details, including instructions for running experiments, can be found below, in the **Package Structure** section.

## Package Structure

This package is structured as follows.

- `layouts/` contains json files that correspond to the scraped micro and macrobenchmarks. 

- `implementation/` contains the source code, as well as runner scripts for regenerating the raw data for the experiments.
  + Our main tool is in `implementation/mockdown/` and has installation instructions its own `README.md` file.
  Several example inputs are in `tests/`, for example `tests/inferui/onetwo.json`.
  Mockdown can be run by command line or as a server on the localhost. Of these, command line is easiest to use;
  for usage, run `mockdown run --help` from a pipenv shell within the Mockdown directory.

  + Our website layout backend is in `implementation/web/` and can be run using `npm`. We currently manually scrape layouts and the process is detailed in `web/README.md`.


## Experimental claims

Our paper makes the following broad experimental claims:
- We contribute a a tool, Mockdown, for synthesizing layouts from input-output examples. This claim is witnessed by the contents of `implementation/mockdown`.
- Our work scrapes layouts from real-world websites. This claim is witnessed by the layout scraper in `implementation/eval-web` and the layouts in `layouts/`. 
- We disclose raw data, layouts, and scripts for rerunning our evaluation. This is witnessed by the subfolders of this package. 

We also make the following detailed experimental claims in our evaluation section:
- RQ1: Mockdown synthesizes layouts that are very close to the original layout, in Table 1 and Table 2.  Table 1 is witnessed by `experiments/overall/macro.xlsx` and Table 2 is witnessed by `experiments/overall/micro.xls`.
- RQ2: The noise-tolerant synthesis algorithms avoid high RMSD, the `nt-all` algorithm improves on the accuracy of `nt-none` (Fig 5a and 5b), and the noise-tolerant performance is not significantly worse than the performance of a rigid inference algorithm (Fig 6a and 6b). 
Fig 5a and 5b are witnessed by `experiments/error_3.png`, `experiments/error_10.png`, `experiments/accuracy_3.png`, and `experiments/accuracy_10.png`. Fig 6a and 6b is witnessed by `synthtime_3.png` and `synthtime_10.png`.
- RQ3: Hierarchical decomposition is necessary to synthesize layouts, and scales linearly with the number of sublayouts in a grid benchmark (Fig 7a and 7b). 
This is witnessed by `experiments/scaling/scaling_sheet.xlsx`.
- RQ4: Mockdown synthesizes android layouts with low RMSD (Fig 8a) and high accuracy (Fig 8b). These are witnessed by `experiments/android_error.png` and `experiments/android_accuracy.png` respectively.

We also provide raw data for all of these claims, as well as scripts for regenerating the data, and generating plots from the data.

## Artifact evaluation instructions

We next provide detailed instructions for generating the above plots, as well as for rerunning our experiments.

### Generating plots
- RQ1: The raw data for `experiments/overall/macro.xlsx` and `experiments/overall/micro.xls` are in CSV format. We provide our original evaluation data in `micro-10.csv`, `micro-3.csv`, `macro-10.csv`, and `macro-3.csv` (all within `experiments/overall/`). To import this data into the Table 1 and Table 2 spreadsheets, directly copy-paste the CSV data into respective sheet. For example, to rebuild Table 2 with new data for `micro-3.csv`, copy the contents of `micro-3.csv` into the 3ex sheet of `micro.xls`. The new Table 2 is automatically updated in the Table sheet of `micro.xls`; notice that it contains an extra (extraneous) row for summary statistics about the hierarchical benchmarks.

  To replicate our claims, import the data from `micro-10.csv` and `micro-3.csv` into `micro.xlsx`, and `macro-10.csv` and `macro-3.csv` into `macro.xlsx`. The Table sheets should correspond to Table 1 and Table 2 of our paper.

  In particular, the majority of benchmarks should finish, the RMS should be low (below 1.0), and the Accuracy should be high. The rate of timeouts and the synthesis time might differ due to slowdown from running in a VM.

- RQ2: In `experiments/noise` there are 6 CSV files that correspond to the 3 algorithms run on 3 and 10 training examples: `3/baseline.csv`, `3/nt-none.csv`, `3/nt-all.csv`, `10/baseline.csv`, `10/nt-none.csv`, and `10/nt-none.csv`.

  To build the graphs for RQ2, Figure 5 and Figure 6,
  change directory to `experiments` and start a `pipenv` shell: 

  > cd experiments
  > pipenv shell

  Next load the plotting script `plot.py`: 
  
  > python3 -i plot.py
  
  and finally, run the python functions `plot_accuracy()`, `plot_error()`, and `plot_synth_time()` from the python prompt: 

  > plot_accuracy()
  > plot_error()
  > plot_synth_time()

  This should produce 6 png images in `experiments/` as specified above (i.e. `error_3.png`, `accuracy_10.png`, etc), which correspond to the subfigures in Fig 5 and Fig 6. 

  In particular, the `baseline` algorithm should have several entries with high RMS error (> 100), while the `nt-none` and `nt-all` algorithms should have all RMS below 10. Also, the `nt-all` should have higher accuracy than the `nt-none` algorithm in general. 

  In runtime, the `baseline` algorithm should perform better but the difference should not be drastic (see Figure 6).


- RQ3: The raw data for RQ3 is in `experiments/scaling/scaling_data.csv`. To build the graph for RQ3 (Figure 7), change directory to 
  `experiments/scaling/` and run `import_scaling.py`: 
  > cd experiments/scaling
  > python3 import_scaling.py 
  
  
  This should print out CSV output. Take this output and copy-paste it into the excel spreadsheet `experiments/scaling/scaling_sheet.xlsx`. There is only one sheet, with one graph, and the graph should automatically update when the data is changed.

  Overall the hierarchical algorithm should scale linearly as a function of elements, while the flat algorithm should blow up for a few benchmarks (see Figure 7).


- RQ4: The raw data is in in `experiments/android/android_results.csv`. To build the graph for RQ4, Figure 8, we again use the plotting script in `experiments`, `plot.py`. 

  First change directory to the experiments folder and start a pipenv shell: 
  
  > cd experiments
  > pipenv shell
  
  Next, load `plot.py` in python and run the `plot_error_android()` and `plot_accuracy_android()` functions: 
  
  > python3 -i plot.py
  > plot_error_android()
  > plot_accuracy_android()
  
  This produces plots `experiments/android_error.png` and `experiments/android_accuracy.png` that correspond to the subfigures of Figure 8.

  In particular, the RMS error should be very low for most benchmarks, and the accuracy should be very high.

### Running experiments (TODO)