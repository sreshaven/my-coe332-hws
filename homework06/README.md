# Homework 6 - Say It Ain’t Genes

## Summary

The EPA, or the Environmental Protection Agency, is an executive agency of the US federal government that is tasked with environmental protection matters. One of their roles is to collect and analyze data related to environmental issues in order to help reduce risks to the environment based on the best available scientific information and to review the safety of parts of society. The EPA collects data about Automotive Trends in the United States to aid in their mission and investigate the effect of the automotive industry on the environment. The goal of this assignment is to create a Flask API that is containerized and injects the Auto Trends data set into a Redis database. The Flask API will have routes that help with getting access to information directly from the database.

## About the Auto Trends Data Set

The EPA and NHTSA (National Highway Traffic Safety Administration) collects data from directly car manufacturers annually about their vehicles. The database has been maintained by the EPA since 1975 and has up to date data available for all model years since then, with preliminary data for 2022. In this data set, there is information about manufacturer and vehicle type, which are categorical values, and model year, production share, compliance and estimated real-world MPG, CO2 emissions, weight, horsepower, and many more, which are numerical values. The data is split into vehicle type categories of sedan/wagon, car SUV, truck SUV, minivan/van, and pickup and the data set also has average observations for all of the cars and all of the trucks. These values reflect arithmetic and harmonic production-weighted averages for each vehicle type. 

## Flask App

The Auto Trends Flask App, located in the `auto_trends_api.py`, helps with processing the Auto Trends data set and adding it into a Redis database so that the data is preserved beyond the lifetime of the application containers. The Flask App also allows the user to query the dataset based on year or manufacturer to get more specific data to help save time in investigating efforts since the data set is so large. The Flask App is also containerized using Docker to allow for more portablility annd easier access to users.

### Run Instructions

In order to run the Flask app and query through the dataset using routes, there are a few steps to the process:

1. Clone this repository to your local system using `git clone git@github.com:sreshaven/my-coe332-hws.git` and change your current directory using `cd my-coe322-hws/homework06/` 

2. Next, get the `auto_trends_api` image in order to start a container for the Flask App. There are two methods to do this:

_Method #1_: Pull the existing image from Docker Hub using the command: `docker pull sreshaven/auto_trends_api:hw06`

_Method #2_: Build the Docker image locally from the Dockerfile in the repository. To do this, first download the Auto Trends dataset located here: [https://www.epa.gov/automotive-trends/explore-automotive-trends-data#DetailedData](https://www.epa.gov/automotive-trends/explore-automotive-trends-data#DetailedData). Click on the blue button that says "Export Detailed Data by Manufacturer" (which is Table A-1 on the site) to download the file to your local system. Rename this file to `auto_trends_data.csv` and move this file to the homework06/ directory. In the homework06/ directory, use `docker build -t <username>/auto_trends_api:hw06 .` and replace `<username>` with your username to build the image using the Dockerfile in the repository. In the docker-compose.yml file, change the line that says `image: sreshaven/auto_trends_api:hw06` by replacing `sreshaven` with your username.

3. Then, make a directory in the homework06/ directory to which the Redis database can mount a volume to by using `mkdir data`.

4. Lastly, to start up the flask app in detached mode using the Docker Compose file in the repository, run `docker-compose up -d`. 

Now, you can use the Flask App to inject the dataset into a Redis database and query the dataset using the routes and examples described in the section below.

### Routes and Examples


