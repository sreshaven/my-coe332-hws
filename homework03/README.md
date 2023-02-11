# Homework 3 - The World Has Turned and Left Me Turbid

## Summary

This assignment is a continuation of Homework 2 in which there is a robot collecting meteorite samples. In order to study these samples, the lab needs to have clean water so that the analysis is accurate and not affected by other variables in the water, and the goal of this assignment is to help ensure that the water in the lab is safe to use. The `analyze_water.py` script uses water quality data readings to calculate turbidity of a sample and determines if the water sample is safe to use or needs more time to fall below the safe threshold. The `test_analyze_water.py` uses unit testing to test if the calculations in `analyze_water.py` are accurate.

## Turbidity Dataset

The `analyze_water.py` script uses a water quality data set located at [this link](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json) in order to calculate the turbidity at each reading. This data set is a JSON dictionary that has a key names `turbidity_data` and its value is a list of dictionaries. In each dictionary, there is information about each reading, such as time it was analyzed, sample volume, calibration constant, ninety degree detector current, and the name of the person who analyzed the sample.

## Part 1

The `analyze_water.py` script uses a turbidity dataset, described in [Turbidity Dataset](#turbidity-dataset), to calculate average turbidity (which is caused by particles suspended or dissolved in water) of the five most recent readings and determines if the water sample is safe to use or needs more time to fall below the safe threshold. If the calculated turbidity is above the safe threshold, the amount of minimum time needed so that it is safe to use is also calculated.

### Requirements

In order to run the `analyze_water.py`, you need to have the python `requests` library installed.

## Part 2

The `test_analyze_water.py` uses unit testing to test that the `calc_turbidity()` and `calc_min_time()` functions are working as intended and that the equations in `analyze_water.py` provide correct results. Each test case has 2 assert statements to help determine if the functions work for different scenarios.

### Requirements

To run `test_analyze_water.py`, the `pytest` library should be installed.

## Instructions

In order to run the code located here at `my-coe332-hws/homework03`, first clone this repository to your local system using `git clone git@github.com:sreshaven/my-coe332-hws.git`. Next, change your current directory using `cd my-coe322-hws/homework03/`. Then, run the command `python3 analyze_water.py`, which will run the script described in [Part 1](#part-1) and return information about 5 most recent samplings in the Turbidity Dataset. Below is an example of what the output looks like after executing the script:
```
Average turbidity based on most recent five measurements = 0.6820 NTU
Info: Turbidity is below threshold for safe use
Minimum time required to return below a safe threshold = 0 hours
```

Next, in order to run the script from [Part 2](#part-2) with the unit tests, run `pytest`. This will output information about the results of these tests (such as if they passed or failed and why), and an example success output is below:
```
=================================================================== test session starts ====================================================================
platform linux -- Python 3.8.10, pytest-7.2.1, pluggy-1.0.0
rootdir: /home/ubuntu/my-coe332-hws/homework03
collected 2 items

test_analyze_water.py ..                                                                                                                             [100%]

==================================================================== 2 passed in 0.11s =====================================================================
```
