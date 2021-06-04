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

## Package Structure

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

We next provide detailed instructions for generating the above plots, as well as for rerunning our experiments. All of the commands below should be run starting from the root replication package directory of `replication-package/`. 

### Generating plots
- RQ1: The raw data for `experiments/overall/macro.xlsx` and `experiments/overall/micro.xls` are in CSV format. We provide our original evaluation data in `micro-10.csv`, `micro-3.csv`, `macro-10.csv`, and `macro-3.csv` (all within `experiments/overall/`). To import this data into the Table 1 and Table 2 spreadsheets, directly copy-paste the CSV data into respective sheet. For example, to rebuild Table 2 with new data for `micro-3.csv`, copy the contents of `micro-3.csv` into the 3ex sheet of `micro.xls`. The new Table 2 is automatically updated in the Table sheet of `micro.xls`; notice that it contains an extra (extraneous) row for summary statistics about the hierarchical benchmarks.

  To replicate our claims, import the data from `micro-10.csv` and `micro-3.csv` into `micro.xlsx`, and `macro-10.csv` and `macro-3.csv` into `macro.xlsx`. The Table sheets should correspond to Table 1 and Table 2 of our paper.

  In particular, the majority of benchmarks should finish, the RMS should be low (below 1.0), and the Accuracy should be high. The rate of timeouts and the synthesis time might differ due to slowdown from running in a VM.

- RQ2: In `experiments/noise` there are 6 CSV files that correspond to the 3 algorithms run on 3 and 10 training examples: `3/baseline.csv`, `3/nt-none.csv`, `3/nt-all.csv`, `10/baseline.csv`, `10/nt-none.csv`, and `10/nt-none.csv`.

  To build the graphs for RQ2, Figure 5 and Figure 6,
  change directory to `experiments` and start a `pipenv` shell: 

  > pushd experiments

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

  Validate the claims by inspecting the output images, and then exit the pipenv shell and return to `replication-package/`:

  > exit

  > popd


- RQ3: The raw data for RQ3 is in `experiments/scaling/scaling_data.csv`. To build the graph for RQ3 (Figure 7), change directory to 
  `experiments/scaling/` and run `import_scaling.py`: 

  > pushd experiments/scaling

  > python3 import_scaling.py 
  
  
  This should print out CSV output. Take this output and copy-paste it into the excel spreadsheet `experiments/scaling/scaling_sheet.xlsx`. There is only one sheet, with one graph, and the graph should automatically update when the data is changed.

  Overall the hierarchical algorithm should scale linearly as a function of elements, while the flat algorithm should blow up for a few benchmarks (see Figure 7).

  Validate the claims by inspecting the graph in `scaling_sheet.xlsx`, and then return to the root directory: 

  > popd

- RQ4: The raw data is in in `experiments/android/android_results.csv`. To build the graph for RQ4, Figure 8, we again use the plotting script in `experiments`, `plot.py`. 

  First change directory to the experiments folder and start a pipenv shell: 
  
  > pushd experiments

  > pipenv shell
  
  Next, load `plot.py` in python and run the `plot_error_android()` and `plot_accuracy_android()` functions: 
  
  > python3 -i plot.py

  > plot_error_android()

  > plot_accuracy_android()
  
  This produces plots `experiments/android_error.png` and `experiments/android_accuracy.png` that correspond to the subfigures of Figure 8.

  In particular, the RMS error should be very low for most benchmarks, and the accuracy should be very high.

  Validate the claims by comparing the png plots with the figures in the paper, and then exit the pipenv shell and return to the root directory: 
  > exit

  > popd


### Running experiments

We have included helper scripts for rerunning all of the experiments. In all cases the output data will be as a CSV file within `implementation/` and needs to be copied to the corresponding file within `experiments/`. 
- RQ1: First change directory to `implementation/eval-web/` and start a pipenv shell: 

  > pushd implementation/eval-web

  > pipenv shell

  The benchmark script `evaluation.py` contains several functions for running the RQ1 experiments: 
  
  + `run_all_macro()` runs the macrobenchmarks, and takes an optional keyword parameters `examples` for the number of training examples, and optional positional arguments for a subset of benchmarks. For example, `run_all_macro()` runs all benchmarks with 10 training examples, while `run_all_macro("ace", "ddg", examples=5)` runs the Ace and DuckDuckGo benchmarks with 5 training examples. 
  
  + `run_all_micro` runs the microbenchmarks, and similarly takes optional positional arguments for a benchmark subset and an optional keyword argument `train_examples` for number of training examples. For example,
  `run_all_micro('synthetic', train_examples=3)` runs the synthetic benchmarks with 3 training examples.

  First run both the micro and macrobenchmarks with 3 training examples.

  > python -i evaluation.py

  > run_all_micro(train_examples=3)

  > run_all_macro(examples=3)

  WARNING: This will take a long time (TODO time on our machine). The output will be in TODO. Copy this output to the corresponding Excel spreadsheets in `experiments` i.e. `experiments/overall/micro.xlsx` and `experiments/overall/macro.xlsx`. 

  For `macro.xlsx`, put the data into the K1-AI11 cells of the macro 3 examples sheet. For `micro.xlsx`, put the data into the A1-J167 of the 3ex sheet. 

  Next, repeat the process for 10 training examples: 

  > python -i evaluation.py

  > run_all_micro()

  > run_all_macro()

  Again, this will take a long time. Copy the output into `micro.xlsx` and `macro.xlsx`; for macro, place the data into the macro_10_training_examples sheet, and for micro, place the data into the 10ex sheet.

  Ensure that the sheets update properly. In particular, the Table sheet of macro should roughly correspond to Table 1 and the Table sheet of micro should roughly correspond to Table 2.

  Once this is done, exit the pipenv shell and return to the root: 

  > exit

  > popd

