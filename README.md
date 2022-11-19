# Yield curves

This repository contains scripts for a simple, user prompted program to return plots of either:

- regression slopes of US treasury bond yields over a month or year;
- the latest US treasury bond yields itself.

Data is obtained from the US treasury department website, https://home.treasury.gov/.

The yield curve is *inverted* if its regression slope is negative. Inverted yield curves indicate oncoming recessions, apparently. 

## Run

Run the script `main.py` and follow the prompts. Data is downloaded and stored in the folder `/datasets`.

**Note.** *If queying data which changes day-to-day (e.g., data for the current year), you need to delete this record from `\datasets`. Otherwise, the program will simply use the stored data in `/datasets` and you won't query new data.*

## Prerequisites

Packages needed to run the program `main.py` are: 

- `scipy`
- `pandas`
- `matplotlib`
- `datetime`




