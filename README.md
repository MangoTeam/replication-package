# fse-21-24-replication-package
Replication package for FSE 2021 submission #24, titled Synthesis of Web Layouts from Examples.

This package is structured as follows.

- `layouts/` contains json files that correspond to the scraped micro and macrobenchmarks. 
- `experiments/` contains data and scripts for our experiments:
  + RQ1 is evaluated in `experiments/overall/`. This folder contains several CSV files that correspond to the RQ1 trials: `micro-10.csv`, `micro-3.csv`, `macro-10.csv`, and `macro-3.csv`.
  There are two excel spreadsheet for building the RQ1 tables: `macro.xls`, which builds Table 1, and `micro.xls` which builds Table 2.
  To move data into the excel spreadsheets, directly copy the contents of the CSV files into the respective sheet. For example, to rebuild Table 1 with new data for `micro-3.csv`, copy the contents of `micro-3.csv` into the 3ex sheet of `micro.xls`. The new Table 2 is automatically updated in the Table sheet of `micro.xls`; notice that it contains an extra (extraneous) row for summary statistics about the hierarchical benchmarks.

  + RQ2 is evaluated in `experiments/noise/`, which contains 6 CSV files that correspond to the 3 algorithms run on 3 and 10 training examples: `3/baseline.csv`, `3/nt-none.csv`, `3/nt-all.csv`, `10/baseline.csv`, `10/nt-none.csv`, and `10/nt-none.csv`.
  To build the graphs for RQ2, Figure 5 and Figure 6, we provide a plotting script in the parent directory of `experiments`, `plot.py`. For Figure 5, load the script (using pipenv and a python3 shell) and run `plot_accuracy()` and `plot_error()` from the python shell. For Figure 6, load the script in a similar manner and run `plot_synth_time()`. This script produces plots in png format (e.g. `error_3.png`), which correspond to the subfigures of RQ2.

  + RQ3 is evaluated in `experiments/scaling/`, which contains a CSV file that corresponds to the two studies: `scaling_data.csv`.
  To build the graph for RQ3 (Figure 7), run `import_scaling.py` and then copy-paste the result into the excel spreadsheet `scaling_sheet.xlsx`. There is only one sheet, with one graph, and the graph should automatically update when the data is changed.

  + RQ4 is evaluated in `experiments/android/`, which contains a single CSV that corresponds to all of the trials: `android_results.csv`.
  To build the graph for RQ4, Figure 8, we again use the plotting script in `experiments`, `plot.py`. Load the script (using pipenv and a python3 shell) and run `plot_error_android()` and `plot_accuracy_android()`. This script produces plots in png format that correspond to the subfigures of Figure 8.
- `implementation/` contains the source code, as well as runner scripts for regenerating the raw data for the experiments.
  + Our main tool is in `implementation/mockdown/` and has installation instructions its own `README.md` file.
  Several example inputs are in `tests/`, for example `tests/inferui/onetwo.json`.
  Mockdown can be run by command line or as a server on the localhost. Of these, command line is easiest to use;
  for usage, run `mockdown run --help` from a pipenv shell within the Mockdown directory.

  + Our website layout backend is in `implementation/web/` and can be run using `npm`. We currently manually scrape layouts and the process is detailed in `web/README.md`.

    To regenerate the experimental data for RQ1, RQ2, and RQ3, we provide an evaluation script `web/evaluation.py`. The output is put in a CSV file within `web/eval/tmp`; the exact location is printed out by the benchmark command.
  
    First load the script in a pipenv environment to have access to the script's functions:

    * For RQ1, the macrobenchmarks can be rerun by running `run_all_macro()`, and the keyword argument `examples` determines the number of training examples. The microbenchmarks are similarly run with `run_all_micro()` (with keyword argument `training_examples`).

      If just one benchmark is desired, the benchmark name can be given as a positional argument. 
      For example, `run_all_macro("ace", examples=3)` runs the ace macro benchmark with 3 training examples; and `run_all_micro(examples=10)` runs all of the microbenchmarks.

    * For RQ2, the results are obtained by running `run_all_micro` with an additional `loclearn` positional argument, which is either `"bayesian"` for the full algorithm (the default, `nt-all`), `"nt-none"` for `nt-none`, or `"simple"` for the baseline algorithm. 

    * For RQ3, run `run_hier_eval(True)` to collect the hierarchical scaling numbers and `run_hier_eval(False)` for flat scaling numbers.

  + Our android layout backend is in `implementation/android/` and can be run using the instructions in `android/README.md`. 
  It builds the data for RQ4 as a side-effect of running the evaluation and places the result in `implementation/web/tmp/results.csv`.