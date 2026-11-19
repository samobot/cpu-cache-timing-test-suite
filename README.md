# Cache timing attack vulnerability test suite

This repo is based on the code from the following paper:

`A Benchmark Suite for Evaluating Caches’ Vulnerability to Timing Attacks`

## Code
The unmodified code from the paper can be found under the tag [original_code](https://github.com/samobot/cpu-cache-timing-test-suite/releases/tag/orignal_code).  It does not compile under modern versions of gcc.  We found that gcc 7 works to compile the original.

The original code has been modified to allow it to compile on gcc 16.  The supporting scripts have also been modified where possible for improved convenience.

## Compiling
The compilation commands and flags are taken care of by the `run_autodetect` scripts.  The C files generated only make use of C standard libraries and linux headers, so no additional libraries are needed.  The code has been tested to work on gcc 16, other versions may yield different results.

## Running
The scripts `run_autodetect.sh` and `run_autodetect_bcm2711.sh` can be used to compile and run the tests on x64 and ARM respectively.

Their input is as follows:

```bash
./run_autodetect.sh <max_cycle> <num_test> <cpu_id> <each_run> <output_name>
```

| input | function (based on original README.txt) |
| - | - |
| max_cycle | maximum cycles for a specific memory related operation |
| num_test * each_run | total number of tests run for a three-step case |
| cpu_id | ID of the CPU being tested (can be found near the top of gen_vulnerabilities_clean.c) | 
| output_name | name of output file, written to `benchmark_output/<output_name>.output(.res)`

The original paper used the values: `./run_autodetect.sh 8000 10 <cpu_id> 30 <output_name>` so we did as well in our testing.

The `autodetect` scripts should automatically pull information such as processor architecture and cache structure and pass it to `run.sh`.  If this does not work, the information can be passed in manually as described in [README.txt](README.txt).

## Generating plots
Some tests from the suite are not plotted.  Because of this, the resulting `.output.res` files from processing need to be transformed to `.output.res.tran` files before they can be plotted.  We wrote a small script to do this automatically:

```bash
python sanitize_output.py <test_file_name>
```
where `<test_file_name>` does not include the `.output.res` extension

After sanitization, plots showing the results of the tests can be generated using `plot_res_simplified.py`.  Just modify the `files` and `names` arrays to match the names of the `.output.res.tran` files and processor names.  Then generate the plots with
```bash
python plot_res_simplified.py <pdf_name>
```
the outputs are written to `gen_figure/vul_by_type_<pdf_name>.pdf`.

## Supporting new CPUs
To add more CPUs to the test suite, `gen_vulnerabilites.c` can be modified.  Before adding a CPU, it may be worth checking if one of the CPUs already included is similar enough to your CPU.  The main things that matter are comparable core count and whether hyperthreading is supported, as CPUs that don't support hyperthreading skip some tests.

Changes required:
| line # | change |
| - | - |
| 71 | create a `#define` assigning your CPU a number (this is the cpu_id you should use when running)
| 1702 | add a branch on the if statement assigning CPUs |
| 2188-2225 | **if** your CPU does not support hyperthreading, add it to the list of other CPUs in each of the 4 `else if` statements in that section.  This will ensure the hyperthreading tests are skipped |