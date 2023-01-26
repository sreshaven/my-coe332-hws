# Homework 1 - No One JSON 

## Summary

In this assignment, we are simulating a robotic vehicle on Mars that is investigating five meteorite landing sites that are located in Syrtis Major, which is a quadrangle region on Mars. This assignment directory contains two python scripts: one that sets up the simulation by generating five random landing site locations and assigning meteorite compositions to each and another script that calculates the time it takes for the vehicle to visit and take samples from each site. This simulation is important as it can give an approximation for the amount of time and distance that the vehicle needs to travel and work.

## Part 1

`generate_sites.py` is the python script that helps set up the simulation by randomly generating characteristics for the 5 landing sites and puts all of this information in a .json file called `landing_sites.json`. For each landing site, the script assigns a random latitude between 16.0 and 18.0 degrees, a longitude between 82.0 and 84.0, and a meteorite composition of either "stony", "iron", or "stony-iron".

## Part 2

`calculate_trip.py` is the python script that calculates the total time needed for the robotic vehicle to visit the five landing sites in order from 1 to 5 based on the info from the .json file from Part 1. We assume that the vehicle starts at (16.0, 82.0) and moves at a speed of 10 km/hr, and each composition type also has a specific amount of sampling time that is added to the travel time. The distances between each landing site are calculated using the great-circle distance algorithm.

## Instructions
In order to run the code located here at `my-coe332-hws/homework02`, first run the command `python3 generate_sites.py`, which will create `landing_sites.json` that contains the info about the 5 landing sites. Next, in order to run a simulation of the vehicle traveling to the sites, run `python3 calculate_trip.py`. This will output information at each leg of the trip such as time to travel from the current site to the next, and the amount of time it will take to sample the meteorite at this site. The last line of the output has an overview of the trip with the calculated total travel time.
