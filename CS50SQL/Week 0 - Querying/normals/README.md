This README is available in [Portuguese](README.pt-BR.md).
# Normals
## Background

As cited in [Normals](https://cs50.harvard.edu/sql/2024/psets/0/normals/) – CS50’s Introduction to Databases with SQL:

> “On the heels of a new annual heat record set in 2022 — the latest in a string of record-setting years — average ocean surface temperatures around the globe have spiked since early March. Excluding polar regions, they are about two-tenths of a degree Celsius warmer than scientists have ever observed at this time of year via satellite data.”  
>  
> — [The Washington Post](https://www.washingtonpost.com/climate-environment/2023/04/28/ocean-temperatures-heat-record-surge-climate/), April 28, 2023

To determine whether ocean temperatures deviate from typical values, scientists use a metric known as a Climate Normal, which represents long-term climate patterns based on 30-year periods. One key indicator included in this metric is ocean temperature.


## Problem Description

This project involves analysing data from a database named `normals.db`, specifically the `normals` table, to examine recent Climate Normal data and better understand the characteristics of normal ocean temperatures across the globe. The task is to write SQL queries that answer a series of questions about the Climate Normal.


## Dataset
For this problem, the database `normals.db` along side with *ten* .sql empty files are provide.  
The single table `normals` within `normals.db` contains the following columns:
- `id`: uniquely identifies each row in the table.
- `latitude`: the degree of latitude — expressed in decimal format.
- `longitude`: the degree of longitude — expressed in decimal format.
- `0m`: the normal ocean surface temperature (i.e., the normal temperature at 0 meters of depth), in degrees Celsius, at the coordinate.
- `5m`: the normal ocean temperature at 5 meters of depth, in degrees Celsius, at the coordinate.
- `10m` the normal temperature at 10 meteres of depth, in degrees Celsius, at the coordinate.

Observations continue up to `5500m` for some coordinates.


## Specification
- Each query should consist of a single `SELECT` statement.
- No assumptions should be made about the `id` values of any particular observations — queries must remain valid regardless of those values.
- Each query should return **only** the data necessary to answer the question.
- Each SQL query must be written in a separate file, named according to the corresponding question number (e.g., 1.sql for question 1, 2.sql for question 2, and so on).


## Questions
Below is a list of the 10 questions answered using SQL queries.  


- [X] **Q1:** Find the normal ocean surface temperature in the [Gulf of Maine](#gulf), off the coast of Massachusetts. 
- [X] **Q2:** Find the normal temperature of the [deepest sensor](#deepest) near the Gulf of Maine, at the same coordinate above.
- [X] **Q3:** Choose a location of your own and find the normal temperature at 0 meters, 100 meters, and 200 meters.
- [X] **Q4:** Find the lowest normal ocean surface temperature.
- [X] **Q5:** Find the highest normal ocean surface temperature.
- [X] **Q6:** Return all normal ocean temperatures at 50m of depth, as well as their respective degrees of latitude and longitude, within the Arabian Sea. Include latitude, longitude, and temperature columns. Assume the Arabian Sea is encased in the following four coordinates:
    - 20° of latitude, 55° of longitude
    - 20° of latitude, 75° of longitude
    - 0° of latitude, 55° degrees of longitude
    - 0° of latitude, 75° degrees of longitude
- [X] **Q7:** Find the average ocean surface temperature, rounded to two decimal places, along the equator. Call the resulting column “Average Equator Ocean Surface Temperature”.
    
- [X] **Q8:** Find the 10 locations with the lowest normal ocean surface temperature, sorted coldest to warmest. If two locations have the same normal ocean surface temperature, sort by latitude, smallest to largest. Include latitude, longitude, and surface temperature columns.
- [X] **Q9:** Find the 10 locations with the highest normal ocean surface temperature, sorted warmest to coldest. If two locations have the same normal ocean surface temperature, sort by latitude, smallest to largest. Include latitude, longitude, and surface temperature columns.
- [X] **Q10:** There are 180 whole degrees of latitude. For this question, determine how many points of latitude we have at least one data point for. (Why might we not have data points for all latitudes?)


## Hints provided
```
Since normals is a wide table, consider SELECTing only the latitude, longitude, and a few depth columns.
```
- The normal ocean surface temperature is in the `0m` column, which stands for 0 meters of depth!

- <a name="gulf"></a> The Gulf of Maine is at 42.5° of latitude and -69.5° of longitude.

- <a name="deepest"></a> The deepest sensor near the Gulf of Maine records temperatures at 225 meters of depth, so this data in the `225m` column.
- The equator’s ocean surface temperatures can be found at all longitudes between the latitudes -0.5° and 0.5°, inclusive.
- May Google Earth be helpful to find some coordinates.


## Source
This README was based on the documentation of the *Normals* problem from Harvard University's course **CS50’s Introduction to Databases with SQL**, available at: [https://cs50.harvard.edu/sql/2024/psets/0/normals/](https://cs50.harvard.edu/sql/2024/psets/0/normals/)