- RQ2: First change directory to `implementation/eval-web/` and start a pipenv shell: 

  > pushd implementation/eval-web

  > pipenv shell

  The `run_all_micro` function takes an additional `loclearn` keyword argument.
  For this experiment, we must run 6 commands:

  > run_all_micro(loclearn='bayesian')

  Copy the output of this command (which should be a CSV) to the CSV file `experiments/noise/10/nt-all.csv`.

  > run_all_micro(loclearn='bayesian', train_examples=3)

  Copy the output to `experiments/noise/3/nt-all.csv`.

  > run_all_micro(loclearn='nt-none')

  Copy the output of this command to `experiments/noise/10/nt-none.csv`.

  > run_all_micro(loclearn='nt-none', train_examples=3)

  Copy the output to `experiments/noise/3/nt-none.csv`.

  > run_all_micro(loclearn='simple')

  Copy the output to `experiments/noise/10/baseline.csv`.

  > run_all_micro(loclearn='simple', train_examples=3)

  Copy the output to `experiments/noise/3/baseline.csv`.

  Once these commands are done, generate the graphs for RQ2 by following the instructions above and compare the output to Figures 5 and 6.

  Finally, exit the pipenv shell and return to the root directory:

  > exit

  > popd

- RQ3: First change directory to `implementation/eval-web/` and start a pipenv shell: 

  > pushd implementation/eval-web

  > pipenv shell

  For the hierarchical experiment, open the `evaluation.py` script in python and run the `run_hier_eval` function: 

  > python3 -i evaluation.py

  > run_hier_eval(True)

  This will produce the hierarchical scaling data. Place this data into `experiments/scaling/scaling_data.csv`, change directory to `experiments/scaling/` and run the `import_scaling.py` python script: 

  > popd 

  > pushd experiments/scaling

  > python3 import_scaling.py

  This should print out a set of benchmark rows in CSV format. Copy-paste this data into `experiments/scaling/scaling_sheet.xlsx` under the hier cell, 
  in cells L9 through V19.

  Next repeat the process for the baseline scaling data by returning
  to the previous directory and running `run_hier_eval` again, this time with 
  `False` as an argument: 

  > popd

  > pushd implementation/eval-web

  > python3 -i evaluation.py

  > run_hier_eval(False)

  > popd

  > pushd experiments/scaling

  As before, copy-paste the baseline scaling data into `experiments/scaling/scaling_data.csv`. Make sure to completely replace all of the previous data, 
  and then rerun `import_scaling.py`:

  > python3 import_scaling.py

  Copy-paste this data into `experiments/scaling/scaling_sheet.xlsx`, this time under the base cell, cells X9 through AH19. 

  The graphs should automatically update when the data is imported into the sheet. Verify that they match the scaling claims of RQ3. Once finished,
  exit the pipenv shell and return to the root directory: 

  > exit

  > popd

- RQ4: First change directory into the `implementation/eval-android/` folder and start a new pipenv shell: 

  > pushd implementation/eval-android

  > pipenv shell

  Next, run the following command: 

  > python3 -c "from  src.mockdown_eval.inferui.eval import main; main()"

  This builds the data for RQ4 as a side-effect of running its evaluation and writes it out into `implementation/eval-web/tmp/results.csv`.

  Once the command finishes, copy `implementation/eval-web/tmp/results.csv` into the `experiments/android/android_results.csv` file.

  Rebuild the graphs for RQ4 using the instructions above and compare the PNG files to the claims of RQ4 (i.e. Figure 8).

  WARNING: the output file `implementation/eval-web/tmp/results.csv` is not cleared between runs. If this command is run several times, delete the contents of `implementation/eval-web/tmp/results.csv` to ensure clean data.

  Once finished, exit the pipenv shell and return to the root directory:

  > exit

  > popd

### Running on a new benchmark

There are two options for running Mockdown on a new benchmark.
First, you can directly provide JSON that corresponds to several renderings of a layout. See `implementation/mockdown/tests/inferui/onetwo.json` for a simple example.

Second, you can use `implementation/eval-web/` to scrape a web layout from a arbitrary web page. The process is rather involved and manual: see `implementation/eval-web/README.md` for detailed instructions and feel free to reach out to the authors for troubleshooting. Our layout scraper is tested on Mozilla FireFox and works for most websites, but might break on arbitrary web layouts. 