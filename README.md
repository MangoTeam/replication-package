[![DOI](https://zenodo.org/badge/363007493.svg)](https://zenodo.org/badge/latestdoi/363007493)

# FSE '21 Mockdown replication package
This a replication package for FSE 2021 submission Synthesis of Web Layouts from Examples, hosted on Github at [https://github.com/MangoTeam/replication-package](https://github.com/MangoTeam/replication-package).
It contains our experimental data, scraped web layouts, our implementation as submodules,
and a Vagrant provisioning script for replicating our experimental results.

## Important Note:

This package contains the necessary artifacts for installing Mockdown, as well as for building a virtual machine image in which our experiements may be replicated.

**A copy of the VM image this repository builds may be found at https://zenodo.org/record/5112648.**

If for any reason the instructions for installation/replication (contained in `INSTALL.md`) fail, please boot this image in VirtualBox. It may be a bit slower than running natively (see the note on performance in `INSTALL.md`) but it will be sufficient to verify that the tool does work.

If you wish to install the tool natively (without a VM) please follow along with `provision.sh`, subsituting the initial package management commands with those appropriate for your system (see `REQUIREMENTS.md` for more details). The individual subpackages in this replication package include pinned (Python/JS) dependencies in the form of lockfiles to make this as simple as possible.

## Package Structure (for the purpose of evaluation)

Note: an alternative (and more detailed) description of package structure is listed in `INSTALL.md`, which provides more details on the contents of the `implementation` directory, and is intended for those who wish to install the packages directly rather than just use the provided VM/Vagrantfile.

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

If you are evaluating using the provided `Vagrantfile` via `vagrant up`, use `vagrant ssh` to connect to the image and then navigate to the evaluation directory by `cd /vagrant`. 

Note: our `author` and `conference` benchmarks were previously named `john` and `icse`. We attempted to anonymize them as much as possible, but there might be some places where the benchmarks and output data refer to the original name. 

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

We have included helper scripts for rerunning each of the experiments. In all cases the output data will be as a CSV file within `implementation/` and needs to be copied to the corresponding file within `experiments/`. 

CAVEATS and WARNING: there might be timing (and timeout) differences due to overhead
of running from within a VM. 

Also, the benchmark scripts take a long time to finish
(each command takes 1-4 hours and there are 13 commands in total), so if you are going
to run these experiments on a time budget, it would be best to start early and 
set them running on a server or background VM.

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

  WARNING: This will take a long time (on our testing VM, `run_all_macro()` takes roughly 3.5 hours to complete and `run_all_micro()` takes roughly 1.5 hours).
  
  Once finished, the command will say where output data is saved, for example: 


```
(eval-web) vagrant@vagrant:/vagrant/implementation/eval-web$ python3 -i evaluation.py
>>> run_all_macro()
starting macrobenchmarks
worst case amount of work in seconds: 54000
on 0: running macro personal
on 0: Running bench personal, john
on 0: Finished.
on 1: running macro icse
on 1: Running bench icse, icse
on 1: Finished.
on 1: invalid parse of result in eval/tmp/macro-examples-10-1900-01-01-15-32-27/bench-icse-0.log
on 2: running macro hackernews
on 2: Running bench hackernews, hn
...
on 29: Running bench ddg, ddg
on 29: Finished.
on 30: done! results printed to eval/tmp/macro-examples-10-1900-01-01-15-32-27/macro_results.csv
```
   In this case the output is being saved in `implementation/eval-web/eval/tmp/macro-examples-10-1900-01-01-15-32-27/macro_results.csv`. It is fine if there are some lines with invalid parses, this happens when the benchmark times out.

   If all of the trials raise an invalid parse error, please check the log and contact us for troubleshooting.

  For `macro.xlsx`, the output runs are combined in the same CSV file. Put this data into the K2-AI11 cells of the macro 3 examples sheet. Make sure to manually split the trials up into three separate tables (i.e. K2-R11 should contain data for one run of john through ddg, S2-Z11 contain data for a second run of john through ddg, etc).
  
   For `micro.xlsx`, put the data into the A1-J167 of the 3ex sheet. 

  Next, repeat the process for 10 training examples: 

  > python -i evaluation.py

  > run_all_micro(train_examples=10)

  > run_all_macro(examples=10)

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

  > run_all_micro(loclearn='bayesian', train_examples=10)

  Copy the output of this command (which should be a CSV) to the CSV file `experiments/noise/10/nt-all.csv`.

  > run_all_micro(loclearn='bayesian', train_examples=3)

  Copy the output to `experiments/noise/3/nt-all.csv`.

  > run_all_micro(loclearn='nt-none', train_examples=10)

  Copy the output of this command to `experiments/noise/10/nt-none.csv`.

  > run_all_micro(loclearn='nt-none', train_examples=3)

  Copy the output to `experiments/noise/3/nt-none.csv`.

  > run_all_micro(loclearn='simple', train_examples=10)

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

Second, you can use `implementation/eval-web/` to scrape a web layout from a arbitrary web page. The process is rather involved and manual: see `implementation/eval-web/README.md` for detailed instructions and feel free to reach out to the authors for troubleshooting. Our layout scraper is tested on Mozilla Firefox and works for most websites, but might break on arbitrary web layouts. 
