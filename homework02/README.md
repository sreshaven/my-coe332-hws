# Homework 1 - No One JSON 

## Summary

In this assignment, we are simulating a robotic vehicle on Mars that is investigating five meteorite landing sites that are located in Syrtis Major, which is a quadrangle region on Mars. This assignment directory contains two python scripts: one that sets up the simulation by generating five random landing site locations and assigning meteorite compositions to each and another script that calculates the time it takes for the vehicle to visit and take samples from each site. This simulation is important as it can give an approximation for the amount of time and distance that the vehicle needs to travel and work.

## Part 1

`generate_sites.py` is the python script that helps set up the simulation by randomly generating characteristics for the 5 landing sites and puts all of this information in a .json file called `landing_sites.json`. For each landing site, the script assigns a random latitude between 16.0 and 18.0 degrees, a longitude between 82.0 and 84.0, and a meteorite composition of either "stony", "iron", or "stony-iron". Below is a snippet of what the output `landing-sites.json` looks like:

```
{
  "sites": [
    {
      "site_id": 1,
      "latitude": 16.99694090390324,
      "longitude": 82.92614210281195,
      "composition": "iron"
    },
    {
      "site_id": 2,
      "latitude": 16.003086245772536,
      "longitude": 83.22587151296021,
      "composition": "iron"
    },
    {
      "site_id": 3,
      "latitude": 16.247294960323483,
      "longitude": 83.35316847766327,
      "composition": "stony"
    },
...
```

## Part 2

`calculate_trip.py` is the python script that calculates the total time needed for the robotic vehicle to visit the five landing sites in order from 1 to 5 based on the info from the .json file from Part 1. We assume that the vehicle starts at (16.0, 82.0) and moves at a speed of 10 km/hr, and each composition type also has a specific amount of sampling time that is added to the travel time. The distances between each landing site are calculated using the great-circle distance algorithm. This script outputs information to the console about each leg of the trip when the vehicle travels from one site to the next one and provide details such as the calculated time to travel based on the distance and time needed to sample the specific meteorite composition. The last line is a summary of the trip with the total time taken to complete the trip in the simulation. Below is an example of what the output looks like when you run this script:

```
leg = 1, time to travel = 7.90 hr, time to sample = 2 hr
leg = 2, time to travel = 6.12 hr, time to sample = 2 hr
leg = 3, time to travel = 1.62 hr, time to sample = 1 hr
leg = 4, time to travel = 9.75 hr, time to sample = 2 hr
leg = 5, time to travel = 3.50 hr, time to sample = 3 hr
==============================
number of legs = 5, total time elapsed = 38.88 hr
```

## Instructions

In order to run the code located here at `my-coe332-hws/homework02`, first clone this repository to your local system using `git clone git@github.com:sreshaven/my-coe332-hws.git`. Next, change your current directory using `cd my-coe322-hws/homework02/`. Then, run the command `python3 generate_sites.py`, which will create `landing_sites.json` that contains the info about the 5 landing sites. Next, in order to run a simulation of the vehicle traveling to the sites, run `python3 calculate_trip.py`. This will output information about the trip to the console. An example output is shown in section Part 2.
